"""
Generator component model.
"""

from __future__ import annotations

import logging

from nh3powerplant.components.component import Component
from nh3powerplant.core.exceptions import ValidationError
from nh3powerplant.core.identifier import Identifier


logger = logging.getLogger(__name__)


class Generator(Component):
    """
    Generator with a prescribed mechanical-to-electrical efficiency.
    """

    def __init__(
        self,
        identifier: Identifier,
        mechanical_power: float,
        efficiency: float,
    ) -> None:
        """
        Parameters
        ----------
        identifier
            Unique component identifier.
        mechanical_power
            Mechanical input power in W.
        efficiency
            Generator efficiency.
        """
        super().__init__(identifier)

        if mechanical_power < 0.0:
            raise ValidationError("mechanical power must not be negative")

        if not 0.0 < efficiency <= 1.0:
            raise ValidationError("generator efficiency must be in (0, 1]")

        self._mechanical_power = mechanical_power
        self._efficiency = efficiency
        self._electrical_power: float | None = None

    @property
    def electrical_power(self) -> float | None:
        """
        Return the electrical output power in W.
        """
        return self._electrical_power

    def calculate(self) -> None:
        """
        Calculate electrical output power.
        """
        self._electrical_power = self._mechanical_power * self._efficiency
        logger.debug(
            "Generator output: id=%s, mechanical_power_W=%.6f, efficiency=%.6f, electrical_power_W=%.6f",
            self.identifier,
            self._mechanical_power,
            self._efficiency,
            self._electrical_power,
        )

    def execute(self) -> None:
        """
        Execute the generator calculation.
        """
        self.calculate()
