import pytest

from nh3powerplant.core import Identifier
from nh3powerplant.core import Registry
from nh3powerplant.core import ValidationError


def test_empty():

    r = Registry[int]()

    assert len(r) == 0


def test_add():

    r = Registry[int]()

    i = Identifier("Pump", "out")

    r.add(i, 42)

    assert len(r) == 1

    assert r.get(i) == 42



def test_duplicate():

    r = Registry[int]()

    i = Identifier("Pump", "out")

    r.add(i, 1)

    with pytest.raises(ValidationError):

        r.add(i, 2)


def test_remove():

    r = Registry[int]()

    i = Identifier("Pump", "out")

    r.add(i, 10)

    r.remove(i)

    assert len(r) == 0


def test_contains():

    r = Registry[int]()

    i = Identifier("Pump", "out")

    r.add(i, 1)

    assert i in r


def test_iteration():

    r = Registry[int]()

    r.add(Identifier("A", "out"), 1)

    r.add(Identifier("B", "out"), 2)

    assert sum(r) == 3


def test_clear():

    r = Registry[int]()

    r.add(Identifier("A", "out"), 1)

    r.clear()

    assert len(r) == 0
