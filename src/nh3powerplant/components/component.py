"""
Abstract base class for all simulation components.
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from nh3powerplant.core.identifier import Identifier


class Component(ABC):
    """
    Abstract base class for all physical components.
    """

    def __init__(
        self,
        identifier: Identifier,
    ) -> None:
        """
        Parameters
        ----------
        identifier
            Unique identifier of the component.
        """
        self._identifier = identifier

    @property
    def identifier(self) -> Identifier:
        """
        Return the unique identifier.
        """
        return self._identifier

    @property
    def name(self) -> str:
        """
        Return the component name.
        """
        return self.identifier.component

    @abstractmethod
    def calculate(self) -> None:
        """
        Perform the component calculation.
        """
        raise NotImplementedError
