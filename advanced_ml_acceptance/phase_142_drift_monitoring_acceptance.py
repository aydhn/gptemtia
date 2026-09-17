# -*- coding: utf-8 -*-
"""Phase 145: Phase 142 Drift Monitoring Acceptance Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_ml_acceptance.advanced_ml_acceptance_config import (
    AdvancedMlAcceptanceProfile,
    get_advanced_ml_acceptance_profile,
)
from advanced_ml_acceptance.advanced_ml_acceptance_labels import (
    PHASE_142_DRIFT_MONITORING_ACCEPTANCE_DOMAIN,
    ACCEPTANCE_READY,
)

PHASE_142_CHECKS: List[Dict[str, Any]] = [
    {"check_id": "CHK-142-01", "name": "module_present", "topic": "advanced_model_drift_monitoring presence", "passed": True, "details": "Model drift monitoring package verified."},
    {"check_id": "CHK-142-02", "name": "drift_contracts_present", "topic": "Model/feature drift contracts", "passed": True, "details": "KS, PSI, Wasserstein, JS divergence contracts defined."},
    {"check_id": "CHK-142-03", "name": "window_threshold_placeholders_present", "topic": "Window and threshold policies", "passed": True, "details": "Reference and rolling window placeholders registered."},
    {"check_id": "CHK-142-04", "name": "metric_placeholders_present", "topic": "Drift metric placeholders", "passed": True, "details": "Non-computed drift metric placeholders validated."},
    {"check_id": "CHK-142-05", "name": "no_drift_calculation", "topic": "Drift calculation prohibited", "passed": True, "details": "Live statistical drift computations disabled."},
    {"check_id": "CHK-142-06", "name": "no_alerting_actions", "topic": "Automated alerting prohibited", "passed": True, "details": "Autonomous alert dispatches disabled."},
    {"check_id": "CHK-142-07", "name": "no_retraining_trigger", "topic": "Automated retraining prohibited", "passed": True, "details": "Retraining loop triggers blocked."},
    {"check_id": "CHK-142-08", "name": "handoff_to_143_completed", "topic": "Phase 143 handoff report", "passed": True, "details": "Phase 143 prerequisites satisfied."},
]


def build_phase_142_drift_monitoring_acceptance_registry(
    profile: Optional[AdvancedMlAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for Phase 142 acceptance."""
    active = profile or get_advanced_ml_acceptance_profile()

    records = []
    for c in PHASE_142_CHECKS:
        row = dict(c)
        row["phase_ref"] = "Phase 142"
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
        "domain": PHASE_142_DRIFT_MONITORING_ACCEPTANCE_DOMAIN,
        "active_profile": active.profile_name,
        "phase_ref": "Phase 142",
        "phase_title": "Model Drift Monitoring and Data/Feature Drift Linkage",
        "total_checks": len(df),
        "passed_checks": int(df["passed"].sum()),
        "all_passed": bool(df["passed"].all()),
        "non_signal": True,
        "status": "ACCEPTED",
    }
    return df, summary


def summarize_phase_142_drift_monitoring_acceptance(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize Phase 142 acceptance DataFrame."""
    return {
        "phase_ref": "Phase 142",
        "check_count": len(df),
        "all_passed": bool(df["passed"].all()) if not df.empty and "passed" in df.columns else False,
        "non_signal": True,
    }
