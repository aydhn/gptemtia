"""Phase 130: Transition Quality Findings Registry.

Tracks and registers findings, anomalies, and observations discovered during
regime transition and stability analysis.
"""

from typing import Any, Dict, List, Optional, Tuple
import uuid
import pandas as pd

from advanced_regime_transition.regime_transition_config import (
    RegimeTransitionProfile,
    get_default_regime_transition_profile,
)
from advanced_regime_transition.regime_transition_models import TransitionQualityFinding

VALID_FINDING_TYPES: List[str] = [
    "missing_sequence_contract",
    "missing_candidate_state_sequence_schema",
    "insufficient_sequence_history",
    "transition_ambiguity_warning",
    "transition_continuity_warning",
    "transition_stability_warning",
    "missing_quality_dependency",
    "missing_validation_dependency",
    "news_metadata_boundary_risk",
    "no_lookahead_dependency_unresolved",
    "phase_131_readiness_blocker",
]

DEFAULT_FINDINGS: List[Dict[str, Any]] = [
    {
        "finding_id": "FIND-130-001",
        "finding_type": "transition_ambiguity_warning",
        "transition_family": "trend_range",
        "severity_label": "transition_medium",
        "message": "Elevated transition ambiguity observed during range boundary transition rehearsal",
        "recommendation": "Perform manual review of candidate state thresholds without automated modification",
        "manual_review_required": True,
        "destructive_action_allowed": False,
        "auto_fix_allowed": False,
        "auto_fix_forbidden": True,
        "auto_drop_allowed": False,
        "non_signal": True,
    },
    {
        "finding_id": "FIND-130-002",
        "finding_type": "transition_continuity_warning",
        "transition_family": "commodity_energy",
        "severity_label": "transition_low",
        "message": "Minor weekend session gap noted in commodity sequence timestamps",
        "recommendation": "Confirm calendar alignment contract covers exchange holiday sessions",
        "manual_review_required": True,
        "destructive_action_allowed": False,
        "auto_fix_allowed": False,
        "auto_fix_forbidden": True,
        "auto_drop_allowed": False,
        "non_signal": True,
    },
]


def create_transition_quality_finding(
    finding_type: str,
    transition_family: str,
    severity_label: str,
    message: str,
    recommendation: str,
    manual_review_required: bool = True,
) -> TransitionQualityFinding:
    """Factory creating a validated TransitionQualityFinding dataclass instance."""
    finding_id = f"FIND-130-{uuid.uuid4().hex[:6].upper()}"
    return TransitionQualityFinding(
        finding_id=finding_id,
        finding_type=finding_type,
        transition_family=transition_family,
        severity_label=severity_label,
        message=message,
        recommendation=recommendation,
        manual_review_required=manual_review_required,
        destructive_action_allowed=False,
        auto_fix_allowed=False,
        auto_drop_allowed=False,
        non_signal=True,
    )


def build_transition_quality_findings_registry(
    profile: Optional[RegimeTransitionProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build findings registry dataframe and summary."""
    if profile is None:
        profile = get_default_regime_transition_profile()

    df = pd.DataFrame(DEFAULT_FINDINGS)
    summary = summarize_transition_quality_findings(df)
    summary["active_profile"] = profile.profile_name
    return df, summary


def summarize_transition_quality_findings(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize transition quality findings."""
    all_forbidden = bool(df["auto_fix_forbidden"].all()) if not df.empty and "auto_fix_forbidden" in df.columns else True
    return {
        "total_findings": len(df),
        "manual_review_count": int(df["manual_review_required"].sum()) if not df.empty and "manual_review_required" in df.columns else 0,
        "manual_review_required": True,
        "all_auto_fix_forbidden": all_forbidden,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "zero_destructive_actions": bool(not df["destructive_action_allowed"].any()) if not df.empty else True,
        "zero_auto_fix_allowed": bool(not df["auto_fix_allowed"].any()) if not df.empty else True,
    }

