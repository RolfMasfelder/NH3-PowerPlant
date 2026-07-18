"""
Unit tests for Connection.
"""

from nh3powerplant.connection.connection import Connection
from nh3powerplant.core.identifier import Identifier
from nh3powerplant.state.statepoint import StatePoint


def test_create_connection() -> None:
    """
    Create a connection.
    """

    state = StatePoint(
        Identifier(
            "Connection",
            "NH3",
            "State",
        )
    )

    connection = Connection(
        identifier=Identifier(
            "C01",
            "NH3",
            "connection",
        ),
        source=Identifier(
            "HeatPump",
            "NH3",
            "out",
        ),
        destination=Identifier(
            "Evaporator",
            "NH3",
            "in",
        ),
        state=state,
    )

    assert connection.identifier.component == "C01"

    assert connection.source.component == "HeatPump"

    assert connection.destination.component == "Evaporator"

    assert connection.state is state


def test_connection_name() -> None:
    """
    Name property.
    """

    state = StatePoint(
        Identifier(
            "Connection",
            "NH3",
            "State",
        )
    )

    connection = Connection(
        identifier=Identifier(
            "C01",
            "NH3",
            "connection",
        ),
        source=Identifier(
            "A",
            "NH3",
            "out",
        ),
        destination=Identifier(
            "B",
            "NH3",
            "in",
        ),
        state=state,
    )

    assert connection.name == "C01.NH3.connection"
