from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from nh3powerplant.core import Identifier


class Component(ABC):
    """
    Base class for all physical components.
    """

    def __init__(
        self,
        name: str,
    ) -> None:

        self.name = name

        self._ports: list[Identifier] = []

    @property
    def ports(self) -> tuple[Identifier, ...]:

        return tuple(self._ports)

    def add_port(
        self,
        identifier: Identifier,
    ) -> None:

        self._ports.append(identifier)

    @abstractmethod
    def calculate(self) -> None:
        """
        Calculates the component.
        """
