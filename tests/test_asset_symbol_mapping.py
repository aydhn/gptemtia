"""Unit tests for Phase 119 asset symbol mapping and normalization."""

import pytest
import pandas as pd
from advanced_cross_asset_alignment.asset_symbol_mapping import (
    normalize_cross_asset_symbol,
    map_symbol_to_related_domains,
    build_asset_symbol_mapping_registry,
)


def test_symbol_normalization():
    assert normalize_cross_asset_symbol("eurusd") == "EUR/USD"
    assert normalize_cross_asset_symbol("EUR_USD") == "EUR/USD"
    assert normalize_cross_asset_symbol("usdtry") == "USD/TRY"
    assert normalize_cross_asset_symbol("xauusd") == "XAU/USD"
    assert normalize_cross_asset_symbol("GOLD") == "XAU/USD"
    assert normalize_cross_asset_symbol("wti") == "WTI_CRUDE_CONTINUOUS_PLACEHOLDER"
    assert normalize_cross_asset_symbol("unknown_symbol") == "UNKNOWN_SYMBOL"


def test_map_symbol_to_related_domains():
    res = map_symbol_to_related_domains("EUR/USD")
    assert res["canonical_symbol"] == "EUR/USD"
    assert "macro" in res["related_domains"]
    assert "calendar" in res["related_domains"]


def test_build_symbol_mapping_registry():
    df, summary = build_asset_symbol_mapping_registry()
    assert len(df) == 8
    assert summary["total_mappings"] == 8
    assert summary["non_signal"] is True
    assert summary["status"] == "READY"
