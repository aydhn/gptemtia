"""Tests for Fusion Feature Matrix Contracts."""

import pandas as pd
from advanced_feature_fusion.fusion_feature_matrix_contracts import (
    get_fusion_feature_matrix_contracts,
    get_fusion_feature_matrix_contracts_summary,
    validate_fusion_feature_matrix_contract,
)


def test_matrix_contracts_registry():
    contracts = get_fusion_feature_matrix_contracts()
    assert len(contracts) >= 4
    summary = get_fusion_feature_matrix_contracts_summary()
    assert summary["contract_count"] == len(contracts)
    assert summary["zero_signal_mandate"] is True


def test_validate_valid_matrix():
    times = pd.date_range("2025-01-01 10:00:00", periods=5, freq="1h", tz="UTC")
    valid_df = pd.DataFrame({
        "timestamp": times,
        "feature_a": [1, 2, 3, 4, 5],
    })
    violations = validate_fusion_feature_matrix_contract(valid_df)
    assert len(violations) == 0


def test_validate_matrix_violations():
    # Forbidden signal column
    bad_df = pd.DataFrame({
        "timestamp": pd.date_range("2025-01-01 10:00:00", periods=3, freq="1h", tz="UTC"),
        "target_return": [0.01, 0.02, -0.01],
    })
    violations = validate_fusion_feature_matrix_contract(bad_df)
    assert len(violations) > 0
