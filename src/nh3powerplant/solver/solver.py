"""
Abstract solver interface.
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from nh3powerplant.simulation.simulation import Simulation


class Solver(ABC):
    """
    Base class for all simulation solvers.
    """

    def __init__(
        self,
        simulation: Simulation,
    ) -> None:
        """
        Parameters
        ----------
        simulation
            Simulation model to be solved.
        """
        self._simulation = simulation

    @property
    def simulation(self) -> Simulation:
        """
        Return the associated simulation.
        """
        return self._simulation

    @abstractmethod
    def solve(self) -> None:
        """
        Execute the simulation.
        """
        raise NotImplementedError
