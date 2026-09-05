"""Unit tests for Phase 119 cross-domain feature matrix builder."""

import pytest
import pandas as pd
from advanced_cross_asset_alignment.cross_domain_feature_matrix import (
    build_cross_domain_feature_matrix_placeholder,
    build_aligned_feature_matrix_from_contract,
)


def test_placeholder_matrix_structure():
    df, summary = build_cross_domain_feature_matrix_placeholder()
    assert len(df) == 10
    assert summary["total_rows"] == 10
    assert summary["is_non_signal"] is True
    assert summary["non_signal"] is True
    assert summary["status"] == "READY"

    # Required metadata columns
    assert "normalized_timestamp" in df.columns
    assert "canonical_symbol" in df.columns

    # No target or prediction columns
    for col in df.columns:
        assert "signal" not in col.lower()
        assert "target" not in col.lower()
        assert "prediction" not in col.lower()


def test_build_matrix_from_contract():
    base_df = pd.DataFrame({
        "normalized_timestamp": ["2026-09-01T10:00:00Z", "2026-09-01T11:00:00Z"],
        "canonical_symbol": ["EUR/USD", "EUR/USD"],
        "fx_feature": [1.0, 2.0],
    })
    aligned = build_aligned_feature_matrix_from_contract(
        base_df=base_df,
        contract_name="test_contract",
        additional_domain_dfs={},
    )
    assert len(aligned) == 2
    assert "fx_feature" in aligned.columns
