"""Phase 134: Regime Manual Review Blocker Store.

Tracks safety blockers requiring manual human inspection before promotion.
Strictly prohibits automated fixes and destructive cleaning.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_featurestore_integration.regime_featurestore_config import (
    RegimeFeatureStoreProfile,
    get_regime_featurestore_profile,
)
from advanced_regime_featurestore_integration.regime_featurestore_labels import (
    MANUAL_REVIEW_BLOCKER_DOMAIN,
    REGIME_STORE_READY,
)

CANONICAL_BLOCKER_DEFINITIONS: List[Dict[str, Any]] = [
    {
        "blocker_id": "blocker_def_no_lookahead",
        "blocker_type": "no_lookahead_acceptance_blocker",
        "severity": "CRITICAL",
        "description": "Triggered if backward-only asof join or temporal timestamp ordering fails.",
        "affected_component": "all_regime_components",
        "remediation_guidance": "Inspect join keys, ensure context_ts <= base_ts, no auto-fix allowed.",
        "auto_fix_allowed": False,
        "destructive_action_allowed": False,
        "is_active": False,
    },
    {
        "blocker_id": "blocker_def_metadata_only_news",
        "blocker_type": "metadata_only_news_blocker",
        "severity": "CRITICAL",
        "description": "Triggered if raw text, HTML, sentiment scores, or embeddings are detected.",
        "affected_component": "macro_event_news_regime_context",
        "remediation_guidance": "Remove raw content; preserve metadata only; no auto-dropping allowed.",
        "auto_fix_allowed": False,
        "destructive_action_allowed": False,
        "is_active": False,
    },
    {
        "blocker_id": "blocker_def_forbidden_column",
        "blocker_type": "forbidden_column_blocker",
        "severity": "CRITICAL",
        "description": "Triggered if forbidden columns (signal, buy, sell, target, prediction) appear.",
        "affected_component": "featurestore_schemas",
        "remediation_guidance": "Manual schema correction required; auto-column drop is prohibited.",
        "auto_fix_allowed": False,
        "destructive_action_allowed": False,
        "is_active": False,
    },
    {
        "blocker_id": "blocker_def_source_preservation",
        "blocker_type": "source_preservation_blocker",
        "severity": "CRITICAL",
        "description": "Triggered if any source file modification, move, or overwrite is attempted.",
        "affected_component": "data_lake_storage",
        "remediation_guidance": "Revert modifications; treat inputs as read-only.",
        "auto_fix_allowed": False,
        "destructive_action_allowed": False,
        "is_active": False,
    },
    {
        "blocker_id": "blocker_def_non_signal_acceptance",
        "blocker_type": "non_signal_acceptance_blocker",
        "severity": "CRITICAL",
        "description": "Triggered if trade recommendations or directional interpretations are claimed.",
        "affected_component": "featurestore_catalogs",
        "remediation_guidance": "Clarify that catalog entries represent descriptive regime states, not trade signals.",
        "auto_fix_allowed": False,
        "destructive_action_allowed": False,
        "is_active": False,
    },
    {
        "blocker_id": "blocker_def_component_acceptance",
        "blocker_type": "component_acceptance_blocker",
        "severity": "HIGH",
        "description": "Triggered if an upstream regime component is missing Phase 133 acceptance verification.",
        "affected_component": "upstream_regime_blocks",
        "remediation_guidance": "Run Phase 133 acceptance suite for the missing component.",
        "auto_fix_allowed": False,
        "destructive_action_allowed": False,
        "is_active": False,
    },
    {
        "blocker_id": "blocker_def_missing_quality_dep",
        "blocker_type": "missing_quality_dependency",
        "severity": "HIGH",
        "description": "Triggered if required quality scores from Phase 123/129 fall below threshold.",
        "affected_component": "quality_dependencies",
        "remediation_guidance": "Investigate quality metric calculations manually.",
        "auto_fix_allowed": False,
        "destructive_action_allowed": False,
        "is_active": False,
    },
    {
        "blocker_id": "blocker_def_missing_validation_dep",
        "blocker_type": "missing_validation_dependency",
        "severity": "HIGH",
        "description": "Triggered if upstream validation reports are absent.",
        "affected_component": "validation_dependencies",
        "remediation_guidance": "Execute required upstream validation script.",
        "auto_fix_allowed": False,
        "destructive_action_allowed": False,
        "is_active": False,
    },
    {
        "blocker_id": "blocker_def_phase_135_acceptance",
        "blocker_type": "phase_135_acceptance_blocker",
        "severity": "CRITICAL",
        "description": "Triggered if handoff prerequisites for Phase 135 Acceptance Report are incomplete.",
        "affected_component": "phase_135_handoff",
        "remediation_guidance": "Resolve all Phase 126-134 catalog prerequisites before generating final acceptance report.",
        "auto_fix_allowed": False,
        "destructive_action_allowed": False,
        "is_active": False,
    },
]


def build_regime_manual_review_blocker_store_registry(
    profile: Optional[RegimeFeatureStoreProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Construct DataFrame and summary for manual review blocker store."""
    active_profile = profile or get_regime_featurestore_profile()
    df = pd.DataFrame(CANONICAL_BLOCKER_DEFINITIONS)
    active_count = int((df["is_active"] == True).sum())
    summary = {
        "domain": MANUAL_REVIEW_BLOCKER_DOMAIN,
        "total_blocker_types": len(df),
        "active_blockers_count": active_count,
        "active_profile": active_profile.profile_name,
        "current_phase": 134,
        "target_final_phase": 160,
        "next_phase": 135,
        "auto_fix_strictly_forbidden": bool((df["auto_fix_allowed"] == False).all()),
        "status": REGIME_STORE_READY,
        "non_signal": True,
    }
    return df, summary


def summarize_regime_manual_review_blocker_store(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize blocker store DataFrame."""
    return {
        "total_blockers": len(df),
        "active_blockers": int((df["is_active"] == True).sum()) if not df.empty else 0,
        "auto_fix_allowed": False,
        "destructive_allowed": False,
    }
