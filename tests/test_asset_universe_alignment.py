"""Unit tests for Phase 119 asset universe alignment."""

import pytest
import pandas as pd
from advanced_cross_asset_alignment.asset_universe_alignment import (
    build_asset_universe_alignment_registry,
    build_asset_universe_registry,
    DEFAULT_UNIVERSES,
)


def test_asset_universe_registry():
    df, summary = build_asset_universe_alignment_registry()
    assert len(df) == 5
    assert summary["total_universes"] == 5
    assert summary["non_signal"] is True

    # Check both alias and original name
    df2, s2 = build_asset_universe_registry()
    assert len(df2) == 5
    assert s2["total_universes"] == 5


def test_asset_universe_symbols():
    df, _ = build_asset_universe_alignment_registry()
    symbols = set(df["canonical_symbol"])
    assert "EUR/USD" in symbols
    assert "USD/TRY" in symbols
    assert "XAU/USD" in symbols
    assert "WTI_CRUDE_CONTINUOUS_PLACEHOLDER" in symbols
    assert "NATURAL_GAS_CONTINUOUS_PLACEHOLDER" in symbols
