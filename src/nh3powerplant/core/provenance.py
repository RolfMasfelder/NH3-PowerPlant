"""
Object provenance.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass(slots=True)
class Provenance:

    simulation_id: str

    component: str

    iteration: int = 0

    created: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
