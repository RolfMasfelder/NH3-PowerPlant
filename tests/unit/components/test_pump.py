"""
Unit tests for the Pump component.
"""

from __future__ import annotations

import pytest

from nh3powerplant.components import Pump
from nh3powerplant.core.exceptions import ValidationError
from nh3powerplant.core.identifier import Identifier
from nh3powerplant.fluids import CoolPropFluid


def test_pump_calculates_outlet_state_and_power() -> None:
    """
    The pump shall increase pressure and consume shaft power.
    """

    fluid = CoolPropFluid("NH3")
    inlet_state = fluid.state_from_pressure_temperature(
        identifier=Identifier("Pump", "NH3", "in"),
        pressure=500_000.0,
        temperature=250.0,
        mass_flow=1.2,
    )
    pump = Pump(
        identifier=Identifier("Pump", "NH3", "body"),
        fluid=fluid,
        inlet_state=inlet_state,
        outlet_identifier=Identifier("Pump", "NH3", "out"),
        outlet_pressure=1_000_000.0,
        isentropic_efficiency=0.75,
    )

    pump.calculate()

    assert pump.outlet_state is not None
    assert pump.power is not None
    assert pump.outlet_state.pressure == 1_000_000.0
    assert pump.outlet_state.mass_flow == pytest.approx(1.2)
    assert pump.power > 0.0


def test_pump_rejects_invalid_efficiency() -> None:
    """
    The pump shall reject efficiencies outside the valid range.
    """

    fluid = CoolPropFluid("NH3")
    inlet_state = fluid.state_from_pressure_temperature(
        identifier=Identifier("Pump", "NH3", "in"),
        pressure=500_000.0,
        temperature=250.0,
    )

    with pytest.raises(ValidationError):
        Pump(
            identifier=Identifier("Pump", "NH3", "body"),
            fluid=fluid,
            inlet_state=inlet_state,
            outlet_identifier=Identifier("Pump", "NH3", "out"),
            outlet_pressure=1_000_000.0,
            isentropic_efficiency=0.0,
        )


def test_pump_requires_mass_flow() -> None:
    """
    The pump shall require mass flow to calculate power.
    """

    fluid = CoolPropFluid("NH3")
    inlet_state = fluid.state_from_pressure_temperature(
        identifier=Identifier("Pump", "NH3", "in"),
        pressure=500_000.0,
        temperature=250.0,
    )
    pump = Pump(
        identifier=Identifier("Pump", "NH3", "body"),
        fluid=fluid,
        inlet_state=inlet_state,
        outlet_identifier=Identifier("Pump", "NH3", "out"),
        outlet_pressure=1_000_000.0,
        isentropic_efficiency=0.75,
    )

    with pytest.raises(ValidationError):
        pump.calculate()
