"""
Simulation container.

The Simulation class represents one complete thermodynamic model.
It owns all components and all thermodynamic state points.
"""

from __future__ import annotations

from nh3powerplant.components.component import Component
from nh3powerplant.core.registry import Registry
from nh3powerplant.state.statepoint import StatePoint


class Simulation:
    """
    Container holding all objects of one simulation.
    """

    def __init__(self, name: str) -> None:
        """
        Parameters
        ----------
        name
            Human readable simulation name.
        """

        self._name = name

        self._components: Registry[Component] = Registry()
        self._states: Registry[StatePoint] = Registry()

    @property
    def name(self) -> str:
        """
        Simulation name.
        """
        return self._name

    @property
    def components(self) -> Registry[Component]:
        """
        Registry containing all components.
        """
        return self._components

    @property
    def states(self) -> Registry[StatePoint]:
        """
        Registry containing all thermodynamic state points.
        """
        return self._states

    def add_component(
        self,
        component: Component,
    ) -> None:
        """
        Add a component to the simulation.
        """
        self._components.add(component)

    def add_state(
        self,
        state: StatePoint,
    ) -> None:
        """
        Add a state point to the simulation.
        """
        self._states.add(state)

    def number_of_components(self) -> int:
        """
        Return the number of registered components.
        """
        return len(self._components)

    def number_of_states(self) -> int:
        """
        Return the number of registered state points.
        """
        return len(self._states)

    def clear(self) -> None:
        """
        Remove all components and all state points.
        """
        self._components.clear()
        self._states.clear()
