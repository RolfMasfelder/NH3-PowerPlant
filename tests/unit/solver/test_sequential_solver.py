"""
Unit tests for the SequentialSolver.
"""

from __future__ import annotations

from nh3powerplant.components.component import Component
from nh3powerplant.core.identifier import Identifier
from nh3powerplant.core.registry import Registry
from nh3powerplant.simulation.simulation import Simulation
from nh3powerplant.solver.sequential_solver import SequentialSolver


class DummyComponent(Component):
    """
    Dummy component used to verify solver execution.
    """

    def __init__(self, identifier: Identifier) -> None:
        super().__init__(identifier)
        self.executed = False

    def calculate(self) -> None:
        self.executed = True

    def execute(self) -> None:
        self.executed = True


def test_empty_simulation() -> None:
    """
    Solving an empty simulation shall not raise an exception.
    """

    simulation = Simulation("Unit Test")

    solver = SequentialSolver(simulation)

    solver.solve()

    assert simulation.number_of_components() == 0


def test_single_component() -> None:
    """
    The solver shall execute one component.
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

    solver = SequentialSolver(simulation)

    solver.solve()

    assert component.executed


def test_multiple_components() -> None:
    """
    The solver shall execute every registered component.
    """

    simulation = Simulation("Unit Test")

    components: Registry[DummyComponent] = Registry()

    for i in range(5):
        component = DummyComponent(
            Identifier(
                component=f"Component{i}",
                circuit="NH3",
                port="body",
            )
        )

        components.add(component)
        simulation.add_component(component)

    solver = SequentialSolver(simulation)

    solver.solve()

    assert all(component.executed for component in components)
