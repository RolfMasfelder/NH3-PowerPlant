from nh3powerplant.state import Phase
from nh3powerplant.state import StatePoint


def test_empty_state():

    s = StatePoint("S1")

    assert s.name == "S1"

    assert s.phase == Phase.UNKNOWN

    assert not s.is_complete()


def test_complete_state():

    s = StatePoint("S1")

    s.temperature = 300

    s.pressure = 101325

    s.enthalpy = 120000

    s.entropy = 450

    assert s.is_complete()


def test_serialization():

    s = StatePoint("A")

    s.temperature = 300

    d = s.to_dict()

    s2 = StatePoint.from_dict(d)

    assert s2.name == "A"

    assert s2.temperature == 300


def test_metadata():

    s = StatePoint("S")

    s.metadata["component"] = "Pump"

    assert s.metadata["component"] == "Pump"
