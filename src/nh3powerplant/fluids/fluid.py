"""
Base class for thermodynamic fluids.
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from nh3powerplant.core.exceptions import ValidationError
from nh3powerplant.core.identifier import Identifier
from nh3powerplant.state.statepoint import StatePoint


class Fluid(ABC):
    """
    Abstract base class for thermodynamic fluid property providers.
    """

    def __init__(self, name: str) -> None:
        """
        Parameters
        ----------
        name
            Name of the fluid in the backing property database.
        """
        if not name.strip():
            raise ValidationError("fluid name must not be empty")

        self._name = name

    @property
    def name(self) -> str:
        """
        Return the fluid name.
        """
        return self._name

    @abstractmethod
    def state_from_pressure_temperature(
        self,
        identifier: Identifier,
        pressure: float,
        temperature: float,
        mass_flow: float | None = None,
    ) -> StatePoint:
        """
        Create a state point from pressure and temperature.
        """
        raise NotImplementedError

    @abstractmethod
    def state_from_pressure_enthalpy(
        self,
        identifier: Identifier,
        pressure: float,
        enthalpy: float,
        mass_flow: float | None = None,
    ) -> StatePoint:
        """
        Create a state point from pressure and specific enthalpy.
        """
        raise NotImplementedError

    @abstractmethod
    def state_from_pressure_entropy(
        self,
        identifier: Identifier,
        pressure: float,
        entropy: float,
        mass_flow: float | None = None,
    ) -> StatePoint:
        """
        Create a state point from pressure and specific entropy.
        """
        raise NotImplementedError

    @abstractmethod
    def state_from_temperature_quality(
        self,
        identifier: Identifier,
        temperature: float,
        vapor_quality: float,
        mass_flow: float | None = None,
    ) -> StatePoint:
        """
        Create a saturated state point from temperature and vapor quality.
        """
        raise NotImplementedError
