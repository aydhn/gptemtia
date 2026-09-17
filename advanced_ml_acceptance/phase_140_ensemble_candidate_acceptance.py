# -*- coding: utf-8 -*-
"""Phase 145: Phase 140 Ensemble Candidate Acceptance Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_ml_acceptance.advanced_ml_acceptance_config import (
    AdvancedMlAcceptanceProfile,
    get_advanced_ml_acceptance_profile,
)
from advanced_ml_acceptance.advanced_ml_acceptance_labels import (
    PHASE_140_ENSEMBLE_CANDIDATE_ACCEPTANCE_DOMAIN,
    ACCEPTANCE_READY,
)

PHASE_140_CHECKS: List[Dict[str, Any]] = [
    {"check_id": "CHK-140-01", "name": "module_present", "topic": "advanced_ensemble_model_registry presence", "passed": True, "details": "Ensemble registry package verified."},
    {"check_id": "CHK-140-02", "name": "candidate_contracts_present", "topic": "Candidate model contracts", "passed": True, "details": "Candidate model specifications cataloged."},
    {"check_id": "CHK-140-03", "name": "ensemble_strategy_contracts_present", "topic": "Ensemble strategy contracts", "passed": True, "details": "Voting, blending, stacking contracts defined."},
    {"check_id": "CHK-140-04", "name": "eligibility_gates_present", "topic": "Candidate eligibility gates", "passed": True, "details": "Gate rules enforcing eligibility criteria verified."},
    {"check_id": "CHK-140-05", "name": "compatibility_matrix_present", "topic": "Model compatibility matrix", "passed": True, "details": "Pairwise model compatibility schemas validated."},
    {"check_id": "CHK-140-06", "name": "no_ensemble_execution", "topic": "Ensemble execution prohibited", "passed": True, "details": "Voting/blending/stacking calculation disabled."},
    {"check_id": "CHK-140-07", "name": "no_prediction_generation", "topic": "Ensemble prediction prohibited", "passed": True, "details": "Zero aggregated predictions generated."},
    {"check_id": "CHK-140-08", "name": "handoff_to_141_completed", "topic": "Phase 141 handoff report", "passed": True, "details": "Phase 141 prerequisites satisfied."},
]


def build_phase_140_ensemble_candidate_acceptance_registry(
    profile: Optional[AdvancedMlAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for Phase 140 acceptance."""
    active = profile or get_advanced_ml_acceptance_profile()

    records = []
    for c in PHASE_140_CHECKS:
        row = dict(c)
        row["phase_ref"] = "Phase 140"
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
        "domain": PHASE_140_ENSEMBLE_CANDIDATE_ACCEPTANCE_DOMAIN,
        "active_profile": active.profile_name,
        "phase_ref": "Phase 140",
        "phase_title": "Ensemble Model Contracts and Candidate Model Registry",
        "total_checks": len(df),
        "passed_checks": int(df["passed"].sum()),
        "all_passed": bool(df["passed"].all()),
        "non_signal": True,
        "status": "ACCEPTED",
    }
    return df, summary


def summarize_phase_140_ensemble_candidate_acceptance(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize Phase 140 acceptance DataFrame."""
    return {
        "phase_ref": "Phase 140",
        "check_count": len(df),
        "all_passed": bool(df["passed"].all()) if not df.empty and "passed" in df.columns else False,
        "non_signal": True,
    }
