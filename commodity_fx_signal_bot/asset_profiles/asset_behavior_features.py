import pandas as pd
import numpy as np
from asset_profiles.asset_profile_config import AssetProfile


def calculate_asset_trend_suitability_score(
    df: pd.DataFrame, asset_profile: AssetProfile
) -> pd.Series:
    """Calculate trend suitability score based on profile and current features."""
    base_score = 0.5
    if asset_profile.trend_following_suitability == "high":
        base_score = 0.8
    elif asset_profile.trend_following_suitability == "low":
        base_score = 0.2

    score = pd.Series(base_score, index=df.index)

    if "regime_primary_label" in df.columns:
        trend_regimes = (
            df["regime_primary_label"].astype(str).str.contains("uptrend|downtrend")
        )
        score = np.where(trend_regimes, np.clip(score + 0.1, 0, 1), score)

    return pd.Series(score, index=df.index, name="asset_trend_suitability_score")


def calculate_asset_reversion_suitability_score(
    df: pd.DataFrame, asset_profile: AssetProfile
) -> pd.Series:
    """Calculate mean reversion suitability score."""
    base_score = 0.5
    if asset_profile.mean_reversion_suitability == "high":
        base_score = 0.8
    elif asset_profile.mean_reversion_suitability == "low":
        base_score = 0.2

    score = pd.Series(base_score, index=df.index)

    if "regime_primary_label" in df.columns:
        range_regimes = df["regime_primary_label"].astype(str).str.contains("range")
        score = np.where(range_regimes, np.clip(score + 0.1, 0, 1), score)

    return pd.Series(score, index=df.index, name="asset_reversion_suitability_score")


def calculate_asset_breakout_suitability_score(
    df: pd.DataFrame, asset_profile: AssetProfile
) -> pd.Series:
    """Calculate breakout suitability score."""
    base_score = 0.5
    if asset_profile.breakout_suitability == "high":
        base_score = 0.8
    elif asset_profile.breakout_suitability == "low":
        base_score = 0.2

    score = pd.Series(base_score, index=df.index)

    if "regime_primary_label" in df.columns:
        compression = df["regime_primary_label"].astype(str).str.contains("compression")
        score = np.where(compression, np.clip(score + 0.1, 0, 1), score)

    return pd.Series(score, index=df.index, name="asset_breakout_suitability_score")


def calculate_asset_risk_context_score(
    df: pd.DataFrame, asset_profile: AssetProfile
) -> pd.Series:
    """Calculate overall risk context score (1 = high risk, 0 = low risk)."""
    base_score = 0.5
    if asset_profile.gap_risk == "high" or asset_profile.typical_volatility == "high":
        base_score = 0.8
    elif asset_profile.gap_risk == "low" and asset_profile.typical_volatility == "low":
        base_score = 0.2

    score = pd.Series(base_score, index=df.index)

    if "regime_primary_label" in df.columns:
        high_vol = (
            df["regime_primary_label"].astype(str).str.contains("high_volatility")
        )
        score = np.where(high_vol, np.clip(score + 0.1, 0, 1), score)

    return pd.Series(score, index=df.index, name="asset_risk_context_score")


def calculate_asset_volume_confidence_score(
    df: pd.DataFrame, asset_profile: AssetProfile
) -> pd.Series:
    """Calculate volume confidence score."""
    base_score = 0.5
    if asset_profile.volume_reliability == "high":
        base_score = 0.9
    elif asset_profile.volume_reliability == "low":
        base_score = 0.2

    score = pd.Series(base_score, index=df.index)

    if "volume_is_usable" in df.columns:
        score = np.where(df["volume_is_usable"] == 1, score, np.clip(score - 0.2, 0, 1))

    return pd.Series(score, index=df.index, name="asset_volume_confidence_score")


def calculate_asset_behavior_score(
    df: pd.DataFrame, asset_profile: AssetProfile
) -> pd.Series:
    """Calculate composite asset behavior score."""
    trend = calculate_asset_trend_suitability_score(df, asset_profile)
    risk = calculate_asset_risk_context_score(df, asset_profile)
    # Higher behavior score means generally better behaving / more predictable
    score = np.clip((trend + (1.0 - risk)) / 2.0, 0, 1)
    return pd.Series(score, index=df.index, name="asset_behavior_score")


def build_asset_behavior_features(
    df: pd.DataFrame,
    asset_profile: AssetProfile,
    symbol: str,
    timeframe: str,
) -> tuple[pd.DataFrame, dict]:
    """Build all asset behavior features for a single symbol."""

    features = pd.DataFrame(index=df.index)
    summary = {"warnings": []}

    if df.empty:
        summary["warnings"].append(f"Empty dataframe provided for {symbol}")
        return features, summary

    features["asset_behavior_score"] = calculate_asset_behavior_score(df, asset_profile)
    features["asset_trend_suitability_score"] = calculate_asset_trend_suitability_score(
        df, asset_profile
    )
    features["asset_reversion_suitability_score"] = (
        calculate_asset_reversion_suitability_score(df, asset_profile)
    )
    features["asset_breakout_suitability_score"] = (
        calculate_asset_breakout_suitability_score(df, asset_profile)
    )
    features["asset_risk_context_score"] = calculate_asset_risk_context_score(
        df, asset_profile
    )
    features["asset_volume_confidence_score"] = calculate_asset_volume_confidence_score(
        df, asset_profile
    )

    features["asset_profile_label"] = asset_profile.name

    macro_map = {"low": 0.2, "medium": 0.5, "high": 0.8, "very_high": 1.0}
    features["asset_macro_sensitivity_score"] = macro_map.get(
        asset_profile.macro_sensitivity, 0.5
    )

    gap_map = {"low": 0.2, "medium": 0.5, "high": 0.8}
    features["asset_gap_risk_score"] = gap_map.get(asset_profile.gap_risk, 0.5)

    summary["rows"] = len(features)
    summary["columns"] = list(features.columns)

    return features, summary
