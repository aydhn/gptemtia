"""Unit tests for Phase 119 session calendar alignment and bucketing."""

import pytest
import pandas as pd
from advanced_cross_asset_alignment.session_calendar_alignment import (
    build_session_bucket,
    build_session_calendar_alignment_registry,
    SESSION_POLICIES,
)


def test_build_session_bucket():
    ts = "2026-09-03T14:30:00Z"
    assert build_session_bucket(ts, "utc_day") == "2026-09-03"
    assert build_session_bucket(ts, "utc_hour") == "2026-09-03T14"
    assert build_session_bucket(ts, "fx_24_5_placeholder") == "2026-W36"
    assert "cm_sess_" in build_session_bucket(ts, "commodity_session_placeholder")
    assert "macro_rel_" in build_session_bucket(ts, "macro_release_session_placeholder")


def test_session_calendar_registry():
    df, summary = build_session_calendar_alignment_registry()
    assert len(df) == 7
    assert summary["total_session_policies"] == 7
    assert summary["non_signal"] is True
    assert summary["status"] == "READY"
