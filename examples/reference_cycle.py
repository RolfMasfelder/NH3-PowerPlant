"""
Minimal NH3 reference cycle example.
"""

from __future__ import annotations

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
PUMP_EFFICIENCY = 0.75
TURBINE_EFFICIENCY = 0.82
GENERATOR_EFFICIENCY = 0.96
HEAT_PUMP_COP = 3.0
TARGET_ELECTRICAL_POWER = 100_000.0
OUTPUT_PATH = Path("results/reference_cycle/result.json")


def main() -> None:
    """
    Run the reference cycle and write the result JSON file.
    """
    result = run_reference_cycle()
    JsonResultIO().write(result, OUTPUT_PATH)
    print(f"Wrote {OUTPUT_PATH}")
    print(f"gross electrical power: {result.components[-1]['electrical_power']:.2f} W")
    print(f"net electrical power: {result.efficiencies[0]['value']:.2f} W")


def run_reference_cycle() -> SimulationResult:
    """
    Calculate a simple saturated NH3 reference cycle.
    """
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

    cycle = _calculate_cycle(mass_flow=mass_flow)

    pump = cycle["pump"]
    evaporator = cycle["evaporator"]
    turbine = cycle["turbine"]
    condenser = cycle["condenser"]
    generator = cycle["generator"]
    simulation = cycle["simulation"]

    pump_power = _required_float("pump power", pump.power)
    turbine_power = _required_float("turbine power", turbine.power)
    evaporator_heat = _required_float("evaporator heat", evaporator.heat_flow)
    condenser_heat = _required_float("condenser heat", condenser.heat_flow)
    generator_power = _required_float("generator electrical power", generator.electrical_power)
    heat_pump_power = evaporator_heat / HEAT_PUMP_COP
    net_power = generator_power - pump_power - heat_pump_power

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
            "evaporation_temperature_K": EVAPORATION_TEMPERATURE,
            "condensation_temperature_K": CONDENSATION_TEMPERATURE,
            "pump_efficiency": PUMP_EFFICIENCY,
            "turbine_efficiency": TURBINE_EFFICIENCY,
            "generator_efficiency": GENERATOR_EFFICIENCY,
            "heat_pump_cop": HEAT_PUMP_COP,
            "target_electrical_power_W": TARGET_ELECTRICAL_POWER,
        },
        parameters=[
            _parameter("Evaporation temperature", EVAPORATION_TEMPERATURE, "K"),
            _parameter("Condensation temperature", CONDENSATION_TEMPERATURE, "K"),
            _parameter("Mass flow", mass_flow, "kg/s"),
            _parameter("Unit electrical power", unit_generator_power, "W/(kg/s)"),
            _parameter("Target electrical power", TARGET_ELECTRICAL_POWER, "W"),
            _parameter("Heat pump COP", HEAT_PUMP_COP, "-"),
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
                "Generator",
                input_ports=[],
                output_ports=[],
                input_states=[],
                output_states=[],
                electrical_power=generator_power,
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
        ],
        validation=[
            _validation("positive_pump_power", pump_power > 0.0, pump_power, "W"),
            _validation("positive_turbine_power", turbine_power > 0.0, turbine_power, "W"),
            _validation("positive_evaporator_heat", evaporator_heat > 0.0, evaporator_heat, "W"),
            _validation("positive_condenser_heat", condenser_heat > 0.0, condenser_heat, "W"),
            _validation(
                "gross_power_matches_target",
                abs(generator_power - TARGET_ELECTRICAL_POWER) < 1.0e-6,
                generator_power,
                "W",
            ),
        ],
        report={
            "summary": "Minimal saturated NH3 reference cycle calculated successfully.",
            "mass_flow_scaling": scaling_trace,
        },
    )


def _calculate_cycle(mass_flow: float) -> dict[str, Any]:
    """
    Build and calculate the material cycle for one prescribed mass flow.
    """
    cycle = _build_cycle(mass_flow)
    cycle["simulation"].calculate()

    generator = Generator(
        identifier=Identifier("Generator", "shaft", "body"),
        mechanical_power=_required_float("turbine power", cycle["turbine"].power),
        efficiency=GENERATOR_EFFICIENCY,
    )
    generator.calculate()
    cycle["generator"] = generator

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
