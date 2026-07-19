"""
Simulation container.

The Simulation class represents one complete thermodynamic model.
It owns all components and all thermodynamic state points.
"""

from __future__ import annotations

from nh3powerplant.connection.connection import Connection
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
        self._connections: Registry[Connection] = Registry()
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

    @property
    def connections(self) -> Registry[Connection]:
        """
        Registry containing all connections.
        """
        return self._connections

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

    def add_connection(
        self,
        connection: Connection,
    ) -> None:
        """
        Add a connection to the simulation.
        """
        self._connections.add(connection)

    def number_of_components(self) -> int:
        """
        Return the number of registered components.
        """
        return len(self._components)

    def number_of_connections(self) -> int:
        """
        Return the number of registered connections.
        """
        return len(self._connections)

    def number_of_states(self) -> int:
        """
        Return the number of registered state points.
        """
        return len(self._states)

    def clear(self) -> None:
        """
        Remove all components, all connections, and all state points.
        """
        self._components.clear()
        self._connections.clear()
        self._states.clear()
