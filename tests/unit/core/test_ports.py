from nh3powerplant.components.component import Component
from nh3powerplant.core import Identifier


class Dummy(Component):

    def calculate(self) -> None:

        pass


def test_ports() -> None:

    c = Dummy("Pump")

    c.add_port(

        Identifier(

            component="Pump",

            circuit="NH3",

            port="in"

        )

    )

    assert len(c.ports) == 1
