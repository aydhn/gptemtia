"""Test suite for Phase 138 Baseline Model Training Plans."""

from advanced_baseline_ml_models.baseline_ml_model_config import (
    get_default_baseline_ml_model_profile,
)
from advanced_baseline_ml_models.baseline_model_training_plans import (
    build_baseline_model_training_plan_registry,
    summarize_baseline_model_training_plans,
)


def test_build_baseline_model_training_plan_registry():
    profile = get_default_baseline_ml_model_profile()
    df, summary = build_baseline_model_training_plan_registry(profile)

    assert len(df) == 10
    assert summary["total_training_plans"] == 10
    assert summary["all_contract_only"] is True
    assert summary["zero_real_training_allowed"] is True
    assert summary["all_dry_run_allowed"] is True
    assert summary["zero_target_label_required"] is True
    assert summary["zero_artifact_persistence"] is True
    assert summary["all_manual_review_required"] is True
    assert summary["non_signal"] is True
