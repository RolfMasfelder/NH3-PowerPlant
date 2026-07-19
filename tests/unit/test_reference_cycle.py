"""
Unit tests for the reference cycle example.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path
from types import ModuleType

import pytest

from nh3powerplant.results import SimulationResult


def _load_reference_cycle() -> ModuleType:
    path = Path(__file__).parents[2] / "examples" / "reference_cycle.py"
    spec = importlib.util.spec_from_file_location("reference_cycle", path)

    if spec is None or spec.loader is None:
        raise RuntimeError("Cannot load reference_cycle.py")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_reference_cycle_produces_result() -> None:
    """
    The reference cycle shall produce a structured simulation result.
    """

    module = _load_reference_cycle()
    result = module.run_reference_cycle()

    assert isinstance(result, SimulationResult)
    assert result.run.id == "reference-cycle"
    assert len(result.state_points) == 4
    assert len(result.connections) == 4
    assert str(result.connections[0].source.identifier) == "Pump.NH3.out"
    assert str(result.connections[0].destination.identifier) == "Evaporator.NH3.in"
    assert result.components[0]["input_ports"] == ["Pump.NH3.in"]
    assert result.components[0]["output_ports"] == ["Pump.NH3.out"]
    assert result.components[0]["input_states"] == ["Condenser.NH3.out"]
    assert result.components[0]["output_states"] == ["Pump.NH3.out"]
    assert result.components[-1]["electrical_power"] == pytest.approx(
        module.TARGET_ELECTRICAL_POWER
    )
    heat_pump = result.components[-2]
    assert heat_pump["identifier"] == "PrescribedHeatPump"
    assert heat_pump["cold_reservoir_temperature"] == module.COLD_RESERVOIR_TEMPERATURE
    assert heat_pump["hot_heat_flow"] == pytest.approx(
        heat_pump["cold_reservoir_heat_flow"] + heat_pump["electrical_power"]
    )
    scaling_trace = result.report["mass_flow_scaling"]
    assert scaling_trace["target_electrical_power_W"] == module.TARGET_ELECTRICAL_POWER
    assert scaling_trace["scaled_mass_flow_kg_per_s"] == pytest.approx(
        module.TARGET_ELECTRICAL_POWER
        / scaling_trace["unit_generator_electrical_power_W"]
    )
    heat_pump_balance = result.report["heat_pump_energy_balance"]
    assert heat_pump_balance["cold_reservoir_temperature_K"] == (
        module.COLD_RESERVOIR_TEMPERATURE
    )
    assert heat_pump_balance["cold_reservoir_heat_W"] > 0.0
    assert heat_pump_balance["hot_heat_to_cycle_W"] == pytest.approx(
        heat_pump_balance["cold_reservoir_heat_W"]
        + heat_pump_balance["electrical_power_W"]
    )
    assert result.balances[0]["passed"] is True
    assert result.balances[1]["target"] == "prescribed_heat_pump"
    assert result.balances[1]["passed"] is True
    assert result.balances[2]["target"] == "overall_plant"
    assert result.balances[2]["passed"] is True
    overall_terms = result.balances[2]["terms"]
    assert overall_terms["cold_reservoir_heat_W"] == pytest.approx(
        heat_pump_balance["cold_reservoir_heat_W"]
    )
    assert overall_terms["external_power_import_W"] > 0.0
    assert overall_terms["external_power_export_W"] == 0.0
    assert result.report["model_boundary"]["evaporator_inlet_state"] == (
        "Rankine-cycle NH3 after feed pump"
    )
    assert all(check["result"] == "passed" for check in result.validation)


def test_reference_cycle_defines_empty_downstream_inlets_before_calculation() -> None:
    """
    Downstream component inlets shall receive their states through connections.
    """

    module = _load_reference_cycle()
    cycle = module._build_cycle(mass_flow=1.0)

    assert cycle["pump"].inlet_port.state is not None
    assert cycle["evaporator"].inlet_port.state is None
    assert cycle["turbine"].inlet_port.state is None
    assert cycle["condenser"].inlet_port.state is None

    cycle["simulation"].calculate()

    assert cycle["evaporator"].inlet_port.state is cycle["pump"].outlet_port.state
    assert cycle["turbine"].inlet_port.state is cycle["evaporator"].outlet_port.state
    assert cycle["condenser"].inlet_port.state is cycle["turbine"].outlet_port.state


def test_reference_cycle_accepts_heat_pump_cop_variant() -> None:
    """
    The prescribed heat pump COP shall be configurable for sensitivity studies.
    """

    module = _load_reference_cycle()
    result = module.run_reference_cycle(heat_pump_cop=4.0)

    heat_pump = result.components[-2]
    heat_pump_balance = result.report["heat_pump_energy_balance"]

    assert result.configuration["heat_pump_cop"] == 4.0
    assert heat_pump["cop"] == 4.0
    assert heat_pump_balance["cop_heating"] == 4.0
    assert heat_pump_balance["electrical_power_W"] == pytest.approx(
        heat_pump_balance["hot_heat_to_cycle_W"] / 4.0
    )


def test_reference_cycle_rejects_invalid_heat_pump_cop() -> None:
    """
    A heating COP must be greater than one for this prescribed heat pump model.
    """

    module = _load_reference_cycle()

    with pytest.raises(ValueError, match="heat_pump_cop must be greater than 1.0"):
        module.run_reference_cycle(heat_pump_cop=1.0)
