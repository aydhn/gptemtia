import pytest
import pandas as pd
import numpy as np
from asset_profiles.asset_profile_config import AssetProfile
from asset_profiles.asset_behavior_features import build_asset_behavior_features


@pytest.fixture
def mock_profile():
    return AssetProfile(
        asset_class="metals",
        name="Metals",
        description="Test",
        preferred_timeframes=("1d",),
        core_feature_sets=("trend",),
        macro_sensitivity="high",
        gap_risk="medium",
        trend_following_suitability="high",
    )


def test_build_asset_behavior_features(mock_profile):
    df = pd.DataFrame(
        {
            "regime_primary_label": ["uptrend", "range", "high_volatility"],
            "volume_is_usable": [1, 1, 0],
        },
        index=pd.date_range("2023-01-01", periods=3),
    )

    features, summary = build_asset_behavior_features(df, mock_profile, "TEST", "1d")

    assert not features.empty
    assert "asset_behavior_score" in features.columns
    assert "asset_profile_label" in features.columns

    # Check bounds
    assert features["asset_trend_suitability_score"].between(0, 1).all()
    assert features["asset_behavior_score"].between(0, 1).all()

    assert summary["rows"] == 3


def test_build_asset_behavior_features_missing_cols(mock_profile):
    # Should not crash with empty or missing expected columns
    df = pd.DataFrame(
        {"some_col": [1, 2, 3]}, index=pd.date_range("2023-01-01", periods=3)
    )
    features, summary = build_asset_behavior_features(df, mock_profile, "TEST", "1d")

    assert not features.empty
    assert "asset_behavior_score" in features.columns
    assert "asset_profile_label" in features.columns
    assert features["asset_profile_label"].iloc[0] == "Metals"
