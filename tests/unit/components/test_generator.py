"""
Unit tests for the Generator component.
"""

from __future__ import annotations

import pytest

from nh3powerplant.components import Generator
from nh3powerplant.core.exceptions import ValidationError
from nh3powerplant.core.identifier import Identifier


def test_generator_calculates_electrical_power() -> None:
    """
    The generator shall convert mechanical power to electrical power.
    """

    generator = Generator(
        identifier=Identifier("Generator", "shaft", "body"),
        mechanical_power=100_000.0,
        efficiency=0.96,
    )

    generator.calculate()

    assert generator.electrical_power == pytest.approx(96_000.0)


def test_generator_rejects_invalid_efficiency() -> None:
    """
    The generator shall reject efficiencies outside the valid range.
    """

    with pytest.raises(ValidationError):
        Generator(
            identifier=Identifier("Generator", "shaft", "body"),
            mechanical_power=100_000.0,
            efficiency=0.0,
        )
