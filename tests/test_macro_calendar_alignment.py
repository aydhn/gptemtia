"""Unit tests for Phase 119 Macro - Calendar alignment registry."""

import pytest
import pandas as pd
from advanced_cross_asset_alignment.macro_calendar_alignment import build_macro_calendar_alignment_registry


def test_macro_calendar_alignment_registry():
    df, summary = build_macro_calendar_alignment_registry()
    assert len(df) == 5
    assert summary["total_alignments"] == 5
    assert summary["all_non_signal"] is True
    assert summary["status"] == "READY"

    indicators = set(df["macro_indicator"])
    assert "FED_POLICY_RATE" in indicators
    assert "US_NONFARM_PAYROLLS" in indicators
