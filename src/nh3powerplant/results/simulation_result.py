"""
Structured simulation result.
"""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from typing import Any

from nh3powerplant.connection.connection import Connection
from nh3powerplant.results.run_info import RunInfo
from nh3powerplant.state.statepoint import StatePoint


def _empty_mapping() -> dict[str, Any]:
    return {}


def _empty_entries() -> list[dict[str, Any]]:
    return []


def _empty_state_points() -> list[StatePoint]:
    return []


def _empty_connections() -> list[Connection]:
    return []


def _empty_figures() -> dict[str, str]:
    return {}


@dataclass(slots=True)
class SimulationResult:
    """
    Machine-readable result of one simulation run.
    """

    run: RunInfo
    configuration: dict[str, Any] = field(default_factory=_empty_mapping)
    parameters: list[dict[str, Any]] = field(default_factory=_empty_entries)
    state_points: list[StatePoint] = field(default_factory=_empty_state_points)
    connections: list[Connection] = field(default_factory=_empty_connections)
    components: list[dict[str, Any]] = field(default_factory=_empty_entries)
    balances: list[dict[str, Any]] = field(default_factory=_empty_entries)
    efficiencies: list[dict[str, Any]] = field(default_factory=_empty_entries)
    validation: list[dict[str, Any]] = field(default_factory=_empty_entries)
    figures: dict[str, str] = field(default_factory=_empty_figures)
    report: dict[str, Any] = field(default_factory=_empty_mapping)

    def to_dict(self) -> dict[str, Any]:
        """
        Return a JSON-serializable representation.
        """
        from nh3powerplant.results.serializers import ResultSerializer

        serializer = ResultSerializer()

        return {
            "run": self.run.to_dict(),
            "configuration": self.configuration,
            "parameters": self.parameters,
            "state_points": [
                serializer.state_point_to_dict(state_point)
                for state_point in self.state_points
            ],
            "connections": [
                serializer.connection_to_dict(connection)
                for connection in self.connections
            ],
            "components": self.components,
            "balances": self.balances,
            "efficiencies": self.efficiencies,
            "validation": self.validation,
            "figures": self.figures,
            "report": self.report,
        }
