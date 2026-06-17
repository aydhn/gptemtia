import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
import pandas as pd
from local_timeline.timeline_validation import (
    validate_no_cloud_or_live_timeline_usage, validate_project_events,
    validate_phase_chronology, validate_artifact_evolution, build_timeline_validation_report
)
from local_timeline.timeline_config import get_default_local_timeline_profile

def test_validate_no_cloud_or_live_timeline_usage():
    res = validate_no_cloud_or_live_timeline_usage(text="cloud upload failed")
    assert not res["valid"]
    assert "forbidden_term_cloud_upload" in res["warnings"]

    res2 = validate_no_cloud_or_live_timeline_usage(text="safe local report")
    assert res2["valid"]

def test_validate_project_events():
    profile = get_default_local_timeline_profile()

    df1 = pd.DataFrame()
    v1 = validate_project_events(df1, profile)
    assert v1["valid"]

    df2 = pd.DataFrame([{"event_id": "1", "event_type": "invalid", "source_label": "project_files_source"}])
    v2 = validate_project_events(df2, profile)
    assert not v2["valid"]
    assert "invalid_event_type" in v2["warnings"]

def test_build_timeline_validation_report():
    profile = get_default_local_timeline_profile()
    tables = {
        "event_registry": pd.DataFrame([{"event_id": "1", "event_type": "phase_event", "source_label": "project_files_source"}]),
        "phase_chronology": pd.DataFrame(),
        "artifact_evolution": pd.DataFrame()
    }
    df, summary = build_timeline_validation_report(tables, profile)
    assert summary["all_valid"]
    assert len(df) == 3
