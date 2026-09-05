"""Unit tests for Phase 119 Commodity - Calendar alignment registry."""

import pytest
import pandas as pd
from advanced_cross_asset_alignment.commodity_calendar_alignment import build_commodity_calendar_alignment_registry


def test_commodity_calendar_alignment_registry():
    df, summary = build_commodity_calendar_alignment_registry()
    assert len(df) == 3
    assert summary["total_alignments"] == 3
    assert summary["all_non_signal"] is True
    assert summary["status"] == "READY"

    events = set(df["calendar_event"])
    assert "EIA_CRUDE_INVENTORY_RELEASE" in events
    assert "EIA_NATURAL_GAS_STORAGE_RELEASE" in events
