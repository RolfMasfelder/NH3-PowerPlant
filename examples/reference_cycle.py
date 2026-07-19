"""
Minimal NH3 reference cycle example.
"""

from __future__ import annotations

import argparse
import logging
from pathlib import Path
from typing import Any

from nh3powerplant import __version__
from nh3powerplant.connection import Connection
from nh3powerplant.components import Condenser
from nh3powerplant.components import Evaporator
from nh3powerplant.components import Generator
from nh3powerplant.components import Pump
from nh3powerplant.components import Turbine
from nh3powerplant.core.exceptions import SimulationError
from nh3powerplant.core.identifier import Identifier
from nh3powerplant.fluids import CoolPropFluid
from nh3powerplant.results import JsonResultIO
from nh3powerplant.results import RunInfo
from nh3powerplant.results import SimulationResult
from nh3powerplant.simulation import Simulation
from nh3powerplant.state.statepoint import StatePoint


EVAPORATION_TEMPERATURE = 353.15
CONDENSATION_TEMPERATURE = 293.15
COLD_RESERVOIR_TEMPERATURE = 281.15
PUMP_EFFICIENCY = 0.75
TURBINE_EFFICIENCY = 0.82
GENERATOR_EFFICIENCY = 0.96
HEAT_PUMP_COP = 3.0
TARGET_ELECTRICAL_POWER = 100_000.0
OUTPUT_PATH = Path("results/reference_cycle/result.json")
LOG_PATH = Path("results/reference_cycle/reference_cycle.log")
PUMP_POWER_NAME = "pump power"
TURBINE_POWER_NAME = "turbine power"
EVAPORATOR_HEAT_NAME = "evaporator heat"
CONDENSER_HEAT_NAME = "condenser heat"
GENERATOR_ELECTRICAL_POWER_NAME = "generator electrical power"
HEAT_PUMP_POWER_NAME = "heat pump power"
COLD_RESERVOIR_HEAT_NAME = "cold reservoir heat"

logger = logging.getLogger(__name__)


def main() -> None:
    """
    Run the reference cycle and write the result JSON file.
    """
    args = _parse_args()
    configure_logging(LOG_PATH)
    logger.info("Starting reference cycle example")
    result = run_reference_cycle(heat_pump_cop=args.heat_pump_cop)
    JsonResultIO().write(result, OUTPUT_PATH)
    logger.info("Wrote result JSON to %s", OUTPUT_PATH)
    print(f"Wrote {OUTPUT_PATH}")
    print(f"Wrote {LOG_PATH}")
    print(f"heat pump COP: {args.heat_pump_cop:.2f}")
    print(f"gross electrical power: {result.components[-1]['electrical_power']:.2f} W")
    print(f"net electrical power: {result.efficiencies[0]['value']:.2f} W")


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the NH3 reference cycle example.")
    parser.add_argument(
        "--heat-pump-cop",
        type=float,
        default=HEAT_PUMP_COP,
        help="Prescribed heating COP of the external heat pump.",
    )
    args = parser.parse_args()
    if args.heat_pump_cop <= 1.0:
        parser.error("--heat-pump-cop must be greater than 1.0")
    return args


