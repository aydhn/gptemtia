"""Tests for Cross-Asset Regime Validation Acceptance."""

from advanced_regime_validation_acceptance.cross_asset_regime_validation_acceptance import (
    build_cross_asset_regime_validation_acceptance_report,
    summarize_cross_asset_regime_validation_acceptance,
)


def test_cross_asset_regime_validation_acceptance():
    df, summary = build_cross_asset_regime_validation_acceptance_report()
    assert not df.empty
    assert summary["all_passed"] is True
    assert summary["component"] == "phase_131_cross_asset_regime"
    assert summary["non_signal"] is True

    s_df = summarize_cross_asset_regime_validation_acceptance(df)
    assert s_df["all_passed"] is True
