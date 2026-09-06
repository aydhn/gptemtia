"""Test suite for Phase 136 GPU ML Runtime Validation."""

import pytest
from advanced_gpu_ml_runtime.gpu_ml_runtime_validation import (
    build_gpu_ml_runtime_validation_report,
    validate_no_forbidden_ml_runtime_claims,
)


def test_validate_no_forbidden_ml_runtime_claims():
    clean_text = "Phase 136 hardware discovery completed without training."
    res = validate_no_forbidden_ml_runtime_claims(text=clean_text)
    assert res["is_clean"] is True
    assert len(res["violations"]) == 0

    dirty_text = "Generating a buy signal with official approval."
    res_dirty = validate_no_forbidden_ml_runtime_claims(text=dirty_text)
    assert res_dirty["is_clean"] is False
    assert len(res_dirty["violations"]) > 0


def test_build_gpu_ml_runtime_validation_report():
    df, summary = build_gpu_ml_runtime_validation_report()
    assert not df.empty
    assert summary["all_passed"] is True
    assert summary["passed_checks"] == summary["total_checks"]
    assert summary["non_signal"] is True
    assert summary["official_approval"] is False
    assert summary["production_ready"] is False
    assert summary["broker_ready"] is False
