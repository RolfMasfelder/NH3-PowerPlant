"""
Unit tests for simulation results.
"""

from __future__ import annotations

from nh3powerplant.core.identifier import Identifier
from nh3powerplant.results import RunInfo
from nh3powerplant.results import SimulationResult
from nh3powerplant.state.statepoint import StatePoint


def test_simulation_result_to_dict() -> None:
    """
    Simulation results shall expose the documented top-level structure.
    """

    result = SimulationResult(
        run=RunInfo(
            id="reference-a",
            timestamp="2026-07-19T00:00:00+00:00",
            project_version="0.1.0",
            simulation_name="Reference model",
            variant="A",
            description="Reference run",
        ),
        configuration={"fluid": "NH3"},
        parameters=[{"name": "Generatorleistung", "value": 100.0, "unit": "kW"}],
        state_points=[
            StatePoint(
                identifier=Identifier("Pump", "NH3", "in"),
                pressure=500_000.0,
                temperature=250.0,
                fluid="NH3",
            )
        ],
    )

    data = result.to_dict()

    assert set(data) == {
        "run",
        "configuration",
        "parameters",
        "state_points",
        "connections",
        "components",
        "balances",
        "efficiencies",
        "validation",
        "figures",
        "report",
    }
    assert data["run"]["id"] == "reference-a"
    assert data["state_points"][0]["identifier"] == "Pump.NH3.in"
