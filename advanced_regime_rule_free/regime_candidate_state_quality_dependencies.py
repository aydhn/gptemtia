"""Phase 128: Regime Candidate State Quality Dependencies.

Defines data quality prerequisites and thresholds linked to Phase 123 diagnostics.
"""

from typing import Dict, Tuple
import pandas as pd

from advanced_regime_rule_free.regime_rule_free_config import (
    RegimeRuleFreeProfile,
    get_default_regime_rule_free_profile,
)

QUALITY_DEPENDENCIES = [
    {
        "dependency_id": "dep_phase_123_quality_score",
        "category": "feature_quality",
        "description": "Requires Phase 123 feature quality score >= 0.70 for candidate state inclusion.",
        "threshold": 0.70,
        "is_blocker": True,
        "non_signal": True,
    },
    {
        "dependency_id": "dep_phase_123_drift_score",
        "category": "drift_stability",
        "description": "Requires Phase 123 PSI drift score < 0.25 to prevent assigning states on unstable distributions.",
        "threshold": 0.25,
        "is_blocker": True,
        "non_signal": True,
    },
    {
        "dependency_id": "dep_feature_availability",
        "category": "completeness",
        "description": "Requires candidate feature availability >= 95% over the rolling assessment window.",
        "threshold": 0.95,
        "is_blocker": True,
        "non_signal": True,
    },
    {
        "dependency_id": "dep_staleness_diagnostics",
        "category": "freshness",
        "description": "Requires feature staleness to remain within designated market session bounds.",
        "threshold": 0.0,
        "is_blocker": True,
        "non_signal": True,
    },
    {
        "dependency_id": "dep_namespace_quality",
        "category": "naming_governance",
        "description": "Requires 100% compliance with candidate_state_ naming conventions and zero forbidden terms.",
        "threshold": 1.0,
        "is_blocker": True,
        "non_signal": True,
    },
    {
        "dependency_id": "dep_manual_review_blocker_status",
        "category": "human_governance",
        "description": "Unresolved manual review queue items block automatic candidate state promotion.",
        "threshold": 0.0,
        "is_blocker": True,
        "non_signal": True,
    },
]


def build_regime_candidate_state_quality_dependency_registry(
    profile: RegimeRuleFreeProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and summary metadata for quality dependencies."""
    active_profile = profile or get_default_regime_rule_free_profile()

    rows = []
    for q in QUALITY_DEPENDENCIES:
        row = q.copy()
        row["current_phase"] = active_profile.current_phase
        row["next_phase"] = active_profile.next_phase
        row["target_final_phase"] = active_profile.target_final_phase
        rows.append(row)

    df = pd.DataFrame(rows)
    summary = summarize_candidate_state_quality_dependencies(df)
    return df, summary


def summarize_candidate_state_quality_dependencies(df: pd.DataFrame) -> Dict:
    """Summarize quality dependencies."""
    total = len(df)
    blockers = int(df["is_blocker"].sum()) if not df.empty else 0
    all_non_signal = bool(df["non_signal"].all()) if not df.empty else True

    return {
        "total_quality_dependencies": total,
        "blocking_dependencies_count": blockers,
        "all_non_signal": all_non_signal,
        "status": "VALID" if all_non_signal and total > 0 else "INVALID",
    }
