"""
JSON input and output for simulation results.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any
from typing import cast

from nh3powerplant.results.simulation_result import SimulationResult


class JsonResultIO:
    """
    Read and write simulation results as JSON.
    """

    def write(self, result: SimulationResult, path: Path) -> Path:
        """
        Write a simulation result to a JSON file.
        """
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            json.dumps(result.to_dict(), indent=2, sort_keys=True),
            encoding="utf-8",
        )
        return path

    def read_dict(self, path: Path) -> dict[str, Any]:
        """
        Read a simulation result JSON file as dictionary.
        """
        return cast(
            dict[str, Any],
            json.loads(path.read_text(encoding="utf-8")),
        )
