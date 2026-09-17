"""Test suite for Phase 138 Baseline Model Output Contracts."""

from advanced_baseline_ml_models.baseline_ml_model_config import (
    get_default_baseline_ml_model_profile,
)
from advanced_baseline_ml_models.baseline_model_output_contracts import (
    build_baseline_model_output_contract_registry,
    summarize_baseline_model_output_contracts,
)


def test_build_baseline_model_output_contract_registry():
    profile = get_default_baseline_ml_model_profile()
    df, summary = build_baseline_model_output_contract_registry(profile)

    assert len(df) == 10
    assert summary["total_output_contracts"] == 10
    assert summary["all_predictions_prohibited"] is True
    assert summary["all_probabilities_prohibited"] is True
    assert summary["all_class_labels_prohibited"] is True
    assert summary["all_regression_prohibited"] is True
    assert summary["all_trade_signals_prohibited"] is True
    assert summary["all_metrics_prohibited"] is True
    assert summary["non_signal"] is True
    assert bool((df["prediction_output_allowed"] == False).all())
    assert bool((df["trade_signal_allowed"] == False).all())
