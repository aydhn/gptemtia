import pandas as pd
import pytest
from advanced_feature_quality_drift.cross_asset_feature_quality import (
    build_cross_asset_feature_quality_report,
    summarize_cross_asset_feature_quality,
)


def test_cross_asset_feature_quality_clean():
    df, summary = build_cross_asset_feature_quality_report()
    assert not df.empty
    assert summary["failed_checks"] == 0
    assert summary["status"] == "diagnostic_pass"


def test_cross_asset_feature_quality_forbidden_target():
    bad_df = pd.DataFrame({
        "timestamp": ["2026-01-01"],
        "target_return": [0.05],
    })
    df, summary = build_cross_asset_feature_quality_report(df=bad_df)
    assert summary["failed_checks"] > 0
    assert summary["status"] == "diagnostic_fail"
    assert summary["manual_review_required"] is True
