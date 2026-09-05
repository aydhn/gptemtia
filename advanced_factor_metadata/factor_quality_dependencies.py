"""Phase 122 Factor Quality Dependencies Registry.

Defines feature hygiene, missingness, duplicate, and stability prerequisites
essential before handing off factors to Phase 123 Drift Diagnostics.
Strictly non-signal and research-only.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_factor_metadata.factor_metadata_config import (
    FactorMetadataProfile,
    get_default_factor_metadata_profile,
)
from advanced_factor_metadata.factor_metadata_labels import FACTOR_READY

QUALITY_DEPENDENCY_CRITERIA: List[Dict[str, Any]] = [
    {
        "quality_metric_id": "qual_dep_missingness_threshold",
        "metric_name": "Maximum Feature Missingness Threshold",
        "target_threshold": 0.35,
        "operator": "<=",
        "description": "Factor input features must not exceed 35% missingness outside warmup.",
        "phase_123_drift_relevant": True,
    },
    {
        "quality_metric_id": "qual_dep_infinite_values",
        "metric_name": "Zero Infinite Values Guard",
        "target_threshold": 0,
        "operator": "==",
        "description": "Zero positive or negative infinite values permitted in feature inputs.",
        "phase_123_drift_relevant": True,
    },
    {
        "quality_metric_id": "qual_dep_duplicate_features",
        "metric_name": "Zero Duplicate Columns Guard",
        "target_threshold": 0,
        "operator": "==",
        "description": "Rejects duplicate column names and perfectly collinear series.",
        "phase_123_drift_relevant": True,
    },
    {
        "quality_metric_id": "qual_dep_feature_availability",
        "metric_name": "Input Feature Availability Ratio",
        "target_threshold": 1.0,
        "operator": "==",
        "description": "All required input features defined in factor contract must be resolved.",
        "phase_123_drift_relevant": True,
    },
    {
        "quality_metric_id": "qual_dep_source_validation",
        "metric_name": "Upstream Source Validation Status",
        "target_threshold": 1.0,
        "operator": "==",
        "description": "Upstream Phase 116-121 matrices must hold verified PASS validation status.",
        "phase_123_drift_relevant": True,
    },
    {
        "quality_metric_id": "qual_dep_manual_review_blockers",
        "metric_name": "Manual Review Unresolved Blockers",
        "target_threshold": 0,
        "operator": "==",
        "description": "Unresolved critical manual review items block downstream drift computation.",
        "phase_123_drift_relevant": True,
    },
    {
        "quality_metric_id": "qual_dep_drift_diagnostics_readiness",
        "metric_name": "Phase 123 Drift Diagnostics Baseline",
        "target_threshold": 1.0,
        "operator": "==",
        "description": "Historical distribution baselines configured for drift tracking.",
        "phase_123_drift_relevant": True,
    },
]


def build_factor_quality_dependency_registry(
    profile: FactorMetadataProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build Factor Quality Dependency Registry DataFrame and summary."""
    active_profile = profile or get_default_factor_metadata_profile()

    records: List[Dict[str, Any]] = []
    for crit in QUALITY_DEPENDENCY_CRITERIA:
        records.append(
            {
                "quality_metric_id": crit["quality_metric_id"],
                "metric_name": crit["metric_name"],
                "target_threshold": crit["target_threshold"],
                "operator": crit["operator"],
                "description": crit["description"],
                "phase_123_drift_relevant": crit["phase_123_drift_relevant"],
                "non_signal": True,
                "status_label": FACTOR_READY,
            }
        )

    df = pd.DataFrame(records)
    summary = {
        "active_profile": active_profile.name,
        "total_quality_dependencies": len(records),
        "drift_relevant_count": sum(1 for r in records if r["phase_123_drift_relevant"]),
        "current_phase": active_profile.current_phase,
        "target_final_phase": active_profile.target_final_phase,
        "non_signal": True,
        "status": FACTOR_READY,
    }
    return df, summary


def summarize_factor_quality_dependencies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize factor quality dependencies DataFrame."""
    return {
        "total_metrics": len(df),
        "drift_prerequisites": int((df["phase_123_drift_relevant"]).sum()) if "phase_123_drift_relevant" in df else 0,
        "non_signal": True,
    }
