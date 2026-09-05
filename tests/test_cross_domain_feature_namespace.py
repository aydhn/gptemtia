"""Unit tests for Phase 119 cross-domain feature namespace standards."""

import pytest
import pandas as pd
from advanced_cross_asset_alignment.cross_domain_feature_namespace import (
    build_namespaced_feature_name,
    validate_namespaced_feature_name,
    build_cross_domain_feature_namespace_registry,
    build_feature_namespace_registry,
    FORBIDDEN_WORDS,
)


def test_build_namespaced_feature_name():
    name = build_namespaced_feature_name("fx", "EUR/USD", "sma", "20")
    assert name == "fx_eur_usd_sma_20"

    name2 = build_namespaced_feature_name("commodity", "XAU/USD", "bb_upper", "w20")
    assert name2 == "commodity_xau_usd_bb_upper_w20"


def test_validate_namespaced_feature_name():
    # Valid
    val1 = validate_namespaced_feature_name("fx_eur_usd_sma_20")
    assert val1["is_valid"] is True

    # Invalid prefix
    val2 = validate_namespaced_feature_name("crypto_btc_usd_sma_20")
    assert val2["is_valid"] is False

    # Forbidden word
    val3 = validate_namespaced_feature_name("fx_eur_usd_buy_signal_w20")
    assert val3["is_valid"] is False
    assert "signal" in val3["forbidden_words_found"] or "buy" in val3["forbidden_words_found"]


def test_namespace_registry():
    df, summary = build_cross_domain_feature_namespace_registry()
    assert len(df) == 8
    assert summary["all_valid"] is True
    assert summary["non_signal"] is True

    # Check alias
    df2, s2 = build_feature_namespace_registry()
    assert len(df2) == 8
    assert s2["all_valid"] is True
