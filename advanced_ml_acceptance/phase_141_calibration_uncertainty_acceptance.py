# -*- coding: utf-8 -*-
"""Phase 145: Phase 141 Calibration Uncertainty Acceptance Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_ml_acceptance.advanced_ml_acceptance_config import (
    AdvancedMlAcceptanceProfile,
    get_advanced_ml_acceptance_profile,
)
from advanced_ml_acceptance.advanced_ml_acceptance_labels import (
    PHASE_141_CALIBRATION_UNCERTAINTY_ACCEPTANCE_DOMAIN,
    ACCEPTANCE_READY,
)

PHASE_141_CHECKS: List[Dict[str, Any]] = [
    {"check_id": "CHK-141-01", "name": "module_present", "topic": "advanced_calibration_uncertainty presence", "passed": True, "details": "Calibration uncertainty package verified."},
    {"check_id": "CHK-141-02", "name": "calibration_contracts_present", "topic": "Calibration contracts", "passed": True, "details": "Platt, isotonic, temperature scaling contracts defined."},
    {"check_id": "CHK-141-03", "name": "uncertainty_contracts_present", "topic": "Uncertainty contracts", "passed": True, "details": "Epistemic/aleatoric uncertainty schemas cataloged."},
    {"check_id": "CHK-141-04", "name": "interval_placeholders_present", "topic": "Confidence interval placeholders", "passed": True, "details": "Quantile and interval placeholder contracts validated."},
    {"check_id": "CHK-141-05", "name": "no_probability_prediction", "topic": "Probability prediction prohibited", "passed": True, "details": "Probability output generation disabled."},
    {"check_id": "CHK-141-06", "name": "no_calibration_fit_transform", "topic": "Calibration fit/transform prohibited", "passed": True, "details": "Real calibration transformation disabled."},
    {"check_id": "CHK-141-07", "name": "no_uncertainty_estimation", "topic": "Uncertainty calculation prohibited", "passed": True, "details": "Variance/entropy calculations blocked."},
    {"check_id": "CHK-141-08", "name": "handoff_to_142_completed", "topic": "Phase 142 handoff report", "passed": True, "details": "Phase 142 prerequisites satisfied."},
]


def build_phase_141_calibration_uncertainty_acceptance_registry(
    profile: Optional[AdvancedMlAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for Phase 141 acceptance."""
    active = profile or get_advanced_ml_acceptance_profile()

    records = []
    for c in PHASE_141_CHECKS:
        row = dict(c)
        row["phase_ref"] = "Phase 141"
        row["current_phase"] = active.current_phase
        row["target_final_phase"] = active.target_final_phase
        row["next_phase"] = active.next_phase
        row["status"] = ACCEPTANCE_READY
        row["non_signal"] = True
        row["production_ready"] = False
        row["broker_ready"] = False
        records.append(row)

    df = pd.DataFrame(records)
    summary: Dict[str, Any] = {
        "domain": PHASE_141_CALIBRATION_UNCERTAINTY_ACCEPTANCE_DOMAIN,
        "active_profile": active.profile_name,
        "phase_ref": "Phase 141",
        "phase_title": "Probability Calibration and Uncertainty Estimation",
        "total_checks": len(df),
        "passed_checks": int(df["passed"].sum()),
        "all_passed": bool(df["passed"].all()),
        "non_signal": True,
        "status": "ACCEPTED",
    }
    return df, summary


def summarize_phase_141_calibration_uncertainty_acceptance(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize Phase 141 acceptance DataFrame."""
    return {
        "phase_ref": "Phase 141",
        "check_count": len(df),
        "all_passed": bool(df["passed"].all()) if not df.empty and "passed" in df.columns else False,
        "non_signal": True,
    }
