"""
Unit tests for JSON result I/O.
"""

from __future__ import annotations

from pathlib import Path

from nh3powerplant.results import JsonResultIO
from nh3powerplant.results import RunInfo
from nh3powerplant.results import SimulationResult


def test_write_and_read_result_dict(tmp_path: Path) -> None:
    """
    Simulation results shall be written and read as JSON dictionaries.
    """

    result = SimulationResult(
        run=RunInfo(
            id="reference-a",
            timestamp="2026-07-19T00:00:00+00:00",
            project_version="0.1.0",
            simulation_name="Reference model",
            variant="A",
            description="Reference run",
        )
    )
    io = JsonResultIO()
    path = tmp_path / "result.json"

    written_path = io.write(result, path)
    data = io.read_dict(path)

    assert written_path == path
    assert data["run"]["id"] == "reference-a"
