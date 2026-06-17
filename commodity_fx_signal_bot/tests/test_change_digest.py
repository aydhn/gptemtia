import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
import pandas as pd
from local_timeline.change_digest import (
    build_recent_change_summary, build_phase_change_digest, build_change_digest_sections,
    build_change_history_digest
)
from local_timeline.timeline_config import get_default_local_timeline_profile

def test_build_recent_change_summary():
    df = pd.DataFrame([{"event_time_utc": "2023-01-01"}, {"event_time_utc": "2023-01-02"}])
    profile = get_default_local_timeline_profile()
    recent = build_recent_change_summary(df, profile)
    assert not recent.empty
    assert recent.iloc[0]['event_time_utc'] == "2023-01-02"

def test_build_phase_change_digest():
    df_ph = pd.DataFrame([{"phase_title": "Phase 1", "event_count": 5}])
    df_evt = pd.DataFrame()
    profile = get_default_local_timeline_profile()
    txt, summary = build_phase_change_digest(df_ph, df_evt, profile)
    assert "Phase 1" in txt
    assert summary["lines"] > 0

def test_build_change_digest_sections():
    df_evt = pd.DataFrame([{"event_id": "1"}])
    df_evo = pd.DataFrame()
    df_gap = pd.DataFrame([{"gap_type": "gap"}])
    sections = build_change_digest_sections(df_evt, df_evo, df_gap)
    assert len(sections) == 2

def test_build_change_history_digest():
    df_evt = pd.DataFrame([{"event_id": "1", "event_time_utc": "2023-01-01T00:00:00Z"}])
    df_evo = pd.DataFrame()
    df_gap = pd.DataFrame()
    profile = get_default_local_timeline_profile()
    txt, summary = build_change_history_digest(df_evt, df_evo, df_gap, profile)

    assert "Change History Digest" in txt
    assert "offline/local project timeline" in txt
    assert "yatırım tavsiyesi değildir" in txt
