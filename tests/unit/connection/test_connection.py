"""
Unit tests for Connection.
"""

from nh3powerplant.connection.connection import Connection
from nh3powerplant.core.identifier import Identifier
from nh3powerplant.core.port import Port
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
        source=Port(Identifier("HeatPump", "NH3", "out")),
        destination=Port(Identifier("Evaporator", "NH3", "in")),
        state=state,
    )

    assert connection.identifier.component == "C01"

    assert connection.source.identifier.component == "HeatPump"

    assert connection.destination.identifier.component == "Evaporator"

    assert connection.state is state
    assert connection.source.state is state
    assert connection.destination.state is state


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
        source=Port(Identifier("A", "NH3", "out")),
        destination=Port(Identifier("B", "NH3", "in")),
        state=state,
    )

    assert connection.name == "C01.NH3.connection"


def test_connection_can_be_created_before_source_state_exists() -> None:
    """
    Connections can be created before the source component has calculated.
    """

    source = Port(Identifier("A", "NH3", "out"))
    destination = Port(Identifier("B", "NH3", "in"))

    connection = Connection(
        identifier=Identifier("C01", "NH3", "connection"),
        source=source,
        destination=destination,
    )

    assert connection.state is None
    assert destination.state is None
