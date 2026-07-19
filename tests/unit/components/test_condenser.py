"""
Unit tests for the Condenser component.
"""

from __future__ import annotations

from nh3powerplant.components import Condenser
from nh3powerplant.core.identifier import Identifier
from nh3powerplant.fluids import CoolPropFluid


def test_condenser_calculates_outlet_state_and_heat_flow() -> None:
    """
    The condenser shall cool the working fluid to saturated liquid.
    """

    fluid = CoolPropFluid("NH3")
    inlet_state = fluid.state_from_temperature_quality(
        identifier=Identifier("Condenser", "NH3", "in"),
        temperature=353.15,
        vapor_quality=1.0,
        mass_flow=1.0,
    )
    condenser = Condenser(
        identifier=Identifier("Condenser", "NH3", "body"),
        fluid=fluid,
        inlet_state=inlet_state,
        outlet_identifier=Identifier("Condenser", "NH3", "out"),
        outlet_temperature=293.15,
    )

    condenser.calculate()

    assert condenser.outlet_state is not None
    assert condenser.heat_flow is not None
    assert condenser.outlet_state.vapor_quality == 0.0
    assert condenser.heat_flow > 0.0
