"""
Structured simulation result.
"""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from typing import Any

from nh3powerplant.results.run_info import RunInfo
from nh3powerplant.state.statepoint import StatePoint


@dataclass(slots=True)
class SimulationResult:
    """
    Machine-readable result of one simulation run.
    """

    run: RunInfo
    configuration: dict[str, Any] = field(default_factory=dict)
    parameters: list[dict[str, Any]] = field(default_factory=list)
    state_points: list[StatePoint] = field(default_factory=list)
    components: list[dict[str, Any]] = field(default_factory=list)
    balances: list[dict[str, Any]] = field(default_factory=list)
    efficiencies: list[dict[str, Any]] = field(default_factory=list)
    validation: list[dict[str, Any]] = field(default_factory=list)
    figures: dict[str, str] = field(default_factory=dict)
    report: dict[str, Any] = field(default_factory=dict)

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
            "components": self.components,
            "balances": self.balances,
            "efficiencies": self.efficiencies,
            "validation": self.validation,
            "figures": self.figures,
            "report": self.report,
        }
