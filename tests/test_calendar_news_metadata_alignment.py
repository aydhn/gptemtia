"""Unit tests for Phase 119 Calendar - News metadata alignment registry."""

import pytest
import pandas as pd
from advanced_cross_asset_alignment.calendar_news_metadata_alignment import build_calendar_news_metadata_alignment_registry


def test_calendar_news_metadata_alignment_registry():
    df, summary = build_calendar_news_metadata_alignment_registry()
    assert len(df) == 4
    assert summary["total_alignments"] == 4
    assert summary["all_non_signal"] is True
    assert summary["all_no_full_text"] is True
    assert summary["status"] == "READY"

    events = set(df["calendar_event"])
    assert "FOMC_RATE_DECISION" in events
    assert "US_NONFARM_PAYROLLS_RELEASE" in events
