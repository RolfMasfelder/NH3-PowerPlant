"""
Thermodynamic state point.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from nh3powerplant.core.provenance import Provenance

from .phase import Phase


@dataclass(slots=True)
class StatePoint:
    """
    Represents one thermodynamic state.

    Units:

        temperature : K
        pressure    : Pa
        enthalpy    : J/kg
        entropy     : J/(kg K)
        density     : kg/m³
        quality     : -

    """

    name: str

    temperature: float | None = None

    pressure: float | None = None

    enthalpy: float | None = None

    entropy: float | None = None

    density: float | None = None

    quality: float | None = None

    phase: Phase = Phase.UNKNOWN

    provenance: Provenance | None = None

    def is_complete(self) -> bool:
        """
        Returns True if all primary thermodynamic properties exist.
        """

        return (
            self.temperature is not None
            and self.pressure is not None
            and self.enthalpy is not None
            and self.entropy is not None
        )

    def to_dict(self) -> dict[str, Any]:

        return {
            "name": self.name,
            "temperature": self.temperature,
            "pressure": self.pressure,
            "enthalpy": self.enthalpy,
            "entropy": self.entropy,
            "density": self.density,
            "quality": self.quality,
            "phase": self.phase.value,
            "provenance": self.provenance,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "StatePoint":

        obj = cls(name=data["name"])

        obj.temperature = data.get("temperature")

        obj.pressure = data.get("pressure")

        obj.enthalpy = data.get("enthalpy")

        obj.entropy = data.get("entropy")

        obj.density = data.get("density")

        obj.quality = data.get("quality")

        obj.phase = Phase(data.get("phase", "unknown"))

        obj.provenance = data.get("provenance")

        return obj
