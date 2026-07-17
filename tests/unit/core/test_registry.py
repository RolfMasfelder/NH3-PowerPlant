import pytest

from nh3powerplant.core import Identifier
from nh3powerplant.core import Registry
from nh3powerplant.core import ValidationError


def test_empty() -> None:

    r = Registry[int]()

    assert len(r) == 0


def test_add() -> None:

    r = Registry[int]()

    i = Identifier("Pump","NH3", "out")

    r.add(i, 42)

    assert len(r) == 1

    assert r.get(i) == 42



def test_duplicate() -> None:

    r = Registry[int]()

    i = Identifier("Pump","NH3", "out")

    r.add(i, 1)

    with pytest.raises(ValidationError):

        r.add(i, 2)


def test_remove() -> None:

    r = Registry[int]()

    i = Identifier("Pump","NH3", "out")

    r.add(i, 10)

    r.remove(i)

    assert len(r) == 0


def test_contains() -> None:

    r = Registry[int]()

    i = Identifier("Pump","NH3", "out")

    r.add(i, 1)

    assert i in r


def test_iteration() -> None:

    r = Registry[int]()

    r.add(Identifier("A","NH3", "out"), 1)

    r.add(Identifier("B","NH3", "out"), 2)

    assert sum(r) == 3


def test_clear() -> None:

    r = Registry[int]()

    r.add(Identifier("A","NH3", "out"), 1)

    r.clear()

    assert len(r) == 0
