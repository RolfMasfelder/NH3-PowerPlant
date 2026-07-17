from nh3powerplant.core import Provenance


def test_provenance() -> None:

    p = Provenance(

        simulation_id="run001",

        component="Pump"

    )

    assert p.component == "Pump"

    assert p.iteration == 0
