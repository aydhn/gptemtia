"""Phase 123 Feature Rolling Stability Diagnostics.

Calculates temporal stability metrics across rolling windows (e.g. 50 bars)
to quantify distribution volatility over time without emitting trading signals.
"""

from typing import Any, Dict, List, Tuple
import numpy as np
import pandas as pd

from advanced_feature_quality_drift.feature_quality_drift_config import (
    FeatureQualityDriftProfile,
    get_default_feature_quality_drift_profile,
)


def calculate_rolling_stability(
    df: pd.DataFrame,
    feature_columns: List[str] | None = None,
    window: int = 50,
) -> pd.DataFrame:
    """Calculate rolling stability metrics for feature columns without mutating input DataFrame."""
    if df.empty:
        cols = feature_columns or ["placeholder_feature"]
        return pd.DataFrame([{
            "column": c,
            "total_rows": 0,
            "window": window,
            "mean_rolling_std": 0.0,
            "std_of_rolling_mean": 0.0,
            "stability_score": 1.0,
            "status": "diagnostic_manual_review_required",
            "severity": "drift_medium",
            "manual_review_required": True,
            "notes": "Empty dataframe provided",
        } for c in cols])

    cols = feature_columns if feature_columns is not None else [
        c for c in df.columns if c not in ("timestamp", "asset_id", "symbol")
    ]
    total_rows = len(df)
    records = []

    for col in cols:
        if col in df.columns and pd.api.types.is_numeric_dtype(df[col]):
            s = df[col].dropna()
            n_obs = len(s)

            if n_obs < window:
                records.append({
                    "column": col,
                    "total_rows": total_rows,
                    "window": window,
                    "mean_rolling_std": 0.0,
                    "std_of_rolling_mean": 0.0,
                    "stability_score": 0.5,
                    "status": "diagnostic_manual_review_required",
                    "severity": "drift_medium",
                    "manual_review_required": True,
                    "notes": f"Insufficient rows ({n_obs} < window {window})",
                })
                continue

            rolling_mean = s.rolling(window).mean().dropna()
            rolling_std = s.rolling(window).std().dropna()

            mean_roll_std = float(rolling_std.mean()) if len(rolling_std) > 0 else 0.0
            std_roll_mean = float(rolling_mean.std()) if len(rolling_mean) > 0 else 0.0

            # Stability score: higher indicates more stable rolling properties
            overall_std = float(s.std()) if len(s) > 1 else 1e-6
            rel_instability = std_roll_mean / max(1e-6, overall_std)
            stab_score = max(0.0, min(1.0, 1.0 / (1.0 + rel_instability)))

            if stab_score < 0.40:
                status = "diagnostic_fail"
                sev = "drift_high"
                review = True
                notes = "High rolling instability detected"
            elif stab_score < 0.65:
                status = "diagnostic_pass_with_warnings"
                sev = "drift_medium"
                review = True
                notes = "Moderate rolling instability"
            else:
                status = "diagnostic_pass"
                sev = "drift_low"
                review = False
                notes = "Stable rolling feature dynamics"

            records.append({
                "column": col,
                "total_rows": total_rows,
                "window": window,
                "mean_rolling_std": round(mean_roll_std, 4),
                "std_of_rolling_mean": round(std_roll_mean, 4),
                "stability_score": round(stab_score, 4),
                "status": status,
                "severity": sev,
                "manual_review_required": review,
                "notes": notes,
            })
        else:
            records.append({
                "column": col,
                "total_rows": total_rows,
                "window": window,
                "mean_rolling_std": 0.0,
                "std_of_rolling_mean": 0.0,
                "stability_score": 0.0,
                "status": "diagnostic_fail",
                "severity": "drift_high",
                "manual_review_required": True,
                "notes": "Non-numeric or missing column",
            })

    return pd.DataFrame(records)


def summarize_feature_rolling_stability(df: pd.DataFrame) -> Dict[str, Any]:
    """Generate overall summary statistics from rolling stability DataFrame."""
    if df.empty:
        return {
            "total_features": 0,
            "mean_stability_score": 0.0,
            "unstable_features_count": 0,
            "status": "diagnostic_pass",
            "manual_review_required": False,
        }

    total_features = len(df)
    unstable_count = int((df["severity"].isin(["drift_high", "drift_critical"])).sum())
    mean_stab = float(df["stability_score"].mean()) if "stability_score" in df.columns else 0.0

    if unstable_count > 0:
        overall_status = "diagnostic_fail"
    elif (df["severity"] == "drift_medium").sum() > 0:
        overall_status = "diagnostic_pass_with_warnings"
    else:
        overall_status = "diagnostic_pass"

    return {
        "total_features": total_features,
        "mean_stability_score": round(mean_stab, 4),
        "unstable_features_count": unstable_count,
        "status": overall_status,
        "manual_review_required": unstable_count > 0,
    }


def build_feature_rolling_stability_report(
    profile: FeatureQualityDriftProfile | None = None,
    df: pd.DataFrame | None = None,
    feature_columns: List[str] | None = None,
    window: int = 50,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build rolling stability report and summary."""
    active_profile = profile or get_default_feature_quality_drift_profile()

    if df is None:
        np.random.seed(42)
        n_rows = 150
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

    res_df = calculate_rolling_stability(eval_df, eval_cols, window=window)
    summary = summarize_feature_rolling_stability(res_df)
    summary["active_profile"] = active_profile.name
    summary["current_phase"] = active_profile.current_phase
    summary["target_final_phase"] = active_profile.target_final_phase
    summary["next_phase"] = active_profile.next_phase
    summary["non_signal"] = True
    summary["destructive_action_allowed"] = False
    return res_df, summary
