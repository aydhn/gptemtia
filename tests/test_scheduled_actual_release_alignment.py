"""Tests for Phase 132 Scheduled vs Actual Release Alignment."""

import pandas as pd
from advanced_macro_event_news_regime.scheduled_actual_release_alignment import (
    build_scheduled_actual_release_alignment_registry,
    validate_scheduled_actual_release_alignment,
    summarize_scheduled_actual_release_alignment,
)


def test_build_scheduled_actual_release_alignment():
    df, summary = build_scheduled_actual_release_alignment_registry()
    assert not df.empty
    assert len(df) >= 3
    assert "alignment_id" in df.columns
    assert "alignment_status" in df.columns
    assert summary["all_non_signal"] is True
    assert summary["all_source_preserved"] is True


def test_validate_scheduled_actual_release_alignment():
    # Valid alignment: actual >= scheduled
    valid_df = pd.DataFrame({
        "sched_time": ["2026-01-01 13:30:00", "2026-01-02 13:30:00"],
        "actual_time": ["2026-01-01 13:30:02", "2026-01-02 13:30:01"],
    })
    res = validate_scheduled_actual_release_alignment(valid_df, "sched_time", "actual_time")
    assert res["valid"] is True
    assert res["lookahead_risk"] is False

    # Invalid alignment: actual < scheduled (premature leak)
    invalid_df = pd.DataFrame({
        "sched_time": ["2026-01-01 13:30:00"],
        "actual_time": ["2026-01-01 13:29:59"],
    })
    res_inv = validate_scheduled_actual_release_alignment(invalid_df, "sched_time", "actual_time")
    assert res_inv["valid"] is False
    assert res_inv["lookahead_risk"] is True


def test_summarize_scheduled_actual_release_alignment():
    df, _ = build_scheduled_actual_release_alignment_registry()
    summary = summarize_scheduled_actual_release_alignment(df)
    assert summary["total_alignments"] >= 3
    assert summary["all_aligned"] is True
    assert summary["all_non_signal"] is True
