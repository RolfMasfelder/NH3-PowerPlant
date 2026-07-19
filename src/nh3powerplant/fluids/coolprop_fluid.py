"""
CoolProp based thermodynamic fluid.
"""

from __future__ import annotations

from CoolProp.CoolProp import PropsSI

from nh3powerplant.core.exceptions import ValidationError
from nh3powerplant.core.identifier import Identifier
from nh3powerplant.fluids.fluid import Fluid
from nh3powerplant.state.statepoint import StatePoint


class CoolPropFluid(Fluid):
    """
    Thermodynamic fluid backed by CoolProp.
    """

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
        self._validate_positive("pressure", pressure)
        self._validate_positive("temperature", temperature)

        enthalpy = self._property("Hmass", "P", pressure, "T", temperature)
        entropy = self._property("Smass", "P", pressure, "T", temperature)
        density = self._property("Dmass", "P", pressure, "T", temperature)
        vapor_quality = self._vapor_quality("P", pressure, "T", temperature)

        return StatePoint(
            identifier=identifier,
            pressure=pressure,
            temperature=temperature,
            enthalpy=enthalpy,
            entropy=entropy,
            density=density,
            mass_flow=mass_flow,
            vapor_quality=vapor_quality,
            fluid=self.name,
        )

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
        self._validate_positive("pressure", pressure)

        temperature = self._property("T", "P", pressure, "Hmass", enthalpy)
        entropy = self._property("Smass", "P", pressure, "Hmass", enthalpy)
        density = self._property("Dmass", "P", pressure, "Hmass", enthalpy)
        vapor_quality = self._vapor_quality("P", pressure, "Hmass", enthalpy)

        return StatePoint(
            identifier=identifier,
            pressure=pressure,
            temperature=temperature,
            enthalpy=enthalpy,
            entropy=entropy,
            density=density,
            mass_flow=mass_flow,
            vapor_quality=vapor_quality,
            fluid=self.name,
        )

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
        self._validate_positive("pressure", pressure)

        temperature = self._property("T", "P", pressure, "Smass", entropy)
        enthalpy = self._property("Hmass", "P", pressure, "Smass", entropy)
        density = self._property("Dmass", "P", pressure, "Smass", entropy)
        vapor_quality = self._vapor_quality("P", pressure, "Smass", entropy)

        return StatePoint(
            identifier=identifier,
            pressure=pressure,
            temperature=temperature,
            enthalpy=enthalpy,
            entropy=entropy,
            density=density,
            mass_flow=mass_flow,
            vapor_quality=vapor_quality,
            fluid=self.name,
        )

    def _property(
        self,
        output: str,
        input_1: str,
        value_1: float,
        input_2: str,
        value_2: float,
    ) -> float:
        try:
            return float(PropsSI(output, input_1, value_1, input_2, value_2, self.name))
        except ValueError as exc:
            raise ValidationError(
                f"Cannot calculate {output} for fluid '{self.name}'."
            ) from exc

    def _vapor_quality(
        self,
        input_1: str,
        value_1: float,
        input_2: str,
        value_2: float,
    ) -> float | None:
        try:
            quality = self._property("Q", input_1, value_1, input_2, value_2)
        except ValidationError:
            return None

        if 0.0 <= quality <= 1.0:
            return quality

        return None

    def _validate_positive(self, name: str, value: float) -> None:
        if value <= 0.0:
            raise ValidationError(f"{name} must be positive")
