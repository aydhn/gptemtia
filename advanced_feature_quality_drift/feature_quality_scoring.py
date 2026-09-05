"""Phase 123 Feature Quality Scoring.

Calculates composite and dimension-specific quality scores across feature columns.
Strictly non-signal and research-only; scores do NOT represent production approvals or trading ratings.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from advanced_feature_quality_drift.feature_quality_drift_config import (
    FeatureQualityDriftProfile,
    get_default_feature_quality_drift_profile,
)


def calculate_feature_quality_score(
    missingness_score: float = 1.0,
    infinite_value_score: float = 1.0,
    zero_variance_score: float = 1.0,
    duplicate_score: float = 1.0,
    namespace_score: float = 1.0,
) -> float:
    """Calculate overall weighted quality score within [0, 1]."""
    weights = {
        "missingness": 0.25,
        "infinite_value": 0.25,
        "zero_variance": 0.20,
        "duplicate": 0.15,
        "namespace": 0.15,
    }
    overall = (
        missingness_score * weights["missingness"]
        + infinite_value_score * weights["infinite_value"]
        + zero_variance_score * weights["zero_variance"]
        + duplicate_score * weights["duplicate"]
        + namespace_score * weights["namespace"]
    )
    return round(max(0.0, min(1.0, overall)), 4)


def build_feature_quality_score_report(
    profile: FeatureQualityDriftProfile | None = None,
    diagnostic_tables: Dict[str, pd.DataFrame] | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build feature quality score report across dimensions."""
    active_profile = profile or get_default_feature_quality_drift_profile()

    # Calculate subscores from tables if available
    miss_score = 1.0
    inf_score = 1.0
    zv_score = 1.0
    dup_score = 1.0
    ns_score = 1.0

    if diagnostic_tables:
        if "missingness" in diagnostic_tables and not diagnostic_tables["missingness"].empty:
            m_df = diagnostic_tables["missingness"]
            crit = (m_df["severity"] == "quality_critical").sum()
            warn = (m_df["severity"] == "quality_medium").sum()
            miss_score = max(0.0, 1.0 - (crit * 0.2 + warn * 0.05))

        if "infinite_values" in diagnostic_tables and not diagnostic_tables["infinite_values"].empty:
            i_df = diagnostic_tables["infinite_values"]
            inf_present = (i_df["total_inf_count"] > 0).sum()
            inf_score = 0.0 if inf_present > 0 else 1.0

        if "zero_variance" in diagnostic_tables and not diagnostic_tables["zero_variance"].empty:
            z_df = diagnostic_tables["zero_variance"]
            zv_count = (z_df["zero_variance_flag"]).sum()
            zv_score = max(0.0, 1.0 - zv_count * 0.25)

        if "duplicates" in diagnostic_tables and not diagnostic_tables["duplicates"].empty:
            d_df = diagnostic_tables["duplicates"]
            dup_warn = (d_df["severity"] == "quality_medium").sum()
            dup_score = max(0.0, 1.0 - dup_warn * 0.1)

        if "namespace" in diagnostic_tables and not diagnostic_tables["namespace"].empty:
            n_df = diagnostic_tables["namespace"]
            forbid = (n_df["has_forbidden_token"]).sum()
            coll = (n_df["is_duplicate"]).sum()
            ns_score = 0.0 if forbid > 0 else (0.5 if coll > 0 else 1.0)

    overall_score = calculate_feature_quality_score(
        missingness_score=miss_score,
        infinite_value_score=inf_score,
        zero_variance_score=zv_score,
        duplicate_score=dup_score,
        namespace_score=ns_score,
    )

    records = [
        {"dimension": "overall_quality", "score": overall_score, "weight": 1.0, "status": "diagnostic_pass" if overall_score >= active_profile.min_quality_score else "diagnostic_fail"},
        {"dimension": "missingness", "score": miss_score, "weight": 0.25, "status": "diagnostic_pass" if miss_score >= 0.70 else "diagnostic_fail"},
        {"dimension": "infinite_values", "score": inf_score, "weight": 0.25, "status": "diagnostic_pass" if inf_score == 1.0 else "diagnostic_fail"},
        {"dimension": "zero_variance", "score": zv_score, "weight": 0.20, "status": "diagnostic_pass" if zv_score >= 0.75 else "diagnostic_fail"},
        {"dimension": "duplicates", "score": dup_score, "weight": 0.15, "status": "diagnostic_pass" if dup_score >= 0.70 else "diagnostic_fail"},
        {"dimension": "namespace", "score": ns_score, "weight": 0.15, "status": "diagnostic_pass" if ns_score == 1.0 else "diagnostic_fail"},
    ]

    df = pd.DataFrame(records)
    summary = {
        "active_profile": active_profile.name,
        "overall_quality_score": overall_score,
        "min_quality_threshold": active_profile.min_quality_score,
        "quality_status": "diagnostic_pass" if overall_score >= active_profile.min_quality_score else "diagnostic_fail",
        "current_phase": active_profile.current_phase,
        "target_final_phase": active_profile.target_final_phase,
        "next_phase": active_profile.next_phase,
        "non_signal": True,
        "official_approval": False,
        "production_ready": False,
    }
    return df, summary
