"""
Unit tests for the Simulation class.
"""

from nh3powerplant.connection.connection import Connection
from nh3powerplant.components.component import Component
from nh3powerplant.core.identifier import Identifier
from nh3powerplant.core.port import Port
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


class IncrementComponent(Component):
    """
    Component used to test state propagation through connections.
    """

    def __init__(self, identifier: Identifier, inlet_state: StatePoint, increment: float) -> None:
        super().__init__(identifier)
        self._increment = increment
        self.calculation_count = 0
        self.inlet_port = Port(
            Identifier(identifier.component, identifier.circuit, "in"),
            state=inlet_state,
        )
        self.outlet_port = Port(
            Identifier(identifier.component, identifier.circuit, "out"),
        )

    def calculate(self) -> None:
        self.calculation_count += 1
        inlet_state = self.inlet_port.state

        if inlet_state is None or inlet_state.temperature is None:
            raise AssertionError("component requires inlet temperature")

        self.outlet_port.state = StatePoint(
            identifier=self.outlet_port.identifier,
            temperature=inlet_state.temperature + self._increment,
        )

    def execute(self) -> None:
        self.calculate()


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


def test_calculate_transfers_states_through_feedback_loop() -> None:
    """
    calculate() shall execute components once and transfer states along connections.
    """

    simulation = Simulation("Unit Test")
    initial_state = StatePoint(
        Identifier("A", "NH3", "in"),
        temperature=0.0,
    )
    component_a = IncrementComponent(
        Identifier("A", "NH3", "body"),
        inlet_state=initial_state,
        increment=1.0,
    )
    component_b = IncrementComponent(
        Identifier("B", "NH3", "body"),
        inlet_state=initial_state,
        increment=10.0,
    )
    simulation.add_component(component_a)
    simulation.add_component(component_b)
    simulation.add_state(initial_state)
    simulation.add_connection(
        Connection(
            Identifier("C01", "NH3", "connection"),
            source=component_a.outlet_port,
            destination=component_b.inlet_port,
        )
    )
    simulation.add_connection(
        Connection(
            Identifier("C02", "NH3", "connection"),
            source=component_b.outlet_port,
            destination=component_a.inlet_port,
        )
    )

    simulation.calculate()
    simulation.calculate()

    assert component_a.inlet_port.state is not None
    assert component_a.inlet_port.state.temperature == 22.0
    assert component_b.inlet_port.state is not None
    assert component_b.inlet_port.state.temperature == 12.0
    assert component_a.calculation_count == 2
    assert component_b.calculation_count == 2
