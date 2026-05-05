import pytest
import pandas as pd
from asset_profiles.asset_profile_quality import (
    check_asset_profile_missing_columns,
    check_group_member_coverage,
    check_group_feature_nan_ratio,
    build_asset_profile_quality_report,
)


def test_check_asset_profile_missing_columns():
    df = pd.DataFrame({"asset_behavior_score": [1]})
    res = check_asset_profile_missing_columns(df)
    assert "missing_columns" in res
    assert "asset_behavior_regime_label" in res["missing_columns"]
    assert "asset_behavior_score" not in res["missing_columns"]


def test_check_group_member_coverage():
    res = check_group_member_coverage("metals", 5, 3)
    assert res["coverage_ratio"] == 0.6
    assert res["passed_minimum_coverage"] is True

    res2 = check_group_member_coverage("metals", 5, 1)
    assert res2["passed_minimum_coverage"] is False


def test_check_group_feature_nan_ratio():
    df = pd.DataFrame({"A": [1, None, None], "B": [1, 2, None]})
    res = check_group_feature_nan_ratio(df, max_nan_ratio=0.4)
    assert res["total_nan_ratio"] == 0.5
    assert not res["passed_nan_check"]


def test_build_asset_profile_quality_report():
    df = pd.DataFrame(
        {
            "asset_behavior_score": [1],
            "asset_behavior_regime_label": ["x"],
            "asset_group_regime_label": ["y"],
            "asset_relative_strength_regime_label": ["z"],
            "rs_vs_group_21": [0.1],
        }
    )

    report = build_asset_profile_quality_report(df, {"warnings": []})
    assert report["passed"] is True
    assert report["relative_strength_available"] is True
