"""Unit tests for Phase 119 cross-asset alignment domain registry."""

import pytest
import pandas as pd
from advanced_cross_asset_alignment.cross_asset_alignment_domain_registry import (
    build_cross_asset_alignment_domain_registry,
    DOMAIN_DEFINITIONS,
)


def test_domain_registry_completeness():
    assert len(DOMAIN_DEFINITIONS) == 28
    df, summary = build_cross_asset_alignment_domain_registry()
    assert len(df) == 28
    assert summary["total_domains"] == 28
    assert summary["non_signal"] is True
    assert summary["status"] == "READY"


def test_domain_registry_columns():
    df, _ = build_cross_asset_alignment_domain_registry()
    expected_cols = ["domain_id", "domain_label", "domain_name", "description", "required_outputs", "non_signal"]
    for c in expected_cols:
        assert c in df.columns
    assert bool(df["non_signal"].all()) is True
