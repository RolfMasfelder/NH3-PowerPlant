"""
Simple sequential solver.
"""

from __future__ import annotations

from .solver import Solver


class SequentialSolver(Solver):
    """
    Executes all components sequentially.
    """

    def solve(self) -> None:
        """
        Calculate every component exactly once.
        """

        for component in self.simulation.components:
            component.calculate()
