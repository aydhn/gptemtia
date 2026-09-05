"""Phase 123 Feature Distribution Summary.

Produces descriptive statistics across feature columns (mean, standard deviation,
quantiles, skewness, kurtosis) to establish empirical baselines for drift monitoring.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_feature_quality_drift.feature_quality_drift_config import (
    FeatureQualityDriftProfile,
    get_default_feature_quality_drift_profile,
)


def build_distribution_summary(
    df: pd.DataFrame,
    feature_columns: List[str] | None = None,
) -> pd.DataFrame:
    """Calculate summary statistics for feature columns without mutating input DataFrame."""
    if df.empty:
        cols = feature_columns or ["placeholder_feature"]
        return pd.DataFrame([{
            "column": c,
            "count": 0,
            "mean": 0.0,
            "std": 0.0,
            "min": 0.0,
            "q25": 0.0,
            "median": 0.0,
            "q75": 0.0,
            "max": 0.0,
            "skewness": 0.0,
            "kurtosis": 0.0,
        } for c in cols])

    cols = feature_columns if feature_columns is not None else [
        c for c in df.columns if c not in ("timestamp", "asset_id", "symbol")
    ]
    records = []

    for col in cols:
        if col in df.columns and pd.api.types.is_numeric_dtype(df[col]):
            valid_vals = df[col].dropna()
            cnt = len(valid_vals)
            if cnt > 0:
                mean_val = float(valid_vals.mean())
                std_val = float(valid_vals.std()) if cnt > 1 else 0.0
                min_val = float(valid_vals.min())
                q25_val = float(valid_vals.quantile(0.25))
                median_val = float(valid_vals.median())
                q75_val = float(valid_vals.quantile(0.75))
                max_val = float(valid_vals.max())
                skew_val = float(valid_vals.skew()) if cnt > 2 else 0.0
                kurt_val = float(valid_vals.kurt()) if cnt > 3 else 0.0
            else:
                mean_val = std_val = min_val = q25_val = median_val = q75_val = max_val = skew_val = kurt_val = 0.0

            records.append({
                "column": col,
                "count": cnt,
                "mean": round(mean_val, 4),
                "std": round(std_val, 4),
                "min": round(min_val, 4),
                "q25": round(q25_val, 4),
                "median": round(median_val, 4),
                "q75": round(q75_val, 4),
                "max": round(max_val, 4),
                "skewness": round(skew_val, 4),
                "kurtosis": round(kurt_val, 4),
            })
        else:
            records.append({
                "column": col,
                "count": 0,
                "mean": 0.0,
                "std": 0.0,
                "min": 0.0,
                "q25": 0.0,
                "median": 0.0,
                "q75": 0.0,
                "max": 0.0,
                "skewness": 0.0,
                "kurtosis": 0.0,
            })

    return pd.DataFrame(records)


def summarize_feature_distribution_summary(df: pd.DataFrame) -> Dict[str, Any]:
    """Generate overall summary from distribution summary DataFrame."""
    if df.empty:
        return {
            "total_features": 0,
            "mean_features_count": 0,
            "non_signal": True,
        }

    total_features = len(df)
    features_with_data = int((df["count"] > 0).sum()) if "count" in df.columns else 0

    return {
        "total_features": total_features,
        "features_with_data": features_with_data,
        "status": "diagnostic_pass",
        "non_signal": True,
    }


def build_feature_distribution_summary_report(
    profile: FeatureQualityDriftProfile | None = None,
    df: pd.DataFrame | None = None,
    feature_columns: List[str] | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build distribution summary report and metadata summary."""
    active_profile = profile or get_default_feature_quality_drift_profile()

    if df is None:
        import numpy as np
        np.random.seed(42)
        n_rows = 100
        cols = feature_columns or [
            "feat_rsi_14", "feat_macd_line", "feat_bb_upper_20",
            "feat_atr_14", "feat_volatility_parkinson_20"
        ]
        synth_data = {c: np.random.randn(n_rows) for c in cols}
        eval_df = pd.DataFrame(synth_data)
        eval_cols = cols
    else:
        eval_df = df
        eval_cols = feature_columns

    res_df = build_distribution_summary(eval_df, eval_cols)
    summary = summarize_feature_distribution_summary(res_df)
    summary["active_profile"] = active_profile.name
    summary["current_phase"] = active_profile.current_phase
    summary["target_final_phase"] = active_profile.target_final_phase
    summary["next_phase"] = active_profile.next_phase
    summary["non_signal"] = True
    summary["destructive_action_allowed"] = False
    return res_df, summary
