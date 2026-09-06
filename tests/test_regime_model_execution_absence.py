"""Tests for Regime Model Execution Absence."""

from advanced_regime_validation_acceptance.regime_model_execution_absence import (
    build_regime_model_execution_absence_report,
    validate_no_model_execution_flags,
    validate_no_model_execution_text,
    summarize_model_execution_absence,
)


def test_model_execution_absence():
    df, summary = build_regime_model_execution_absence_report()
    assert not df.empty
    assert summary["all_zero_execution"] is True

    s_df = summarize_model_execution_absence(df)
    assert s_df["all_zero_execution"] is True

    # Flags validation
    clean_flags = {
        "model_training_executed": False,
        "model_fit_executed": False,
        "clustering_executed": False,
    }
    assert validate_no_model_execution_flags(clean_flags)["passed"] is True

    dirty_flags = {
        "model_training_executed": True,
        "model_fit_executed": False,
    }
    res_flags = validate_no_model_execution_flags(dirty_flags)
    assert res_flags["passed"] is False
    assert "model_training_executed" in res_flags["violating_flags"]

    # Text validation
    assert validate_no_model_execution_text("Descriptive analysis without machine learning.")["passed"] is True
    assert validate_no_model_execution_text("The model trained on historical data.")["passed"] is False
