"""
Unique identifier for simulation objects.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True, order=True)
class Identifier:
    """
    Identifier consisting of

    component.circuit.port

    Example
    -------

    HeatPump.main.out
    Turbine.main.in
    Condenser.coolingWater.in
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
