"""
Pump component model.
"""

from __future__ import annotations

import logging

from nh3powerplant.components.component import Component
from nh3powerplant.core.exceptions import ValidationError
from nh3powerplant.core.identifier import Identifier
from nh3powerplant.core.port import Port
from nh3powerplant.fluids.fluid import Fluid
from nh3powerplant.state.statepoint import StatePoint


logger = logging.getLogger(__name__)


class Pump(Component):
    """
    Incompressible pump model.
    """

    def __init__(
        self,
        identifier: Identifier,
        fluid: Fluid,
        outlet_identifier: Identifier,
        outlet_pressure: float,
        isentropic_efficiency: float,
        inlet_state: StatePoint | None = None,
    ) -> None:
        """
        Parameters
        ----------
        identifier
            Unique component identifier.
        fluid
            Fluid property provider.
        outlet_identifier
            Identifier of the generated outlet state.
        outlet_pressure
            Pump outlet pressure in Pa.
        isentropic_efficiency
            Pump isentropic efficiency.
        inlet_state
            Optional initial thermodynamic state at the pump inlet.
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
        self._inlet_port = Port(
            identifier=Identifier(identifier.component, identifier.circuit, "in"),
            description="Pump inlet",
            state=inlet_state,
        )
        self._outlet_port = Port(
            identifier=outlet_identifier,
            description="Pump outlet",
        )
        self._outlet_state: StatePoint | None = None
        self._power: float | None = None

    @property
    def inlet_port(self) -> Port:
        """
        Return the material inlet port.
        """
        return self._inlet_port

    @property
    def outlet_port(self) -> Port:
        """
        Return the material outlet port.
        """
        return self._outlet_port

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
        inlet_state = self._required_state(self._inlet_port.state)
        inlet_pressure = self._required("pressure", inlet_state.pressure)
        inlet_enthalpy = self._required("enthalpy", inlet_state.enthalpy)
        inlet_density = self._required("density", inlet_state.density)
        mass_flow = self._required("mass_flow", inlet_state.mass_flow)
        logger.debug(
            "Pump input: id=%s, inlet_state=%s, p_in_Pa=%.6f, h_in_J_per_kg=%.6f, "
            "rho_in_kg_per_m3=%.6f, mass_flow_kg_per_s=%.9f, p_out_Pa=%.6f, eta=%.6f",
            self.identifier,
            inlet_state.identifier,
            inlet_pressure,
            inlet_enthalpy,
            inlet_density,
            mass_flow,
            self._outlet_pressure,
            self._isentropic_efficiency,
        )

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
        self._outlet_port.state = self._outlet_state
        self._power = mass_flow * specific_work
        logger.debug(
            "Pump output: id=%s, outlet_state=%s, specific_work_J_per_kg=%.6f, power_W=%.6f",
            self.identifier,
            self._outlet_state.identifier,
            specific_work,
            self._power,
        )

    def execute(self) -> None:
        """
        Execute the pump calculation.
        """
        self.calculate()

    def _required(self, name: str, value: float | None) -> float:
        if value is None:
            raise ValidationError(f"inlet state requires {name}")

        return value

    def _required_state(self, value: StatePoint | None) -> StatePoint:
        if value is None:
            raise ValidationError("inlet port requires state")

        return value
