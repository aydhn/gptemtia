"""Test suite for Phase 139 GPU Training No-Lookahead Guards."""

import pandas as pd
from advanced_gpu_training_governance.gpu_training_governance_config import (
    get_default_gpu_training_governance_profile,
)
from advanced_gpu_training_governance.gpu_training_no_lookahead_guards import (
    build_gpu_training_no_lookahead_guard_registry,
    summarize_gpu_training_no_lookahead_guards,
    validate_gpu_training_no_lookahead_columns,
    validate_no_future_gpu_training_join,
)


def test_build_gpu_training_no_lookahead_guard_registry():
    profile = get_default_gpu_training_governance_profile()
    df, summary = build_gpu_training_no_lookahead_guard_registry(profile)

    assert len(df) == 3
    assert summary["total_guards"] == 3
    assert summary["all_enforced"] is True
    assert summary["non_signal"] is True


def test_validate_gpu_training_no_lookahead_columns():
    clean_cols = ["open", "high", "low", "close", "volume", "rsi_14"]
    res_clean = validate_gpu_training_no_lookahead_columns(clean_cols)
    assert res_clean["is_clean"] is True
    assert len(res_clean["violating_columns"]) == 0
    assert res_clean["status"] == "PASS"

    dirty_cols = ["open", "future_return", "shift(-1)", "lead_5", "target_next"]
    res_dirty = validate_gpu_training_no_lookahead_columns(dirty_cols)
    assert res_dirty["is_clean"] is False
    assert len(res_dirty["violating_columns"]) == 4
    assert res_dirty["status"] == "FAIL_LOOKAHEAD"


def test_validate_no_future_gpu_training_join():
    df_left = pd.DataFrame({"timestamp": ["2026-01-01", "2026-01-02", "2026-01-03"]})
    df_right_safe = pd.DataFrame({"timestamp": ["2026-01-01", "2026-01-02"]})
    df_right_future = pd.DataFrame({"timestamp": ["2026-01-01", "2026-01-05"]})

    res_safe = validate_no_future_gpu_training_join(df_left, df_right_safe, "timestamp", "timestamp")
    assert res_safe["is_valid"] is True
    assert res_safe["has_future_leakage"] is False

    res_future = validate_no_future_gpu_training_join(df_left, df_right_future, "timestamp", "timestamp")
    assert res_future["is_valid"] is False
    assert res_future["has_future_leakage"] is True
