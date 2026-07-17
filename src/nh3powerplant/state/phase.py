"""
Enumeration of thermodynamic phases.
"""

from enum import Enum


class Phase(Enum):
    """Possible thermodynamic phases."""

    UNKNOWN = "unknown"

    LIQUID = "liquid"

    TWO_PHASE = "two_phase"

    VAPOR = "vapor"

    SUPERCRITICAL = "supercritical"
