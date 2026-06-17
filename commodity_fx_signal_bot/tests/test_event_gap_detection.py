import pytest
import pandas as pd
from local_timeline.event_gap_detection import (
    detect_missing_phase_events, detect_missing_expected_timeline_domains,
    detect_stale_or_missing_artifact_events, detect_event_gaps
)
from local_timeline.timeline_config import get_default_local_timeline_profile

def test_detect_missing_phase_events():
    df_ph = pd.DataFrame([{"phase_number": 1, "event_count": 0}])
    df_evt = pd.DataFrame([{"phase_number": 2}])
    gaps = detect_missing_phase_events(df_ph, df_evt)
    assert not gaps.empty
    assert gaps.iloc[0]['gap_type'] == "missing_phase_events"

def test_detect_missing_expected_timeline_domains():
    df_evt = pd.DataFrame([{"source_label": "data_lake_source"}])
    gaps = detect_missing_expected_timeline_domains(df_evt)
    assert not gaps.empty
    assert "missing_expected_domain" in gaps['gap_type'].values

def test_detect_stale_or_missing_artifact_events():
    df_evo = pd.DataFrame([{"temporal_status": "event_stale", "relative_path": "a.txt"}])
    profile = get_default_local_timeline_profile()
    gaps = detect_stale_or_missing_artifact_events(df_evo, profile)
    assert not gaps.empty
    assert gaps.iloc[0]['gap_type'] == "event_stale"

def test_detect_event_gaps():
    df_evt = pd.DataFrame([{"source_label": "project_files_source"}])
    df_ph = pd.DataFrame([{"phase_number": 1, "event_count": 0}])
    df_evo = pd.DataFrame([{"temporal_status": "event_stale", "relative_path": "a.txt"}])
    profile = get_default_local_timeline_profile()

    gaps = detect_event_gaps(df_evt, df_ph, df_evo, profile)
    assert not gaps.empty
    assert len(gaps) > 1 # Should catch missing domains, missing phase, and stale artifact
