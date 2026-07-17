"""
Unit tests for the generic Registry.
"""

from dataclasses import dataclass

import pytest

from nh3powerplant.core.exceptions import NotFoundError
from nh3powerplant.core.exceptions import ValidationError
from nh3powerplant.core.identifier import Identifier
from nh3powerplant.core.registry import Registry


@dataclass(slots=True, frozen=True)
class DummyObject:
    """
    Minimal object implementing the Identifiable protocol.
    """

    identifier: Identifier

    value: int


def test_empty_registry() -> None:

    registry: Registry[DummyObject] = Registry()

    assert len(registry) == 0


def test_add_object() -> None:

    registry: Registry[DummyObject] = Registry()

    obj = DummyObject(
        identifier=Identifier("Pump", "NH3", "out"),
        value=42,
    )

    registry.add(obj)

    assert len(registry) == 1

    assert registry.get(obj.identifier) is obj


def test_contains() -> None:

    registry: Registry[DummyObject] = Registry()

    obj = DummyObject(
        Identifier("Pump", "NH3", "out"),
        1,
    )

    registry.add(obj)

    assert obj.identifier in registry


def test_duplicate_identifier() -> None:

    registry: Registry[DummyObject] = Registry()

    identifier = Identifier("Pump", "NH3", "out")

    registry.add(DummyObject(identifier, 1))

    with pytest.raises(ValidationError):
        registry.add(DummyObject(identifier, 2))


def test_remove() -> None:

    registry: Registry[DummyObject] = Registry()

    obj = DummyObject(
        Identifier("Pump", "NH3", "out"),
        5,
    )

    registry.add(obj)

    registry.remove(obj.identifier)

    assert len(registry) == 0


def test_unknown_identifier() -> None:

    registry: Registry[DummyObject] = Registry()

    with pytest.raises(NotFoundError):
        registry.get(
            Identifier("Unknown", "NH3", "out")
        )


def test_clear() -> None:

    registry: Registry[DummyObject] = Registry()

    registry.add(
        DummyObject(
            Identifier("A", "NH3", "out"),
            1,
        )
    )

    registry.add(
        DummyObject(
            Identifier("B", "NH3", "out"),
            2,
        )
    )

    registry.clear()

    assert len(registry) == 0


def test_iteration() -> None:

    registry: Registry[DummyObject] = Registry()

    registry.add(
        DummyObject(
            Identifier("A", "NH3", "out"),
            1,
        )
    )

    registry.add(
        DummyObject(
            Identifier("B", "NH3", "out"),
            2,
        )
    )

    values = sorted(obj.value for obj in registry)

    assert values == [1, 2]
