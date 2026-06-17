import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
import pandas as pd
from datetime import datetime, timezone, timedelta
from local_timeline.freshness_analysis import classify_event_freshness, build_event_freshness_report, build_stale_artifact_timeline_report
from local_timeline.timeline_config import get_default_local_timeline_profile

def test_classify_event_freshness():
    profile = get_default_local_timeline_profile()

    assert classify_event_freshness(None, profile) == "event_missing_timestamp"
    assert classify_event_freshness("invalid", profile) == "event_unknown_time"

    now = datetime.now(timezone.utc)
    fresh = now.isoformat()
    stale = (now - timedelta(days=100)).isoformat()
    warn = (now - timedelta(days=50)).isoformat()

    assert classify_event_freshness(fresh, profile) == "event_fresh"
    assert classify_event_freshness(stale, profile) == "event_stale"
    assert classify_event_freshness(warn, profile) == "event_warning_stale"

def test_build_event_freshness_report():
    now = datetime.now(timezone.utc)
    df = pd.DataFrame([{"event_time_utc": now.isoformat()}])
    profile = get_default_local_timeline_profile()
    report, summary = build_event_freshness_report(df, profile)

    assert not report.empty
    assert summary["fresh_count"] == 1

def test_build_stale_artifact_timeline_report():
    df = pd.DataFrame([{"temporal_status": "event_stale"}])
    profile = get_default_local_timeline_profile()
    report, summary = build_stale_artifact_timeline_report(df, profile)

    assert not report.empty
    assert summary["total_stale"] == 1
