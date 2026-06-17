import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
import pandas as pd
from local_timeline.phase_chronology import (
    build_phase_chronology_registry, map_events_to_phases, build_phase_event_digest
)
from local_timeline.timeline_config import get_default_local_timeline_profile

def test_phase_chronology_registry():
    event_data = [
        {"event_id": "1", "phase_number": 1, "module_name": "modA", "relative_path": "a.txt", "event_time_utc": "2023-01-01T00:00:00Z"},
        {"event_id": "2", "phase_number": 1, "module_name": "modA", "relative_path": "b.txt", "event_time_utc": "2023-01-02T00:00:00Z"}
    ]
    df_evt = pd.DataFrame(event_data)
    profile = get_default_local_timeline_profile()
    df_phase, summary = build_phase_chronology_registry(df_evt, profile)

    assert not df_phase.empty
    assert len(df_phase) == 1
    assert df_phase.iloc[0]['event_count'] == 2
    assert "perfect" not in str(df_phase.iloc[0]['status']).lower() # "status" is "completed", no perfection guarantees.

def test_map_events_to_phases():
    event_data = [{"event_id": "1", "phase_number": 1}]
    phase_data = [{"phase_number": 1, "phase_title": "Phase 1 title"}]
    df_evt = pd.DataFrame(event_data)
    df_ph = pd.DataFrame(phase_data)
    mapped = map_events_to_phases(df_evt, df_ph)

    assert not mapped.empty
    assert 'phase_title' in mapped.columns

def test_build_phase_event_digest():
    phase_data = [{"phase_number": 1, "phase_title": "Phase 1 title", "event_count": 5, "first_seen_utc": None, "last_seen_utc": None, "related_modules": []}]
    df_ph = pd.DataFrame(phase_data)
    profile = get_default_local_timeline_profile()
    txt, summary = build_phase_event_digest(pd.DataFrame(), df_ph, profile)

    assert isinstance(txt, str)
    assert "Phase 1 title" in txt
