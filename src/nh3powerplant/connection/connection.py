"""
Connection between two simulation components.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass

from nh3powerplant.core.exceptions import ValidationError
from nh3powerplant.core.identifier import Identifier
from nh3powerplant.core.port import Port
from nh3powerplant.state.statepoint import StatePoint


logger = logging.getLogger(__name__)


@dataclass(slots=True)
class Connection:
    """
    Represents one material connection between two components.

    A connection transports exactly one thermodynamic state.
    """

    identifier: Identifier

    source: Port

    destination: Port

    state: StatePoint | None = None

    def __post_init__(self) -> None:
        """
        Initialize the transported state and destination port.
        """
        if self.state is not None or self.source.state is not None:
            self.transfer()

    @property
    def name(self) -> str:
        """
        Human readable connection name.
        """
        return str(self.identifier)

    def transfer(self) -> StatePoint:
        """
        Transfer the connection state from source port to destination port.
        """
        source_state = self.source.state

        if source_state is None and self.state is None:
            raise ValidationError("connection requires a state")

        if source_state is not None:
            self.state = source_state

        self.source.state = self.state
        self.destination.state = self.state

        if self.state is None:
            raise ValidationError("connection requires a state")

        logger.debug(
            "Connection transfer: %s, %s -> %s, state=%s",
            self.identifier,
            self.source.identifier,
            self.destination.identifier,
            self.state.identifier,
        )

        return self.state
