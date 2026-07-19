"""
Metadata for one simulation run.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from datetime import timezone


@dataclass(slots=True, frozen=True)
class RunInfo:
    """
    Metadata describing one simulation run.
    """

    id: str
    simulation_name: str
    variant: str
    description: str
    project_version: str
    timestamp: str

    @classmethod
    def create(
        cls,
        id: str,
        simulation_name: str,
        variant: str,
        description: str,
        project_version: str,
    ) -> RunInfo:
        """
        Create run metadata with the current UTC timestamp.
        """
        return cls(
            id=id,
            simulation_name=simulation_name,
            variant=variant,
            description=description,
            project_version=project_version,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )

    def to_dict(self) -> dict[str, str]:
        """
        Return a JSON-serializable representation.
        """
        return {
            "id": self.id,
            "timestamp": self.timestamp,
            "project_version": self.project_version,
            "simulation_name": self.simulation_name,
            "variant": self.variant,
            "description": self.description,
        }
