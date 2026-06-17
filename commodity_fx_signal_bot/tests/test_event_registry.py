import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
from pathlib import Path
import pandas as pd
from local_timeline.event_registry import (
    build_project_event_registry, infer_event_type_from_path, infer_event_source_label,
    infer_event_phase_number
)
from local_timeline.timeline_config import get_default_local_timeline_profile

def test_build_project_event_registry(tmp_path):
    # Setup mock structure
    (tmp_path / "reports" / "output").mkdir(parents=True)
    (tmp_path / "reports" / "output" / "test.txt").touch()

    profile = get_default_local_timeline_profile()
    df, summary = build_project_event_registry(tmp_path, profile)

    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert "event_id" in df.columns

def test_infer_event_type_from_path():
    assert infer_event_type_from_path(Path("reports/output/a.txt"), Path(".")) == "report_generated_event"
    assert infer_event_type_from_path(Path("docs/generated/b.txt"), Path(".")) == "documentation_event"

def test_infer_event_source_label():
    assert infer_event_source_label(Path("data/lake/c.parquet"), Path(".")) == "data_lake_source"

def test_infer_event_phase_number():
    assert infer_event_phase_number(Path("phase_67_report.md")) == 67
    assert infer_event_phase_number(Path("other.txt"), text_hint="phase 60") == 60
    assert infer_event_phase_number(Path("other.txt")) is None
