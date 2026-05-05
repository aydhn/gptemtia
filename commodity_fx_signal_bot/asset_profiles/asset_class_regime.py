import pandas as pd
import numpy as np
from asset_profiles.asset_profile_config import AssetProfile


def classify_asset_behavior_regime(
    df: pd.DataFrame,
    asset_profile: AssetProfile,
) -> tuple[pd.DataFrame, dict]:
    """Classify the current asset behavior regime based on profile and context."""
    features = pd.DataFrame(index=df.index)
    summary = {"warnings": []}

    if df.empty:
        return features, summary

    labels = pd.Series("asset_unknown", index=df.index)
    confidences = pd.Series(0.0, index=df.index)

    # Simple heuristic to map existing features to a single behavior label
    # E.g. macro sensitive pressure, low volume risk

    if "asset_volume_confidence_score" in df.columns:
        low_vol = df["asset_volume_confidence_score"] < 0.4
        labels = np.where(low_vol, "asset_low_volume_confidence", labels)
        confidences = np.where(
            low_vol, 1.0 - df["asset_volume_confidence_score"], confidences
        )

    if "asset_risk_context_score" in df.columns:
        high_risk = df["asset_risk_context_score"] > 0.7
        # Overwrite if higher confidence or specific priority
        labels = np.where(
            high_risk & (labels == "asset_unknown"), "asset_high_gap_risk", labels
        )
        confidences = np.where(
            high_risk,
            np.maximum(confidences, df["asset_risk_context_score"]),
            confidences,
        )

    features["asset_behavior_regime_label"] = labels
    features["asset_profile_confidence"] = confidences

    return features, summary


def classify_group_regime(
    group_df: pd.DataFrame,
    asset_class: str,
) -> tuple[pd.DataFrame, dict]:
    """Classify the regime of the entire group."""
    features = pd.DataFrame(index=group_df.index)
    summary = {"warnings": []}

    if group_df.empty:
        return features, summary

    labels = pd.Series("group_range", index=group_df.index)
    confidences = pd.Series(0.5, index=group_df.index)

    mom_col = f"group_{asset_class}_momentum_63"
    disp_col = f"group_{asset_class}_dispersion_high"
    vol_col = f"group_{asset_class}_volatility_63"

    if mom_col in group_df.columns:
        uptrend = group_df[mom_col] > 0.05
        downtrend = group_df[mom_col] < -0.05

        labels = np.where(uptrend, "group_uptrend", labels)
        labels = np.where(downtrend, "group_downtrend", labels)

        # Base confidence on momentum magnitude
        conf = np.clip(np.abs(group_df[mom_col]) * 5, 0, 1)
        confidences = np.where(uptrend | downtrend, conf, confidences)

    if disp_col in group_df.columns:
        high_disp = group_df[disp_col] == 1
        labels = np.where(
            high_disp & (labels == "group_range"), "group_dispersion_high", labels
        )

    # High vol overrides range
    if vol_col in group_df.columns:
        # Assuming we have some percentile or absolute threshold for high vol.
        # For simplicity, if it's top quartile of its rolling 252 (if we computed it)
        # Here we just use a placeholder threshold or rely on events later
        pass

    features["asset_group_regime_label"] = labels
    features["group_regime_confidence"] = confidences

    return features, summary


def classify_relative_strength_regime(
    rs_df: pd.DataFrame,
) -> tuple[pd.DataFrame, dict]:
    """Classify relative strength regime (leader/laggard)."""
    features = pd.DataFrame(index=rs_df.index)
    summary = {"warnings": []}

    if rs_df.empty:
        return features, summary

    labels = pd.Series("asset_group_neutral", index=rs_df.index)

    if "rs_is_group_leader" in rs_df.columns and "rs_is_group_laggard" in rs_df.columns:
        labels = np.where(
            rs_df["rs_is_group_leader"] == 1, "asset_group_leader", labels
        )
        labels = np.where(
            rs_df["rs_is_group_laggard"] == 1, "asset_group_laggard", labels
        )

    features["asset_relative_strength_regime_label"] = labels
    return features, summary


def classify_correlation_regime(
    corr_df: pd.DataFrame,
) -> tuple[pd.DataFrame, dict]:
    """Classify correlation regime."""
    features = pd.DataFrame(index=corr_df.index)
    summary = {"warnings": []}

    if corr_df.empty:
        return features, summary

    labels = pd.Series("asset_normal_correlation", index=corr_df.index)

    # Find symbol_group_corr col
    corr_cols = [c for c in corr_df.columns if "corr_symbol_group" in c]
    if corr_cols:
        col = corr_cols[0]
        high_corr = corr_df[col] > 0.7
        low_corr = corr_df[col] < 0.3

        labels = np.where(high_corr, "asset_high_group_correlation", labels)
        labels = np.where(low_corr, "asset_group_decoupling", labels)

    features["asset_correlation_regime_label"] = labels
    return features, summary
