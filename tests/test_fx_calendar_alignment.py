"""Unit tests for Phase 119 FX - Calendar alignment registry."""

import pytest
import pandas as pd
from advanced_cross_asset_alignment.fx_calendar_alignment import build_fx_calendar_alignment_registry


def test_fx_calendar_alignment_registry():
    df, summary = build_fx_calendar_alignment_registry()
    assert len(df) == 5
    assert summary["total_alignments"] == 5
    assert summary["all_non_signal"] is True
    assert summary["status"] == "READY"

    events = set(df["calendar_event"])
    assert "FOMC_RATE_DECISION" in events
    assert "ECB_RATE_DECISION" in events
    assert "US_NONFARM_PAYROLLS_RELEASE" in events
