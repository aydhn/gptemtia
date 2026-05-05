import pytest
import pandas as pd
from asset_profiles.asset_profile_config import AssetProfile
from asset_profiles.asset_class_regime import (
    classify_asset_behavior_regime,
    classify_group_regime,
    classify_relative_strength_regime,
    classify_correlation_regime,
)


@pytest.fixture
def mock_profile():
    return AssetProfile(
        asset_class="metals",
        name="Metals",
        description="Test",
        preferred_timeframes=("1d",),
        core_feature_sets=("trend",),
    )


def test_classify_asset_behavior_regime(mock_profile):
    idx = pd.date_range("2023-01-01", periods=3)
    df = pd.DataFrame(
        {
            "asset_volume_confidence_score": [0.8, 0.3, 0.9],
            "asset_risk_context_score": [0.2, 0.5, 0.8],
        },
        index=idx,
    )

    regime, summary = classify_asset_behavior_regime(df, mock_profile)
    assert "asset_behavior_regime_label" in regime.columns
    assert (
        regime["asset_behavior_regime_label"].iloc[1] == "asset_low_volume_confidence"
    )
    assert regime["asset_behavior_regime_label"].iloc[2] == "asset_high_gap_risk"


def test_classify_group_regime():
    idx = pd.date_range("2023-01-01", periods=3)
    df = pd.DataFrame(
        {
            "group_metals_momentum_63": [0.01, 0.1, -0.1],
            "group_metals_dispersion_high": [0, 1, 0],
        },
        index=idx,
    )

    regime, summary = classify_group_regime(df, "metals")
    assert "asset_group_regime_label" in regime.columns
    assert regime["asset_group_regime_label"].iloc[0] == "group_range"
    assert regime["asset_group_regime_label"].iloc[1] == "group_uptrend"
    assert regime["asset_group_regime_label"].iloc[2] == "group_downtrend"


def test_classify_relative_strength_regime():
    idx = pd.date_range("2023-01-01", periods=3)
    df = pd.DataFrame(
        {"rs_is_group_leader": [1, 0, 0], "rs_is_group_laggard": [0, 0, 1]}, index=idx
    )

    regime, summary = classify_relative_strength_regime(df)
    assert "asset_relative_strength_regime_label" in regime.columns
    assert (
        regime["asset_relative_strength_regime_label"].iloc[0] == "asset_group_leader"
    )
    assert (
        regime["asset_relative_strength_regime_label"].iloc[1] == "asset_group_neutral"
    )
    assert (
        regime["asset_relative_strength_regime_label"].iloc[2] == "asset_group_laggard"
    )


def test_classify_correlation_regime():
    idx = pd.date_range("2023-01-01", periods=3)
    df = pd.DataFrame({"corr_symbol_group_90": [0.8, 0.5, 0.2]}, index=idx)

    regime, summary = classify_correlation_regime(df)
    assert "asset_correlation_regime_label" in regime.columns
    assert (
        regime["asset_correlation_regime_label"].iloc[0]
        == "asset_high_group_correlation"
    )
    assert (
        regime["asset_correlation_regime_label"].iloc[1] == "asset_normal_correlation"
    )
    assert regime["asset_correlation_regime_label"].iloc[2] == "asset_group_decoupling"
