"""Phase 123 Feature Drift Scoring.

Calculates composite drift and temporal stability scores across feature columns.
Strictly non-signal and research-only; scores do NOT represent trade signals or model predictions.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from advanced_feature_quality_drift.feature_quality_drift_config import (
    FeatureQualityDriftProfile,
    get_default_feature_quality_drift_profile,
)


def calculate_feature_drift_score(
    mean_stability_score: float = 1.0,
    std_stability_score: float = 1.0,
    quantile_stability_score: float = 1.0,
    rolling_stability_score: float = 1.0,
) -> float:
    """Calculate overall weighted drift stability score within [0, 1]."""
    weights = {
        "mean_stability": 0.30,
        "std_stability": 0.30,
        "quantile_stability": 0.20,
        "rolling_stability": 0.20,
    }
    overall = (
        mean_stability_score * weights["mean_stability"]
        + std_stability_score * weights["std_stability"]
        + quantile_stability_score * weights["quantile_stability"]
        + rolling_stability_score * weights["rolling_stability"]
    )
    return round(max(0.0, min(1.0, overall)), 4)


def build_feature_drift_score_report(
    profile: FeatureQualityDriftProfile | None = None,
    diagnostic_tables: Dict[str, pd.DataFrame] | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build feature drift score report across stability dimensions."""
    active_profile = profile or get_default_feature_quality_drift_profile()

    mean_stab = 1.0
    std_stab = 1.0
    quant_stab = 1.0
    roll_stab = 1.0

    if diagnostic_tables:
        if "distribution_drift" in diagnostic_tables and not diagnostic_tables["distribution_drift"].empty:
            d_df = diagnostic_tables["distribution_drift"]
            crit = (d_df["severity"] == "drift_critical").sum()
            warn = (d_df["severity"] == "drift_medium").sum()
            penalty = float(crit * 0.25 + warn * 0.08)
            mean_stab = max(0.0, 1.0 - penalty)
            std_stab = max(0.0, 1.0 - penalty)
            quant_stab = max(0.0, 1.0 - penalty)

        if "rolling_stability" in diagnostic_tables and not diagnostic_tables["rolling_stability"].empty:
            r_df = diagnostic_tables["rolling_stability"]
            if "stability_score" in r_df.columns:
                roll_stab = float(r_df["stability_score"].mean())

    overall_score = calculate_feature_drift_score(
        mean_stability_score=mean_stab,
        std_stability_score=std_stab,
        quantile_stability_score=quant_stab,
        rolling_stability_score=roll_stab,
    )

    records = [
        {"dimension": "overall_stability", "score": overall_score, "weight": 1.0, "status": "diagnostic_pass" if overall_score >= active_profile.min_drift_score else "diagnostic_fail"},
        {"dimension": "mean_stability", "score": mean_stab, "weight": 0.30, "status": "diagnostic_pass" if mean_stab >= 0.60 else "diagnostic_fail"},
        {"dimension": "std_stability", "score": std_stab, "weight": 0.30, "status": "diagnostic_pass" if std_stab >= 0.60 else "diagnostic_fail"},
        {"dimension": "quantile_stability", "score": quant_stab, "weight": 0.20, "status": "diagnostic_pass" if quant_stab >= 0.60 else "diagnostic_fail"},
        {"dimension": "rolling_stability", "score": roll_stab, "weight": 0.20, "status": "diagnostic_pass" if roll_stab >= 0.50 else "diagnostic_fail"},
    ]

    df = pd.DataFrame(records)
    summary = {
        "active_profile": active_profile.name,
        "overall_drift_score": overall_score,
        "min_drift_threshold": active_profile.min_drift_score,
        "drift_status": "diagnostic_pass" if overall_score >= active_profile.min_drift_score else "diagnostic_fail",
        "current_phase": active_profile.current_phase,
        "target_final_phase": active_profile.target_final_phase,
        "next_phase": active_profile.next_phase,
        "non_signal": True,
        "official_approval": False,
        "production_ready": False,
    }
    return df, summary
