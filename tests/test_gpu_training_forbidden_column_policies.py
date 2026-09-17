"""Test suite for Phase 139 GPU Training Forbidden Column Policies."""

from advanced_gpu_training_governance.gpu_training_governance_config import (
    get_default_gpu_training_governance_profile,
)
from advanced_gpu_training_governance.gpu_training_forbidden_column_policies import (
    FORBIDDEN_COLUMNS_LIST,
    build_gpu_training_forbidden_column_policy_registry,
    summarize_gpu_training_forbidden_column_policies,
    validate_gpu_training_forbidden_columns,
)


def test_build_gpu_training_forbidden_column_policy_registry():
    profile = get_default_gpu_training_governance_profile()
    df, summary = build_gpu_training_forbidden_column_policy_registry(profile)

    assert len(df) == len(FORBIDDEN_COLUMNS_LIST)
    assert summary["total_forbidden_columns"] == len(df)
    assert summary["all_enforced"] is True
    assert summary["non_signal"] is True


def test_validate_gpu_training_forbidden_columns():
    clean_cols = ["date", "symbol", "close", "volume", "ema_20", "atr_14"]
    res_clean = validate_gpu_training_forbidden_columns(clean_cols)
    assert res_clean["is_clean"] is True
    assert len(res_clean["violating_columns"]) == 0
    assert res_clean["status"] == "PASS"

    dirty_cols = ["date", "signal", "buy", "target", "label", "prediction", "sentiment"]
    res_dirty = validate_gpu_training_forbidden_columns(dirty_cols)
    assert res_dirty["is_clean"] is False
    assert len(res_dirty["violating_columns"]) == 6
    assert res_dirty["status"] == "FAIL_FORBIDDEN_COLUMNS"
