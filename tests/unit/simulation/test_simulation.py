"""
Unit tests for the Simulation class.
"""

from nh3powerplant.components.component import Component
from nh3powerplant.core.identifier import Identifier
from nh3powerplant.simulation.simulation import Simulation
from nh3powerplant.state.statepoint import StatePoint


class DummyComponent(Component):
    """
    Minimal concrete component used for testing.
    """

    def calculate(self) -> None:
        pass

    def execute(self) -> None:
        pass


def test_create_simulation() -> None:
    """
    A newly created simulation shall be empty.
    """

    simulation = Simulation("Unit Test")

    assert simulation.name == "Unit Test"

    assert simulation.number_of_components() == 0
    assert simulation.number_of_states() == 0


def test_add_component() -> None:
    """
    Components can be added to the simulation.
    """

    simulation = Simulation("Unit Test")

    component = DummyComponent(
        Identifier(
            component="Pump",
            circuit="NH3",
            port="body",
        )
    )

    simulation.add_component(component)

    assert simulation.number_of_components() == 1


def test_add_state() -> None:
    """
    State points can be added to the simulation.
    """

    simulation = Simulation("Unit Test")

    state = StatePoint(
        Identifier(
            component="Pump",
            circuit="NH3",
            port="out",
        )
    )

    simulation.add_state(state)

    assert simulation.number_of_states() == 1


def test_clear() -> None:
    """
    clear() removes all registered objects.
    """

    simulation = Simulation("Unit Test")

    simulation.add_component(
        DummyComponent(
            Identifier(
                "Pump",
                "NH3",
                "body",
            )
        )
    )

    simulation.add_state(
        StatePoint(
            Identifier(
                "Pump",
                "NH3",
                "out",
            )
        )
    )

    simulation.clear()

    assert simulation.number_of_components() == 0
    assert simulation.number_of_states() == 0


def test_component_registry() -> None:
    """
    Components are accessible through the registry.
    """

    simulation = Simulation("Unit Test")

    component = DummyComponent(
        Identifier(
            "Pump",
            "NH3",
            "body",
        )
    )

    simulation.add_component(component)

    assert simulation.components.get(component.identifier) is component


def test_state_registry() -> None:
    """
    State points are accessible through the registry.
    """

    simulation = Simulation("Unit Test")

    state = StatePoint(
        Identifier(
            "Pump",
            "NH3",
            "out",
        )
    )

    simulation.add_state(state)

    assert simulation.states.get(state.identifier) is state
