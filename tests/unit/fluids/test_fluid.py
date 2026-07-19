"""
Unit tests for fluid property providers.
"""

from __future__ import annotations

import pytest

from nh3powerplant.core.exceptions import ValidationError
from nh3powerplant.core.identifier import Identifier
from nh3powerplant.fluids import CoolPropFluid


def test_coolprop_fluid_name() -> None:
    """
    The fluid shall expose its CoolProp name.
    """

    fluid = CoolPropFluid("NH3")

    assert fluid.name == "NH3"


def test_state_from_pressure_temperature() -> None:
    """
    The fluid shall calculate a complete state from pressure and temperature.
    """

    fluid = CoolPropFluid("NH3")
    identifier = Identifier("Turbine", "NH3", "in")

    state = fluid.state_from_pressure_temperature(
        identifier=identifier,
        pressure=1_000_000.0,
        temperature=300.0,
        mass_flow=0.5,
    )

    assert state.identifier == identifier
    assert state.fluid == "NH3"
    assert state.pressure == 1_000_000.0
    assert state.temperature == 300.0
    assert state.mass_flow == 0.5
    assert state.enthalpy is not None
    assert state.entropy is not None
    assert state.density is not None


def test_state_from_pressure_enthalpy_roundtrip() -> None:
    """
    A state reconstructed from pressure and enthalpy shall preserve temperature.
    """

    fluid = CoolPropFluid("NH3")

    initial = fluid.state_from_pressure_temperature(
        identifier=Identifier("Pump", "NH3", "out"),
        pressure=1_000_000.0,
        temperature=300.0,
    )

    assert initial.enthalpy is not None
    assert initial.pressure is not None

    reconstructed = fluid.state_from_pressure_enthalpy(
        identifier=Identifier("Pump", "NH3", "check"),
        pressure=initial.pressure,
        enthalpy=initial.enthalpy,
    )

    assert reconstructed.temperature == pytest.approx(initial.temperature)
    assert reconstructed.entropy == pytest.approx(initial.entropy)
    assert reconstructed.density == pytest.approx(initial.density)


def test_state_from_pressure_entropy_roundtrip() -> None:
    """
    A state reconstructed from pressure and entropy shall preserve temperature.
    """

    fluid = CoolPropFluid("NH3")

    initial = fluid.state_from_pressure_temperature(
        identifier=Identifier("Turbine", "NH3", "in"),
        pressure=1_000_000.0,
        temperature=300.0,
    )

    assert initial.entropy is not None
    assert initial.pressure is not None

    reconstructed = fluid.state_from_pressure_entropy(
        identifier=Identifier("Turbine", "NH3", "check"),
        pressure=initial.pressure,
        entropy=initial.entropy,
    )

    assert reconstructed.temperature == pytest.approx(initial.temperature)
    assert reconstructed.enthalpy == pytest.approx(initial.enthalpy)
    assert reconstructed.density == pytest.approx(initial.density)


def test_reject_empty_fluid_name() -> None:
    """
    Empty fluid names shall be rejected.
    """

    with pytest.raises(ValidationError):
        CoolPropFluid(" ")
