from nh3powerplant.state import Phase
from nh3powerplant.state import StatePoint


def test_empty_state() -> None:

    s = StatePoint("S1")

    assert s.name == "S1"

    assert s.phase == Phase.UNKNOWN

    assert not s.is_complete()


def test_complete_state() -> None:

    s = StatePoint("S1")

    s.temperature = 300

    s.pressure = 101325

    s.enthalpy = 120000

    s.entropy = 450

    assert s.is_complete()


def test_serialization() -> None:

    s = StatePoint("A")

    s.temperature = 300

    d = s.to_dict()

    s2 = StatePoint.from_dict(d)

    assert s2.name == "A"

    assert s2.temperature == 300
