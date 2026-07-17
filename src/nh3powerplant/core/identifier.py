"""
Unique identifier for simulation objects.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True, order=True)
class Identifier:
    """
    Unique identifier of a simulation object.

    Parameters
    ----------
    component
        Name of the component.
    circuit
        Name of the thermodynamic circuit.
    port
        Port name.

    Examples
    --------
    HeatPump.NH3.in

    Turbine.NH3.out
    """

    component: str

    circuit: str

    port: str

    def __post_init__(self) -> None:

        if not self.component.strip():
            raise ValueError("component must not be empty")

        if not self.circuit.strip():
            raise ValueError("circuit must not be empty")

        if not self.port.strip():
            raise ValueError("port must not be empty")

    def __str__(self) -> str:

        return f"{self.component}.{self.circuit}.{self.port}"
