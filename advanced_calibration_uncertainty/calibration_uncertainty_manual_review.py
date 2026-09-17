# -*- coding: utf-8 -*-
"""Phase 141: Calibration & Uncertainty Manual Review Queue."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_calibration_uncertainty.calibration_uncertainty_config import (
    CalibrationUncertaintyProfile,
    get_calibration_uncertainty_profile,
)

MANUAL_REVIEW_TASKS: List[Dict[str, Any]] = [
    {
        "review_id": "REV_CALIB_001",
        "task_name": "inspect_probability_calibration_contracts",
        "description": "Inspect probability calibration contracts ensuring fit and prediction are disabled.",
        "suggested_action": "inspect calibration contracts",
    },
    {
        "review_id": "REV_UNCERT_002",
        "task_name": "inspect_uncertainty_estimation_contracts",
        "description": "Inspect uncertainty estimation contracts ensuring intervals and conformal sets are uncomputed.",
        "suggested_action": "inspect uncertainty contracts",
    },
    {
        "review_id": "REV_METH_003",
        "task_name": "inspect_calibration_method_placeholders",
        "description": "Inspect calibration method placeholders ensuring zero fitting or optimization occurred.",
        "suggested_action": "inspect calibration method placeholders",
    },
    {
        "review_id": "REV_UMETH_004",
        "task_name": "inspect_uncertainty_method_placeholders",
        "description": "Inspect uncertainty method placeholders ensuring zero resampling or estimation occurred.",
        "suggested_action": "inspect uncertainty method placeholders",
    },
    {
        "review_id": "REV_DIS_005",
        "task_name": "inspect_disabled_execution_reports",
        "description": "Inspect disabled execution reports confirming all runtime interceptors are active.",
        "suggested_action": "inspect disabled probability/calibration/uncertainty reports",
    },
    {
        "review_id": "REV_GATE_006",
        "task_name": "inspect_quality_gates",
        "description": "Inspect calibration and uncertainty quality gates to verify blocking policies.",
        "suggested_action": "inspect calibration/uncertainty quality gates",
    },
    {
        "review_id": "REV_DRIFT_007",
        "task_name": "inspect_phase_142_drift_monitoring_blockers",
        "description": "Inspect handoff prerequisites for Phase 142 Model Drift Monitoring.",
        "suggested_action": "inspect Phase 142 drift monitoring blockers",
    },
]


def build_calibration_uncertainty_manual_review_queue(
    profile: Optional[CalibrationUncertaintyProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for manual review queue."""
    prof = profile or get_calibration_uncertainty_profile()
    rows = []
    for item in MANUAL_REVIEW_TASKS:
        rows.append(
            {
                "review_id": item["review_id"],
                "task_name": item["task_name"],
                "description": item["description"],
                "suggested_action": item["suggested_action"],
                "auto_action_allowed": False,
                "auto_fix_allowed": False,
                "non_signal": True,
                "status": "PENDING_OPERATOR_REVIEW",
                "phase": prof.current_phase,
            }
        )

    df = pd.DataFrame(rows)
    summary = summarize_calibration_uncertainty_manual_review_queue(df)
    return df, summary


def summarize_calibration_uncertainty_manual_review_queue(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize manual review queue DataFrame."""
    return {
        "total_review_items": len(df),
        "review_ids": df["review_id"].tolist() if not df.empty else [],
        "all_auto_prohibited": bool((~df["auto_action_allowed"]).all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
    }
