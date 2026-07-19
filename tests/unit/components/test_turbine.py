"""
Unit tests for the Turbine component.
"""

from __future__ import annotations

import pytest

from nh3powerplant.components import Turbine
from nh3powerplant.core.exceptions import ValidationError
from nh3powerplant.core.identifier import Identifier
from nh3powerplant.fluids import CoolPropFluid


def test_turbine_calculates_outlet_state_and_power() -> None:
    """
    The turbine shall reduce pressure and produce shaft power.
    """

    fluid = CoolPropFluid("NH3")
    inlet_state = fluid.state_from_pressure_temperature(
        identifier=Identifier("Turbine", "NH3", "in"),
        pressure=2_000_000.0,
        temperature=370.0,
        mass_flow=0.8,
    )
    turbine = Turbine(
        identifier=Identifier("Turbine", "NH3", "body"),
        fluid=fluid,
        inlet_state=inlet_state,
        outlet_identifier=Identifier("Turbine", "NH3", "out"),
        outlet_pressure=700_000.0,
        isentropic_efficiency=0.82,
    )

    turbine.calculate()

    assert turbine.outlet_state is not None
    assert turbine.power is not None
    assert turbine.outlet_state.pressure == 700_000.0
    assert turbine.outlet_state.mass_flow == pytest.approx(0.8)
    assert turbine.power > 0.0


def test_turbine_rejects_invalid_efficiency() -> None:
    """
    The turbine shall reject efficiencies outside the valid range.
    """

    fluid = CoolPropFluid("NH3")
    inlet_state = fluid.state_from_pressure_temperature(
        identifier=Identifier("Turbine", "NH3", "in"),
        pressure=2_000_000.0,
        temperature=370.0,
    )

    with pytest.raises(ValidationError):
        Turbine(
            identifier=Identifier("Turbine", "NH3", "body"),
            fluid=fluid,
            inlet_state=inlet_state,
            outlet_identifier=Identifier("Turbine", "NH3", "out"),
            outlet_pressure=700_000.0,
            isentropic_efficiency=1.2,
        )


def test_turbine_requires_pressure_drop() -> None:
    """
    The turbine shall reject outlet pressures above inlet pressure.
    """

    fluid = CoolPropFluid("NH3")
    inlet_state = fluid.state_from_pressure_temperature(
        identifier=Identifier("Turbine", "NH3", "in"),
        pressure=2_000_000.0,
        temperature=370.0,
        mass_flow=0.8,
    )
    turbine = Turbine(
        identifier=Identifier("Turbine", "NH3", "body"),
        fluid=fluid,
        inlet_state=inlet_state,
        outlet_identifier=Identifier("Turbine", "NH3", "out"),
        outlet_pressure=2_500_000.0,
        isentropic_efficiency=0.82,
    )

    with pytest.raises(ValidationError):
        turbine.calculate()
