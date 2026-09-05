"""Unit tests for Phase 119 FX - Commodity alignment registry."""

import pytest
import pandas as pd
from advanced_cross_asset_alignment.fx_commodity_alignment import build_fx_commodity_alignment_registry


def test_fx_commodity_alignment_registry():
    df, summary = build_fx_commodity_alignment_registry()
    assert len(df) == 3
    assert summary["total_alignments"] == 3
    assert summary["all_non_signal"] is True
    assert summary["status"] == "READY"

    pairs = set(df["fx_pair"])
    assert "EUR/USD" in pairs
    assert "USD/TRY" in pairs
    assert "USD/CAD" in pairs