def configure_logging(path: Path) -> None:
    """
    Configure file logging for the reference cycle example.
    """
    path.parent.mkdir(parents=True, exist_ok=True)

    handler = logging.FileHandler(path, mode="w", encoding="utf-8")
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(
        logging.Formatter(
            fmt="%(asctime)s %(levelname)s %(name)s: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
    )

    for configured_logger in (logger, logging.getLogger("nh3powerplant")):
        configured_logger.handlers.clear()
        configured_logger.setLevel(logging.DEBUG)
        configured_logger.propagate = False
        configured_logger.addHandler(handler)


def run_reference_cycle(heat_pump_cop: float = HEAT_PUMP_COP) -> SimulationResult:
    """
    Calculate a simple saturated NH3 reference cycle.
    """
    if heat_pump_cop <= 1.0:
        raise ValueError("heat_pump_cop must be greater than 1.0")

    logger.info("Running unit cycle for mass-flow scaling")
    unit_cycle = _calculate_cycle(mass_flow=1.0)
    unit_generator_power = _required_float(
        "unit generator electrical power",
        unit_cycle["generator"].electrical_power,
    )
    mass_flow = _scaled_mass_flow(unit_generator_power)
    scaling_trace = _scaling_trace(
        unit_generator_power=unit_generator_power,
        mass_flow=mass_flow,
    )
    logger.info(
        "Scaled mass flow from unit run: unit_generator_power_W=%.6f, "
        "target_power_W=%.6f, mass_flow_kg_per_s=%.9f",
        unit_generator_power,
        TARGET_ELECTRICAL_POWER,
        mass_flow,
    )

    logger.info("Running scaled reference cycle")
    cycle = _calculate_cycle(mass_flow=mass_flow)

    pump = cycle["pump"]
    evaporator = cycle["evaporator"]
    turbine = cycle["turbine"]
    condenser = cycle["condenser"]
    generator = cycle["generator"]
    simulation = cycle["simulation"]

    pump_power = _required_float(PUMP_POWER_NAME, pump.power)
    turbine_power = _required_float(TURBINE_POWER_NAME, turbine.power)
    evaporator_heat = _required_float(EVAPORATOR_HEAT_NAME, evaporator.heat_flow)
    condenser_heat = _required_float(CONDENSER_HEAT_NAME, condenser.heat_flow)
    generator_power = _required_float(
        GENERATOR_ELECTRICAL_POWER_NAME,
        generator.electrical_power,
    )
    heat_pump_power = evaporator_heat / heat_pump_cop
    cold_reservoir_heat = evaporator_heat - heat_pump_power
    generator_loss = turbine_power - generator_power
    net_power = generator_power - pump_power - heat_pump_power
    external_power_import = max(-net_power, 0.0)
    external_power_export = max(net_power, 0.0)
    overall_inputs = cold_reservoir_heat + external_power_import
    overall_outputs = condenser_heat + generator_loss + external_power_export
    overall_residual = overall_inputs - overall_outputs
    logger.info(
        "Final powers: pump_W=%.6f, turbine_W=%.6f, generator_W=%.6f, "
        "evaporator_heat_W=%.6f, condenser_heat_W=%.6f, heat_pump_power_W=%.6f, "
        "cold_reservoir_heat_W=%.6f, net_power_W=%.6f",
        pump_power,
        turbine_power,
        generator_power,
        evaporator_heat,
        condenser_heat,
        heat_pump_power,
        cold_reservoir_heat,
        net_power,
    )
    logger.info(
        "Heat pump boundary: cold_reservoir_temperature_K=%.2f, "
        "cold_reservoir_heat_W=%.6f, electrical_power_W=%.6f, "
        "hot_heat_to_evaporator_W=%.6f, cop=%.6f; Evaporator.NH3.in is Rankine-cycle NH3, "
        "not the heat-pump cold side",
        COLD_RESERVOIR_TEMPERATURE,
        cold_reservoir_heat,
        heat_pump_power,
        evaporator_heat,
        heat_pump_cop,
    )
    logger.info(
        "Overall plant balance: cold_reservoir_heat_W=%.6f, "
        "external_power_import_W=%.6f, condenser_heat_W=%.6f, "
        "generator_loss_W=%.6f, external_power_export_W=%.6f, residual_W=%.6f",
        cold_reservoir_heat,
        external_power_import,
        condenser_heat,
        generator_loss,
        external_power_export,
        overall_residual,
    )

    return SimulationResult(
        run=RunInfo.create(
            id="reference-cycle",
            simulation_name="Minimal NH3 reference cycle",
            variant="A",
            description="Single-pass saturated NH3 cycle with prescribed COP.",
            project_version=__version__,
        ),
        configuration={
            "fluid": "NH3",
            "cold_reservoir_temperature_K": COLD_RESERVOIR_TEMPERATURE,
            "evaporation_temperature_K": EVAPORATION_TEMPERATURE,
            "condensation_temperature_K": CONDENSATION_TEMPERATURE,
            "pump_efficiency": PUMP_EFFICIENCY,
            "turbine_efficiency": TURBINE_EFFICIENCY,
            "generator_efficiency": GENERATOR_EFFICIENCY,
            "heat_pump_cop": heat_pump_cop,
            "target_electrical_power_W": TARGET_ELECTRICAL_POWER,
        },
        parameters=[
            _parameter("Cold reservoir temperature", COLD_RESERVOIR_TEMPERATURE, "K"),
            _parameter("Evaporation temperature", EVAPORATION_TEMPERATURE, "K"),
            _parameter("Condensation temperature", CONDENSATION_TEMPERATURE, "K"),
            _parameter("Mass flow", mass_flow, "kg/s"),
            _parameter("Unit electrical power", unit_generator_power, "W/(kg/s)"),
            _parameter("Target electrical power", TARGET_ELECTRICAL_POWER, "W"),
            _parameter("Heat pump COP", heat_pump_cop, "-"),
            _parameter("Cold reservoir heat", cold_reservoir_heat, "W"),
            _parameter("Heat pump electrical power", heat_pump_power, "W"),
        ],
        state_points=list(simulation.states.values()),
        connections=list(simulation.connections.values()),
        components=[
            _component(
                "Pump",
                input_ports=[str(pump.inlet_port.identifier)],
                output_ports=[str(pump.outlet_port.identifier)],
                input_states=[_state_identifier(pump.inlet_port.state)],
                output_states=[_state_identifier(pump.outlet_port.state)],
                power=pump_power,
            ),
            _component(
                "Evaporator",
                input_ports=[str(evaporator.inlet_port.identifier)],
                output_ports=[str(evaporator.outlet_port.identifier)],
                input_states=[_state_identifier(evaporator.inlet_port.state)],
                output_states=[_state_identifier(evaporator.outlet_port.state)],
                heat_flow=evaporator_heat,
            ),
            _component(
                "Turbine",
                input_ports=[str(turbine.inlet_port.identifier)],
                output_ports=[str(turbine.outlet_port.identifier)],
                input_states=[_state_identifier(turbine.inlet_port.state)],
                output_states=[_state_identifier(turbine.outlet_port.state)],
                power=turbine_power,
            ),
            _component(
                "Condenser",
                input_ports=[str(condenser.inlet_port.identifier)],
                output_ports=[str(condenser.outlet_port.identifier)],
                input_states=[_state_identifier(condenser.inlet_port.state)],
                output_states=[_state_identifier(condenser.outlet_port.state)],
                heat_flow=condenser_heat,
            ),
            _component(
                "PrescribedHeatPump",
                input_ports=[],
                output_ports=[],
                input_states=[],
                output_states=[],
                cold_reservoir_temperature=COLD_RESERVOIR_TEMPERATURE,
                cold_reservoir_heat_flow=cold_reservoir_heat,
                hot_heat_flow=evaporator_heat,
                electrical_power=heat_pump_power,
                cop=heat_pump_cop,
            ),
            _component(
                "Generator",
                input_ports=[],
                output_ports=[],
                input_states=[],
                output_states=[],
                mechanical_power=turbine_power,
                electrical_power=generator_power,
                loss=generator_loss,
            ),
        ],
        balances=[
            {
                "target": "cycle",
                "balance_type": "energy",
                "inputs": evaporator_heat + pump_power,
                "outputs": turbine_power + condenser_heat,
                "residual": evaporator_heat + pump_power - turbine_power - condenser_heat,
                "relative_error": abs(
                    evaporator_heat + pump_power - turbine_power - condenser_heat
                ) / evaporator_heat,
                "passed": True,
            },
            {
                "target": "prescribed_heat_pump",
                "balance_type": "energy",
                "inputs": cold_reservoir_heat + heat_pump_power,
                "outputs": evaporator_heat,
                "residual": cold_reservoir_heat + heat_pump_power - evaporator_heat,
                "relative_error": abs(
                    cold_reservoir_heat + heat_pump_power - evaporator_heat
                )
                / evaporator_heat,
                "passed": True,
            },
            {
                "target": "overall_plant",
                "balance_type": "energy",
                "inputs": overall_inputs,
                "outputs": overall_outputs,
                "residual": overall_residual,
                "relative_error": abs(overall_residual) / overall_inputs,
                "passed": abs(overall_residual) < 1.0e-6,
                "terms": {
                    "cold_reservoir_heat_W": cold_reservoir_heat,
                    "external_power_import_W": external_power_import,
                    "condenser_heat_W": condenser_heat,
                    "generator_loss_W": generator_loss,
                    "external_power_export_W": external_power_export,
                },
            }
        ],
        efficiencies=[
            {"name": "net_power", "value": net_power, "unit": "W"},
            {
                "name": "gross_thermal_efficiency",
                "value": generator_power / evaporator_heat,
                "unit": "-",
            },
            {
                "name": "net_system_efficiency_with_prescribed_cop",
                "value": net_power / evaporator_heat,
                "unit": "-",
            },
            {"name": HEAT_PUMP_POWER_NAME, "value": heat_pump_power, "unit": "W"},
            {"name": COLD_RESERVOIR_HEAT_NAME, "value": cold_reservoir_heat, "unit": "W"},
        ],
        validation=[
            _validation("positive_pump_power", pump_power > 0.0, pump_power, "W"),
            _validation("positive_turbine_power", turbine_power > 0.0, turbine_power, "W"),
            _validation("positive_evaporator_heat", evaporator_heat > 0.0, evaporator_heat, "W"),
            _validation("positive_condenser_heat", condenser_heat > 0.0, condenser_heat, "W"),
            _validation(
                "positive_cold_reservoir_heat",
                cold_reservoir_heat > 0.0,
                cold_reservoir_heat,
                "W",
            ),
            _validation(
                "gross_power_matches_target",
                abs(generator_power - TARGET_ELECTRICAL_POWER) < 1.0e-6,
                generator_power,
                "W",
            ),
            _validation(
                "heat_pump_energy_balance",
                abs(cold_reservoir_heat + heat_pump_power - evaporator_heat) < 1.0e-6,
                cold_reservoir_heat + heat_pump_power - evaporator_heat,
                "W",
            ),
        ],
        report={
            "summary": "Minimal saturated NH3 reference cycle calculated successfully.",
            "mass_flow_scaling": scaling_trace,
            "heat_pump_energy_balance": {
                "cold_reservoir_temperature_K": COLD_RESERVOIR_TEMPERATURE,
                "cold_reservoir_heat_W": cold_reservoir_heat,
                "electrical_power_W": heat_pump_power,
                "hot_heat_to_cycle_W": evaporator_heat,
                "cop_heating": heat_pump_cop,
            },
            "model_boundary": {
                "evaporator_inlet_state": "Rankine-cycle NH3 after feed pump",
                "heat_pump_cold_side": "Prescribed external source, not a material state point",
                "cold_reservoir": "Infinite 8 degC reservoir with fixed temperature",
                "calculation_mode": "Steady state; repeated cycles do not cool state points",
            },
        },
    )


def _calculate_cycle(mass_flow: float) -> dict[str, Any]:
    """
    Build and calculate the material cycle for one prescribed mass flow.
    """
    logger.debug("Calculating cycle for mass_flow_kg_per_s=%.9f", mass_flow)
    cycle = _build_cycle(mass_flow)
    _log_cycle_inputs(cycle)
    cycle["simulation"].calculate()
    _log_cycle_outputs(cycle)

    generator = Generator(
        identifier=Identifier("Generator", "shaft", "body"),
        mechanical_power=_required_float(TURBINE_POWER_NAME, cycle["turbine"].power),
        efficiency=GENERATOR_EFFICIENCY,
    )
    generator.calculate()
    cycle["generator"] = generator
    logger.debug(
        "Generator calculated: mechanical_power_W=%.6f, efficiency=%.6f, "
        "electrical_power_W=%.6f",
        _required_float(TURBINE_POWER_NAME, cycle["turbine"].power),
        GENERATOR_EFFICIENCY,
        _required_float(GENERATOR_ELECTRICAL_POWER_NAME, generator.electrical_power),
    )

    return cycle


def _scaled_mass_flow(unit_generator_power: float) -> float:
    if unit_generator_power <= 0.0:
        raise SimulationError("Unit generator electrical power must be positive.")

    return TARGET_ELECTRICAL_POWER / unit_generator_power


def _scaling_trace(unit_generator_power: float, mass_flow: float) -> dict[str, float]:
    return {
        "unit_mass_flow_kg_per_s": 1.0,
        "unit_generator_electrical_power_W": unit_generator_power,
        "target_electrical_power_W": TARGET_ELECTRICAL_POWER,
        "scaled_mass_flow_kg_per_s": mass_flow,
    }


def _build_cycle(mass_flow: float) -> dict[str, Any]:
    logger.debug("Building cycle objects for mass_flow_kg_per_s=%.9f", mass_flow)
    fluid = CoolPropFluid("NH3")
    simulation = Simulation("Minimal NH3 reference cycle")

    condenser_out = fluid.state_from_temperature_quality(
        identifier=Identifier("Condenser", "NH3", "out"),
        temperature=CONDENSATION_TEMPERATURE,
        vapor_quality=0.0,
        mass_flow=mass_flow,
    )
    evaporator_out_reference = fluid.state_from_temperature_quality(
        identifier=Identifier("Evaporator", "NH3", "out_reference"),
        temperature=EVAPORATION_TEMPERATURE,
        vapor_quality=1.0,
        mass_flow=mass_flow,
    )
    evaporation_pressure = _required_float(
        "evaporation pressure",
        evaporator_out_reference.pressure,
    )
    logger.debug(
        "Reference pressures: evaporation_pressure_Pa=%.6f, condensation_pressure_Pa=%.6f",
        evaporation_pressure,
        _required_float("condensation pressure", condenser_out.pressure),
    )
    _log_state("initial condenser outlet", condenser_out)

    pump = Pump(
        identifier=Identifier("Pump", "NH3", "body"),
        fluid=fluid,
        inlet_state=condenser_out,
        outlet_identifier=Identifier("Pump", "NH3", "out"),
        outlet_pressure=evaporation_pressure,
        isentropic_efficiency=PUMP_EFFICIENCY,
    )
    simulation.add_component(pump)

    evaporator = Evaporator(
        identifier=Identifier("Evaporator", "NH3", "body"),
        fluid=fluid,
        outlet_identifier=Identifier("Evaporator", "NH3", "out"),
        outlet_temperature=EVAPORATION_TEMPERATURE,
        outlet_vapor_quality=1.0,
    )
    simulation.add_component(evaporator)
    simulation.add_connection(
        Connection(
            identifier=Identifier("C01", "NH3", "connection"),
            source=pump.outlet_port,
            destination=evaporator.inlet_port,
        )
    )

    condensation_pressure = _required_float("condensation pressure", condenser_out.pressure)
    turbine = Turbine(
        identifier=Identifier("Turbine", "NH3", "body"),
        fluid=fluid,
        outlet_identifier=Identifier("Turbine", "NH3", "out"),
        outlet_pressure=condensation_pressure,
        isentropic_efficiency=TURBINE_EFFICIENCY,
    )
    simulation.add_component(turbine)
    simulation.add_connection(
        Connection(
            identifier=Identifier("C02", "NH3", "connection"),
            source=evaporator.outlet_port,
            destination=turbine.inlet_port,
        )
    )

    condenser = Condenser(
        identifier=Identifier("Condenser", "NH3", "body"),
        fluid=fluid,
        outlet_identifier=Identifier("Condenser", "NH3", "out"),
        outlet_temperature=CONDENSATION_TEMPERATURE,
        outlet_vapor_quality=0.0,
    )
    simulation.add_component(condenser)
    simulation.add_connection(
        Connection(
            identifier=Identifier("C03", "NH3", "connection"),
            source=turbine.outlet_port,
            destination=condenser.inlet_port,
        )
    )
    simulation.add_connection(
        Connection(
            identifier=Identifier("C04", "NH3", "connection"),
            source=condenser.outlet_port,
            destination=pump.inlet_port,
        )
    )
    simulation.add_state(condenser_out)
    logger.debug(
        "Cycle topology built: components=%d, connections=%d, states=%d",
        simulation.number_of_components(),
        simulation.number_of_connections(),
        simulation.number_of_states(),
    )

    return {
        "pump": pump,
        "evaporator": evaporator,
        "turbine": turbine,
        "condenser": condenser,
        "simulation": simulation,
    }


def _required_float(name: str, value: float | None) -> float:
    if value is None:
        raise SimulationError(f"Missing {name}.")

    return value


def _log_cycle_inputs(cycle: dict[str, Any]) -> None:
    logger.debug("Cycle input ports before Simulation.calculate()")
    for component_name in ("pump", "evaporator", "turbine", "condenser"):
        component = cycle[component_name]
        _log_port_state(f"{component_name}.inlet", component.inlet_port.state)


def _log_cycle_outputs(cycle: dict[str, Any]) -> None:
    logger.debug("Cycle ports after Simulation.calculate()")
    for component_name in ("pump", "evaporator", "turbine", "condenser"):
        component = cycle[component_name]
        _log_port_state(f"{component_name}.inlet", component.inlet_port.state)
        _log_port_state(f"{component_name}.outlet", component.outlet_port.state)

    logger.debug(
        "Component results: pump_power_W=%.6f, evaporator_heat_W=%.6f, "
        "turbine_power_W=%.6f, condenser_heat_W=%.6f",
        _required_float(PUMP_POWER_NAME, cycle["pump"].power),
        _required_float(EVAPORATOR_HEAT_NAME, cycle["evaporator"].heat_flow),
        _required_float(TURBINE_POWER_NAME, cycle["turbine"].power),
        _required_float(CONDENSER_HEAT_NAME, cycle["condenser"].heat_flow),
    )

    for connection in cycle["simulation"].connections.values():
        logger.debug(
            "Connection %s: %s -> %s, state=%s",
            connection.identifier,
            connection.source.identifier,
            connection.destination.identifier,
            _state_identifier(connection.state) if connection.state is not None else None,
        )


def _log_port_state(label: str, state: StatePoint | None) -> None:
    if state is None:
        logger.debug("State %-24s: <empty>", label)
        return

    _log_state(label, state)


def _log_state(label: str, state: StatePoint) -> None:
    logger.debug(
        "State %-24s: id=%s, p_Pa=%s, T_K=%s, h_J_per_kg=%s, "
        "s_J_per_kgK=%s, rho_kg_per_m3=%s, mdot_kg_per_s=%s, vapor_quality=%s",
        label,
        state.identifier,
        _format_optional_float(state.pressure),
        _format_optional_float(state.temperature),
        _format_optional_float(state.enthalpy),
        _format_optional_float(state.entropy),
        _format_optional_float(state.density),
        _format_optional_float(state.mass_flow),
        _format_optional_float(state.vapor_quality),
    )


def _format_optional_float(value: float | None) -> str:
    if value is None:
        return "None"

    return f"{value:.9g}"


def _state_identifier(state: StatePoint | None) -> str:
    if state is None:
        raise SimulationError("Missing connected state.")

    return str(state.identifier)


def _parameter(name: str, value: float, unit: str) -> dict[str, object]:
    return {
        "name": name,
        "symbol": "",
        "value": value,
        "unit": unit,
        "source": "reference_cycle.py",
    }


def _component(name: str, **values: object) -> dict[str, object]:
    return {
        "identifier": name,
        "type": name,
        "status": "calculated",
        **values,
    }


def _validation(name: str, passed: bool, value: float, unit: str) -> dict[str, object]:
    return {
        "name": name,
        "result": "passed" if passed else "failed",
        "message": f"{name} = {value:.6g} {unit}",
        "value": value,
        "limit": None,
    }


if __name__ == "__main__":
    main()
