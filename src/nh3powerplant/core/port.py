from dataclasses import dataclass

from nh3powerplant.core import Identifier


@dataclass(slots=True)
class Port:
    """
    Connection point of a component.
    """

    identifier: Identifier

    description: str = ""

    state = None
