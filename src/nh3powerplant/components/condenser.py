"""
Condenser component model.
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


class Condenser(Component):
    """
    Condenser with a prescribed outlet temperature and vapor quality.
    """

    def __init__(
        self,
        identifier: Identifier,
        fluid: Fluid,
        outlet_identifier: Identifier,
        outlet_temperature: float,
        outlet_vapor_quality: float = 0.0,
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
        outlet_temperature
            Outlet saturation temperature in K.
        outlet_vapor_quality
            Outlet vapor quality.
        inlet_state
            Optional initial thermodynamic state at the condenser inlet.
        """
        super().__init__(identifier)
        self._fluid = fluid
        self._inlet_state = inlet_state
        self._outlet_identifier = outlet_identifier
        self._outlet_temperature = outlet_temperature
        self._outlet_vapor_quality = outlet_vapor_quality
        self._inlet_port = Port(
            identifier=Identifier(identifier.component, identifier.circuit, "in"),
            description="Condenser inlet",
            state=inlet_state,
        )
        self._outlet_port = Port(
            identifier=outlet_identifier,
            description="Condenser outlet",
        )
        self._outlet_state: StatePoint | None = None
        self._heat_flow: float | None = None

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
    def heat_flow(self) -> float | None:
        """
        Return the heat flow rejected by the working fluid in W.
        """
        return self._heat_flow

    def calculate(self) -> None:
        """
        Calculate outlet state and rejected heat flow.
        """
        inlet_state = self._required_state(self._inlet_port.state)
        inlet_enthalpy = self._required("enthalpy", inlet_state.enthalpy)
        mass_flow = self._required("mass_flow", inlet_state.mass_flow)
        logger.debug(
            "Condenser input: id=%s, inlet_state=%s, h_in_J_per_kg=%.6f, "
            "mass_flow_kg_per_s=%.9f, T_out_K=%.6f, x_out=%.6f",
            self.identifier,
            inlet_state.identifier,
            inlet_enthalpy,
            mass_flow,
            self._outlet_temperature,
            self._outlet_vapor_quality,
        )

        self._outlet_state = self._fluid.state_from_temperature_quality(
            identifier=self._outlet_identifier,
            temperature=self._outlet_temperature,
            vapor_quality=self._outlet_vapor_quality,
            mass_flow=mass_flow,
        )
        self._outlet_port.state = self._outlet_state
        outlet_enthalpy = self._required("outlet enthalpy", self._outlet_state.enthalpy)
        self._heat_flow = mass_flow * (inlet_enthalpy - outlet_enthalpy)

        if self._heat_flow <= 0.0:
            raise ValidationError("condenser heat flow must be positive")

        logger.debug(
            "Condenser output: id=%s, outlet_state=%s, h_out_J_per_kg=%.6f, heat_flow_W=%.6f",
            self.identifier,
            self._outlet_state.identifier,
            outlet_enthalpy,
            self._heat_flow,
        )

    def execute(self) -> None:
        """
        Execute the condenser calculation.
        """
        self.calculate()

    def _required(self, name: str, value: float | None) -> float:
        if value is None:
            raise ValidationError(f"state requires {name}")

        return value

    def _required_state(self, value: StatePoint | None) -> StatePoint:
        if value is None:
            raise ValidationError("inlet port requires state")

        return value
