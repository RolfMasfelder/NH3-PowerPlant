"""
Pump component model.
"""

from __future__ import annotations

from nh3powerplant.components.component import Component
from nh3powerplant.core.exceptions import ValidationError
from nh3powerplant.core.identifier import Identifier
from nh3powerplant.fluids.fluid import Fluid
from nh3powerplant.state.statepoint import StatePoint


class Pump(Component):
    """
    Incompressible pump model.
    """

    def __init__(
        self,
        identifier: Identifier,
        fluid: Fluid,
        inlet_state: StatePoint,
        outlet_identifier: Identifier,
        outlet_pressure: float,
        isentropic_efficiency: float,
    ) -> None:
        """
        Parameters
        ----------
        identifier
            Unique component identifier.
        fluid
            Fluid property provider.
        inlet_state
            Thermodynamic state at the pump inlet.
        outlet_identifier
            Identifier of the generated outlet state.
        outlet_pressure
            Pump outlet pressure in Pa.
        isentropic_efficiency
            Pump isentropic efficiency.
        """
        super().__init__(identifier)

        if outlet_pressure <= 0.0:
            raise ValidationError("outlet pressure must be positive")

        if not 0.0 < isentropic_efficiency <= 1.0:
            raise ValidationError("isentropic efficiency must be in (0, 1]")

        self._fluid = fluid
        self._inlet_state = inlet_state
        self._outlet_identifier = outlet_identifier
        self._outlet_pressure = outlet_pressure
        self._isentropic_efficiency = isentropic_efficiency
        self._outlet_state: StatePoint | None = None
        self._power: float | None = None

    @property
    def outlet_state(self) -> StatePoint | None:
        """
        Return the calculated outlet state.
        """
        return self._outlet_state

    @property
    def power(self) -> float | None:
        """
        Return the pump shaft power in W.
        """
        return self._power

    def calculate(self) -> None:
        """
        Calculate outlet state and pump power.
        """
        inlet_pressure = self._required("pressure", self._inlet_state.pressure)
        inlet_enthalpy = self._required("enthalpy", self._inlet_state.enthalpy)
        inlet_density = self._required("density", self._inlet_state.density)
        mass_flow = self._required("mass_flow", self._inlet_state.mass_flow)

        if self._outlet_pressure <= inlet_pressure:
            raise ValidationError("outlet pressure must exceed inlet pressure")

        pressure_increase = self._outlet_pressure - inlet_pressure
        specific_work = pressure_increase / inlet_density / self._isentropic_efficiency
        outlet_enthalpy = inlet_enthalpy + specific_work

        self._outlet_state = self._fluid.state_from_pressure_enthalpy(
            identifier=self._outlet_identifier,
            pressure=self._outlet_pressure,
            enthalpy=outlet_enthalpy,
            mass_flow=mass_flow,
        )
        self._power = mass_flow * specific_work

    def execute(self) -> None:
        """
        Execute the pump calculation.
        """
        self.calculate()

    def _required(self, name: str, value: float | None) -> float:
        if value is None:
            raise ValidationError(f"inlet state requires {name}")

        return value
