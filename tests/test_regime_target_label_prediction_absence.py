"""Tests for Regime Target/Label/Prediction Absence."""

from advanced_regime_validation_acceptance.regime_target_label_prediction_absence import (
    build_regime_target_label_prediction_absence_report,
    validate_no_target_label_prediction_columns,
    validate_no_target_label_prediction_text,
    summarize_target_label_prediction_absence,
)


def test_target_label_prediction_absence():
    df, summary = build_regime_target_label_prediction_absence_report()
    assert not df.empty
    assert summary["all_absent"] is True

    s_df = summarize_target_label_prediction_absence(df)
    assert s_df["all_absent"] is True

    # Column validation
    clean_cols = ["regime_id", "persistence_days", "dispersion_metric"]
    assert validate_no_target_label_prediction_columns(clean_cols)["passed"] is True

    for term in ["target", "label", "prediction", "forecast"]:
        res = validate_no_target_label_prediction_columns(["asset_id", term])
        assert res["passed"] is False

    # Text validation
    assert validate_no_target_label_prediction_text("Offline descriptive regime analysis.")["passed"] is True
    assert validate_no_target_label_prediction_text("This is a supervised label generation step.")["passed"] is False
