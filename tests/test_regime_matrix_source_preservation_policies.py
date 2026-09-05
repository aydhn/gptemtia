import pytest
from advanced_regime_matrix.regime_matrix_source_preservation_policies import (
    is_forbidden_preservation_action,
    assert_action_allowed_for_source,
    build_regime_matrix_source_preservation_policies,
)


def test_is_forbidden_preservation_action():
    assert is_forbidden_preservation_action("in_place_impute") is True
    assert is_forbidden_preservation_action("auto_drop_sparse_columns") is True
    assert is_forbidden_preservation_action("overwrite_raw_parquet") is True
    assert is_forbidden_preservation_action("read_only_feature_computation") is False


def test_assert_action_allowed_for_source():
    assert_action_allowed_for_source("read_only_feature_computation")
    with pytest.raises(PermissionError, match="Action 'in_place_impute' is strictly forbidden"):
        assert_action_allowed_for_source("in_place_impute")


def test_build_regime_matrix_source_preservation_policies():
    df, s = build_regime_matrix_source_preservation_policies()
    assert len(df) == 5
    assert s["total_policies"] == 5
    assert s["all_enforced"] is True
