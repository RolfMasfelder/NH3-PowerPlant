from nh3powerplant.core import Identifier


def test_identifier():

    i = Identifier("Pump", "out")

    assert str(i) == "Pump.out"


def test_compare():

    a = Identifier("A", "out")

    b = Identifier("B", "out")

    assert a < b
