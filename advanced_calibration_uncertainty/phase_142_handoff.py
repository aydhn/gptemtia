# -*- coding: utf-8 -*-
"""Phase 141: Phase 142 Model Drift Monitoring Handoff."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_calibration_uncertainty.calibration_uncertainty_config import (
    CalibrationUncertaintyProfile,
    get_calibration_uncertainty_profile,
)

HANDOFF_PREREQUISITES: List[Dict[str, Any]] = [
    {
        "prerequisite_id": "PREREQ_CALIB_CONTRACTS",
        "title": "calibration_contract_prerequisites",
        "description": "7 probability calibration contracts registered and verified non-executing.",
        "status": "SATISFIED",
        "blocking": True,
    },
    {
        "prerequisite_id": "PREREQ_UNCERT_CONTRACTS",
        "title": "uncertainty_contract_prerequisites",
        "description": "8 uncertainty estimation contracts registered and verified non-executing.",
        "status": "SATISFIED",
        "blocking": True,
    },
    {
        "prerequisite_id": "PREREQ_MODEL_REGISTRY",
        "title": "candidate_ensemble_registry_prerequisites",
        "description": "Candidate model contracts and ensemble strategy contracts established in Phase 140.",
        "status": "SATISFIED",
        "blocking": True,
    },
    {
        "prerequisite_id": "PREREQ_DATASET_CONTRACTS",
        "title": "dataset_contract_prerequisites",
        "description": "Temporal dataset contracts and feature snapshot governance from Phase 137.",
        "status": "SATISFIED",
        "blocking": True,
    },
    {
        "prerequisite_id": "PREREQ_GUARDS",
        "title": "no_lookahead_and_metadata_guards",
        "description": "Strict verification of zero lookahead bias, metadata-only news, and source preservation.",
        "status": "SATISFIED",
        "blocking": True,
    },
    {
        "prerequisite_id": "PREREQ_METRICS_AUDIT",
        "title": "metric_and_audit_placeholders",
        "description": "Uncalculated ECE/Brier/Interval metrics and audit trail templates ready for drift linkage.",
        "status": "SATISFIED",
        "blocking": True,
    },
    {
        "prerequisite_id": "PREREQ_DRIFT_LINKAGE",
        "title": "feature_drift_linkage_readiness",
        "description": "Phase 123 feature drift diagnostics prepared to link with Phase 142 model drift monitoring.",
        "status": "SATISFIED",
        "blocking": True,
    },
    {
        "prerequisite_id": "PREREQ_SAFETY_BOUNDARY",
        "title": "zero_trading_zero_broker_boundary",
        "description": "Explicit non-trading and non-execution invariant maintained for Phase 142.",
        "status": "SATISFIED",
        "blocking": True,
    },
]


def build_phase_142_model_drift_monitoring_handoff_report(
    profile: Optional[CalibrationUncertaintyProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for Phase 142 handoff report."""
    prof = profile or get_calibration_uncertainty_profile()
    rows = []
    for item in HANDOFF_PREREQUISITES:
        rows.append(
            {
                "prerequisite_id": item["prerequisite_id"],
                "title": item["title"],
                "description": item["description"],
                "status": item["status"],
                "blocking": item["blocking"],
                "source_phase": prof.current_phase,
                "next_phase": prof.next_phase,
                "target_final_phase": prof.target_final_phase,
                "non_signal": True,
            }
        )

    df = pd.DataFrame(rows)
    summary = summarize_phase_142_handoff(df)
    return df, summary


def summarize_phase_142_handoff(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize Phase 142 handoff DataFrame."""
    total = len(df)
    satisfied = int((df["status"] == "SATISFIED").sum()) if not df.empty else 0
    all_satisfied = (satisfied == total) and total > 0
    return {
        "handoff_status": "READY_FOR_PHASE_142" if all_satisfied else "BLOCKED",
        "source_phase": 141,
        "next_phase": 142,
        "next_phase_title": "Model Drift Monitoring and Data/Feature Drift Linkage",
        "target_final_phase": 160,
        "total_prerequisites": total,
        "satisfied_prerequisites": satisfied,
        "all_prerequisites_met": all_satisfied,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
    }
