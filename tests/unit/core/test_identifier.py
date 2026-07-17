from nh3powerplant.core import Identifier


def test_identifier() -> None:

    i = Identifier("Pump", "NH3", "out")

    assert str(i) == "Pump.NH3.out"


def test_compare() -> None:

    a = Identifier("A", "NH3", "out")

    b = Identifier("B", "NH3", "out")

    assert a < b
