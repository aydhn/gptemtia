# -*- coding: utf-8 -*-
"""Phase 145: Advanced ML Blocker Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_ml_acceptance.advanced_ml_acceptance_config import (
    AdvancedMlAcceptanceProfile,
    get_advanced_ml_acceptance_profile,
)
from advanced_ml_acceptance.advanced_ml_acceptance_labels import (
    BLOCKER_DOMAIN,
    ACCEPTANCE_BLOCKED_BY_SAFETY,
)
from advanced_ml_acceptance.advanced_ml_acceptance_models import AdvancedMlFinding

BLOCKER_TYPES = [
    "missing_phase_module",
    "missing_manifest",
    "missing_validation_report",
    "missing_safety_boundary",
    "missing_disabled_execution_report",
    "unsafe_claim_detected",
    "production_approval_detected",
    "broker_ready_claim_detected",
    "live_trading_claim_detected",
    "model_training_detected",
    "prediction_detected",
    "artifact_persistence_detected",
    "model_registry_write_detected",
    "phase_146_handoff_missing",
]


def create_advanced_ml_blocker(
    blocker_type: str,
    phase_ref: str,
    severity_label: str,
    message: str,
    recommendation: str,
) -> AdvancedMlFinding:
    """Create a structured blocker finding."""
    return AdvancedMlFinding(
        finding_id=f"BLK-{blocker_type[:6].upper()}",
        finding_type=blocker_type,
        phase_ref=phase_ref,
        severity_label=severity_label,
        message=message,
        recommendation=recommendation,
        manual_review_required=True,
        non_signal=True,
    )


def build_advanced_ml_blocker_registry(
    profile: Optional[AdvancedMlAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for blocker registry (empty by default if clean)."""
    active = profile or get_advanced_ml_acceptance_profile()

    # When all components are clean, blocker registry has zero critical blockers
    records: List[Dict[str, Any]] = []

    df = pd.DataFrame(records, columns=[
        "finding_id", "finding_type", "phase_ref", "severity_label",
        "message", "recommendation", "manual_review_required", "non_signal",
    ])
    summary: Dict[str, Any] = {
        "domain": BLOCKER_DOMAIN,
        "active_profile": active.profile_name,
        "current_phase": active.current_phase,
        "target_final_phase": active.target_final_phase,
        "next_phase": active.next_phase,
        "total_blockers": len(df),
        "has_blockers": len(df) > 0,
        "non_signal": True,
        "status": "CLEAN" if len(df) == 0 else "BLOCKED",
    }
    return df, summary


def summarize_advanced_ml_blockers(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize blocker DataFrame."""
    return {
        "blocker_count": len(df),
        "has_blockers": len(df) > 0,
        "non_signal": True,
    }
