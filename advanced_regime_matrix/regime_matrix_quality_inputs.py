"""Phase 127: Regime Matrix Quality Inputs Registry.

Defines data quality and drift prerequisites gating regime matrix rows.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_matrix.regime_matrix_config import (
    RegimeMatrixProfile,
    get_default_regime_matrix_profile,
)

QUALITY_INPUTS_CATALOG: List[Dict[str, Any]] = [
    {
        "metric_id": "qual_validation_status",
        "metric_name": "validation_pass_status",
        "source_phase": 121,
        "description": "Requires VALIDATION_PASS or VALIDATION_WARN before inclusion in matrix.",
        "threshold": "status in ['VALIDATION_PASS', 'VALIDATION_WARN']",
        "is_blocking": True,
        "non_signal": True,
    },
    {
        "metric_id": "qual_missingness_score",
        "metric_name": "feature_missingness_ratio",
        "source_phase": 123,
        "description": "Maximum permitted fraction of missing points in rolling windows.",
        "threshold": "missingness <= 0.05",
        "is_blocking": True,
        "non_signal": True,
    },
    {
        "metric_id": "qual_drift_score_psi",
        "metric_name": "population_stability_index",
        "source_phase": 123,
        "description": "Population Stability Index monitoring feature distribution shift.",
        "threshold": "psi <= 0.25",
        "is_blocking": False,
        "non_signal": True,
    },
    {
        "metric_id": "qual_staleness_diagnostics",
        "metric_name": "time_since_last_update",
        "source_phase": 123,
        "description": "Detects flatlining or delayed observation updates.",
        "threshold": "stale_bars <= 5",
        "is_blocking": True,
        "non_signal": True,
    },
    {
        "metric_id": "qual_manual_review_blocker",
        "metric_name": "active_manual_review_blockers",
        "source_phase": 124,
        "description": "Ensures no critical blocking findings exist in manual review queue.",
        "threshold": "blocking_review_count == 0",
        "is_blocking": True,
        "non_signal": True,
    },
    {
        "metric_id": "qual_source_preservation_status",
        "metric_name": "source_preservation_verified",
        "source_phase": 125,
        "description": "Guarantees raw data has not been modified, overwritten, or auto-imputed.",
        "threshold": "source_preserved == True",
        "is_blocking": True,
        "non_signal": True,
    },
]


def build_regime_matrix_quality_input_registry(
    profile: Optional[RegimeMatrixProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the quality inputs registry for Phase 127."""
    p = profile or get_default_regime_matrix_profile()

    rows = []
    for q in QUALITY_INPUTS_CATALOG:
        q_copy = q.copy()
        q_copy["current_phase"] = p.current_phase
        q_copy["target_final_phase"] = p.target_final_phase
        q_copy["next_phase"] = p.next_phase
        q_copy["source_preserved"] = True
        q_copy["status"] = "matrix_ready"
        rows.append(q_copy)

    df = pd.DataFrame(rows)
    summary = summarize_regime_matrix_quality_inputs(df)
    return df, summary


def summarize_regime_matrix_quality_inputs(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize quality inputs registry."""
    return {
        "total_quality_inputs": len(df),
        "metric_ids": df["metric_id"].tolist() if not df.empty else [],
        "blocking_metrics_count": int(df["is_blocking"].sum()) if not df.empty else 0,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "all_source_preserved": bool(df["source_preserved"].all()) if not df.empty else True,
        "status": "matrix_ready",
    }


build_regime_matrix_quality_inputs_registry = build_regime_matrix_quality_input_registry

