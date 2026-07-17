"""
Object provenance.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, UTC


@dataclass(slots=True)
class Provenance:

    simulation_id: str

    component: str

    iteration: int = 0

    created: datetime = field(default_factory=lambda: datetime.now(UTC))
