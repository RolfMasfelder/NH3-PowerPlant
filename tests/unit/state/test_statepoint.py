"""
Unit tests for StatePoint.
"""

from nh3powerplant.core.identifier import Identifier
from nh3powerplant.state.statepoint import StatePoint


def test_create_statepoint() -> None:

    state = StatePoint(

        identifier=Identifier(
            "Pump",
            "NH3",
            "out",
        )

    )

    assert state.identifier.component == "Pump"

    assert state.pressure is None

    assert state.temperature is None

    assert state.enthalpy is None

    assert state.entropy is None


def test_modify_statepoint() -> None:

    state = StatePoint(

        Identifier(
            "Pump",
            "NH3",
            "out",
        )

    )

    state.pressure = 12e5

    state.temperature = 95.0

    assert state.pressure == 12e5

    assert state.temperature == 95.0
