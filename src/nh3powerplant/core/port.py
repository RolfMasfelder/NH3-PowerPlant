"""
Connection points of simulation components.
"""

from __future__ import annotations

from dataclasses import dataclass

from nh3powerplant.core import Identifier
from nh3powerplant.state.statepoint import StatePoint


@dataclass(slots=True)
class Port:
    """
    Connection point of a component.
    """

    identifier: Identifier

    description: str = ""

    state: StatePoint | None = None

    @property
    def name(self) -> str:
        """
        Human readable port name.
        """
        return str(self.identifier)
