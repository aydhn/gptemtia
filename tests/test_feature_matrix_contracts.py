"""Unit tests for Phase 119 feature matrix contracts."""

import pytest
import pandas as pd
from advanced_cross_asset_alignment.feature_matrix_contracts import (
    build_feature_matrix_contract_registry,
    DEFAULT_FEATURE_MATRIX_CONTRACTS,
)


def test_feature_matrix_contracts_registry():
    assert len(DEFAULT_FEATURE_MATRIX_CONTRACTS) == 6
    df, summary = build_feature_matrix_contract_registry()
    assert len(df) == 6
    assert summary["total_contracts"] == 6
    assert summary["all_backward_only"] is True
    assert summary["all_non_signal"] is True
    assert summary["status"] == "READY"


def test_matrix_contract_fields():
    df, _ = build_feature_matrix_contract_registry()
    for _, row in df.iterrows():
        assert row["non_signal"] is True
        assert "backward" in row["no_lookahead_policy"] or "no_future" in row["no_lookahead_policy"]
