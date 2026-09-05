import pytest
from advanced_feature_quality_drift.factor_family_quality import (
    build_factor_family_quality_report,
    summarize_factor_family_quality,
)


def test_factor_family_quality_report():
    df, summary = build_factor_family_quality_report()
    assert not df.empty
    assert summary["total_families"] == 10
    assert summary["passed_families"] == 10
    assert summary["status"] == "diagnostic_pass"

    families = list(df["family_id"])
    expected = [
        "trend", "momentum", "volatility", "mean_reversion",
        "returns", "quote_microstructure", "macro_context",
        "calendar_event", "news_attention", "cross_asset_context"
    ]
    for ef in expected:
        assert ef in families
