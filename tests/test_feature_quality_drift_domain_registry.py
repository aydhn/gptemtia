import pytest
from advanced_feature_quality_drift.feature_quality_drift_domain_registry import build_feature_quality_drift_domain_registry


def test_build_feature_quality_drift_domain_registry():
    df, summary = build_feature_quality_drift_domain_registry()
    assert not df.empty
    assert summary["total_domains"] >= 20
    assert summary["current_phase"] == 123
    assert summary["target_final_phase"] == 160
    assert summary["next_phase"] == 124
    assert summary["non_signal"] is True

    domains = list(df["domain"])
    assert "missingness_domain" in domains
    assert "infinite_value_domain" in domains
    assert "distribution_drift_domain" in domains
    assert "rolling_stability_domain" in domains
    assert "factor_quality_domain" in domains
