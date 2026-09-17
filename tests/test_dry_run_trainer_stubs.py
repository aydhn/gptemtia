"""Test suite for Phase 138 Dry-Run Trainer Stubs."""

from advanced_baseline_ml_models.baseline_ml_model_config import (
    get_default_baseline_ml_model_profile,
)
from advanced_baseline_ml_models.dry_run_trainer_stubs import (
    build_dry_run_trainer_stub_registry,
    dry_run_train_stub,
    summarize_dry_run_trainer_stubs,
)


def test_build_dry_run_trainer_stub_registry():
    profile = get_default_baseline_ml_model_profile()
    df, summary = build_dry_run_trainer_stub_registry(profile)

    assert len(df) == 10
    assert summary["total_trainer_stubs"] == 10
    assert summary["all_real_training_blocked"] is True
    assert summary["all_fit_blocked"] is True
    assert summary["all_predict_blocked"] is True
    assert summary["all_active_stubs"] is True
    assert summary["non_signal"] is True
    assert bool((df["real_training_executed"] == False).all())
    assert bool((df["model_fit_executed"] == False).all())
    assert bool((df["model_predict_executed"] == False).all())


def test_dry_run_train_stub_execution():
    res = dry_run_train_stub({
        "model_family": "random_forest",
        "plan_name": "test_dry_run_plan",
    })
    assert res["dry_run"] is True
    assert res["real_training_executed"] is False
    assert res["model_fit_executed"] is False
    assert res["model_predict_executed"] is False
    assert res["target_label_generated"] is False
    assert res["artifact_persisted"] is False
    assert res["model_registry_written"] is False
    assert res["execution_status"] == "no_real_training_executed"
    assert res["status"] == "execution_blocked_by_policy"
