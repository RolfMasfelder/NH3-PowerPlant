"""
Unit tests for the Evaporator component.
"""

from __future__ import annotations

from nh3powerplant.components import Evaporator
from nh3powerplant.core.identifier import Identifier
from nh3powerplant.fluids import CoolPropFluid


def test_evaporator_calculates_outlet_state_and_heat_flow() -> None:
    """
    The evaporator shall heat the working fluid to saturated vapor.
    """

    fluid = CoolPropFluid("NH3")
    inlet_state = fluid.state_from_temperature_quality(
        identifier=Identifier("Evaporator", "NH3", "in"),
        temperature=293.15,
        vapor_quality=0.0,
        mass_flow=1.0,
    )
    evaporator = Evaporator(
        identifier=Identifier("Evaporator", "NH3", "body"),
        fluid=fluid,
        inlet_state=inlet_state,
        outlet_identifier=Identifier("Evaporator", "NH3", "out"),
        outlet_temperature=353.15,
    )

    evaporator.calculate()

    assert evaporator.outlet_state is not None
    assert evaporator.heat_flow is not None
    assert evaporator.outlet_state.vapor_quality == 1.0
    assert evaporator.heat_flow > 0.0
