"""
Unit tests for the Component base class.
"""

from nh3powerplant.components.component import Component
from nh3powerplant.core.identifier import Identifier


class DummyComponent(Component):

    def calculate(self) -> None:
        pass


def test_identifier() -> None:

    component = DummyComponent(
        Identifier("Pump", "NH3", "body")
    )

    assert component.identifier == Identifier(
        "Pump",
        "NH3",
        "body",
    )


def test_name() -> None:

    component = DummyComponent(
        Identifier("HeatPump", "NH3", "body")
    )

    assert component.name == "HeatPump"
