"""Unit tests for Phase 119 FX - Macro alignment registry."""

import pytest
import pandas as pd
from advanced_cross_asset_alignment.fx_macro_alignment import build_fx_macro_alignment_registry


def test_fx_macro_alignment_registry():
    df, summary = build_fx_macro_alignment_registry()
    assert len(df) == 5
    assert summary["total_alignments"] == 5
    assert summary["all_non_signal"] is True
    assert summary["status"] == "READY"

    indicators = set(df["macro_indicator"])
    assert "FED_POLICY_RATE" in indicators
    assert "ECB_POLICY_RATE" in indicators
    assert "CBRT_POLICY_RATE" in indicators
    assert "DXY_PLACEHOLDER" in indicators
