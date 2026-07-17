"""
Thermodynamic state point.
"""

from __future__ import annotations

from dataclasses import dataclass

from nh3powerplant.core.identifier import Identifier


@dataclass(slots=True)
class StatePoint:
    """
    Thermodynamic state of a fluid stream.

    All quantities use SI units.

    Unknown values are represented by None.
    """

    identifier: Identifier

    pressure: float | None = None
    temperature: float | None = None

    enthalpy: float | None = None
    entropy: float | None = None

    density: float | None = None

    mass_flow: float | None = None

    vapor_quality: float | None = None

    fluid: str | None = None
