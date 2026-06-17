import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
import pandas as pd
from local_timeline.timeline_query import (
    classify_timeline_query_intent, parse_timeline_query, execute_timeline_query
)
from local_timeline.timeline_config import get_default_local_timeline_profile

def test_classify_timeline_query_intent():
    assert classify_timeline_query_intent("Phase 60 sonrası") == "find_events_by_phase"
    assert classify_timeline_query_intent("hangi artifactler stale") == "find_stale_artifacts"
    assert classify_timeline_query_intent("timeline gap var mı") == "find_timeline_gaps"
    assert classify_timeline_query_intent("son değişiklikler") == "find_recent_changes"
    assert classify_timeline_query_intent("bu modül ne zaman") == "find_events_by_module"
    assert classify_timeline_query_intent("bunu kim yazdı") == "unknown_timeline_query"

def test_parse_timeline_query_rejects_trading():
    profile = get_default_local_timeline_profile()
    q = parse_timeline_query("al sinyali ver", profile)
    assert "query_rejected_due_to_trading_intent" in q.warnings

def test_execute_timeline_query_rejection():
    profile = get_default_local_timeline_profile()
    q = parse_timeline_query("sat emri gönder", profile)
    df, summary = execute_timeline_query(q, pd.DataFrame(), profile=profile)
    assert df.empty
    assert summary.get("status") == "rejected"

def test_execute_timeline_query_success():
    profile = get_default_local_timeline_profile()
    q = parse_timeline_query("son değişiklikler neler?", profile)
    df_evt = pd.DataFrame([{"event_id": "1", "event_type": "typeA"}])
    df, summary = execute_timeline_query(q, df_evt, profile=profile)
    assert not df.empty
    assert summary["total_results"] > 0
