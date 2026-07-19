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
    scaling_trace = result.report["mass_flow_scaling"]
    assert scaling_trace["target_electrical_power_W"] == module.TARGET_ELECTRICAL_POWER
    assert scaling_trace["scaled_mass_flow_kg_per_s"] == pytest.approx(
        module.TARGET_ELECTRICAL_POWER
        / scaling_trace["unit_generator_electrical_power_W"]
    )
    assert result.balances[0]["passed"] is True
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
