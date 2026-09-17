"""Test suite for Phase 138 Baseline Model Families."""

from advanced_baseline_ml_models.baseline_ml_model_config import (
    get_default_baseline_ml_model_profile,
)
from advanced_baseline_ml_models.baseline_model_families import (
    BASELINE_MODEL_FAMILIES_DATA,
    build_baseline_model_family_registry,
    summarize_baseline_model_families,
)


def test_baseline_model_families_data():
    assert len(BASELINE_MODEL_FAMILIES_DATA) == 10
    family_ids = [f["family_id"] for f in BASELINE_MODEL_FAMILIES_DATA]
    assert "logistic_regression_baseline_contract" in family_ids
    assert "random_forest_baseline_contract" in family_ids
    assert "xgboost_baseline_contract" in family_ids



def test_build_baseline_model_family_registry():
    profile = get_default_baseline_ml_model_profile()
    df, summary = build_baseline_model_family_registry(profile)

    assert len(df) == 10
    assert summary["total_families"] == 10
    assert summary["all_contract_only"] is True
    assert summary["zero_real_training"] is True
    assert summary["zero_prediction"] is True
    assert bool((df["real_training_allowed"] == False).all())
    assert bool((df["model_fit_allowed"] == False).all())
    assert bool((df["model_predict_allowed"] == False).all())
    assert bool((df["non_signal"] == True).all())
