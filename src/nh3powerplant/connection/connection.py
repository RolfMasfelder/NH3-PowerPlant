"""
Connection between two simulation components.
"""

from __future__ import annotations

from dataclasses import dataclass

from nh3powerplant.core.identifier import Identifier
from nh3powerplant.state.statepoint import StatePoint


@dataclass(slots=True)
class Connection:
    """
    Represents one material connection between two components.

    A connection transports exactly one thermodynamic state.
    """

    identifier: Identifier

    source: Identifier

    destination: Identifier

    state: StatePoint

    @property
    def name(self) -> str:
        """
        Human readable connection name.
        """
        return str(self.identifier)
