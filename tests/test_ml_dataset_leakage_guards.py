"""Test suite for Phase 137 ML Dataset Leakage Guards."""

import pytest
from advanced_ml_dataset_registry.ml_dataset_leakage_guards import (
    build_ml_dataset_leakage_guard_registry,
    validate_ml_dataset_leakage_fields,
    validate_no_negative_shift_usage,
    summarize_ml_dataset_leakage_guards,
)


def test_build_leakage_guards():
    df, summary = build_ml_dataset_leakage_guard_registry()
    assert not df.empty
    assert summary["total_leakage_guards"] >= 3
    assert summary["non_signal"] is True


def test_validate_negative_shift():
    clean = validate_no_negative_shift_usage("df['ret'] = df['close'].pct_change()")
    assert clean["valid"] is True

    dirty = validate_no_negative_shift_usage("df['target'] = df['close'].shift(-1)")
    assert dirty["valid"] is False
    assert any("shift(-" in err for err in dirty["issues"])


def test_validate_leakage_fields():
    v_clean = validate_ml_dataset_leakage_fields(["timestamp_utc", "ml_feature_rsi"])
    assert v_clean["valid"] is True

    v_leak = validate_ml_dataset_leakage_fields(["timestamp_utc", "future_return_1d"])
    assert v_leak["valid"] is False
