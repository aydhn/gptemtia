"""Unit tests for Phase 119 Commodity - Macro alignment registry."""

import pytest
import pandas as pd
from advanced_cross_asset_alignment.commodity_macro_alignment import build_commodity_macro_alignment_registry


def test_commodity_macro_alignment_registry():
    df, summary = build_commodity_macro_alignment_registry()
    assert len(df) == 4
    assert summary["total_alignments"] == 4
    assert summary["all_non_signal"] is True
    assert summary["status"] == "READY"

    commodities = set(df["commodity_symbol"])
    assert "XAU/USD" in commodities
    assert "WTI_CRUDE_CONTINUOUS_PLACEHOLDER" in commodities
