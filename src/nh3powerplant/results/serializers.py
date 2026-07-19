"""
Serializers for result objects.
"""

from __future__ import annotations

from nh3powerplant.state.statepoint import StatePoint


class ResultSerializer:
    """
    Convert domain objects into JSON-serializable dictionaries.
    """

    def state_point_to_dict(self, state_point: StatePoint) -> dict[str, object]:
        """
        Convert a state point to a dictionary.
        """
        return {
            "identifier": str(state_point.identifier),
            "fluid": state_point.fluid,
            "pressure": state_point.pressure,
            "temperature": state_point.temperature,
            "enthalpy": state_point.enthalpy,
            "entropy": state_point.entropy,
            "density": state_point.density,
            "mass_flow": state_point.mass_flow,
            "vapor_quality": state_point.vapor_quality,
        }
