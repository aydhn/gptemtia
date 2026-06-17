import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
import pandas as pd
from local_timeline.artifact_evolution import (
    build_artifact_evolution_registry, detect_artifact_evolution_patterns, build_artifact_evolution_record
)
from local_timeline.timeline_config import get_default_local_timeline_profile

def test_build_artifact_evolution_registry():
    event_data = [
        {"relative_path": "file1.txt", "event_type": "typeA", "module_name": "mod", "event_time_utc": "2023-01-01T00:00:00Z", "change_impact": "informational_change"}
    ]
    df_evt = pd.DataFrame(event_data)
    profile = get_default_local_timeline_profile()
    df_evo, summary = build_artifact_evolution_registry(df_evt, profile)

    assert not df_evo.empty
    assert len(df_evo) == 1
    assert "temporal_status" in df_evo.columns

def test_detect_artifact_evolution_patterns():
    evo_data = [
        {"artifact_id": "1", "temporal_status": "event_stale", "event_count": 1}
    ]
    df_evo = pd.DataFrame(evo_data)
    df_pat = detect_artifact_evolution_patterns(df_evo)

    assert not df_pat.empty
    assert "stale_artifact" in df_pat.iloc[0]['patterns']

def test_evolution_is_not_diff():
    # Record has counts and timestamps, not content diff
    event_data = [{"relative_path": "file1.txt", "event_type": "typeA", "module_name": "mod", "event_time_utc": "2023-01-01T00:00:00Z", "change_impact": "informational_change"}]
    df_evt = pd.DataFrame(event_data)
    profile = get_default_local_timeline_profile()
    rec = build_artifact_evolution_record("file1.txt", df_evt, profile)
    assert not hasattr(rec, "content_diff")
