"""Phase 133: Regime Manual Review Acceptance Queue.

Defines the non-destructive inspection queue for human analysts.
Explicitly prohibits destructive automated remediation, model fitting, and trading approval.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_validation_acceptance.regime_validation_acceptance_config import (
    RegimeValidationAcceptanceProfile,
    get_default_regime_validation_acceptance_profile,
)

PERMITTED_REVIEW_TASKS = [
    ("MR_01_NO_LOOKAHEAD", "no_lookahead_acceptance_domain", "regime_pipeline", "inspect no-lookahead blockers", "acceptance_info"),
    ("MR_02_TIMESTAMP_ORDER", "timestamp_order_acceptance_domain", "timestamp_alignment", "inspect timestamp ordering blockers", "acceptance_info"),
    ("MR_03_METADATA_ONLY_NEWS", "metadata_only_news_acceptance_domain", "news_context", "inspect metadata-only news blockers", "acceptance_info"),
    ("MR_04_FORBIDDEN_COLUMN", "forbidden_column_acceptance_domain", "schema_validation", "inspect forbidden column blockers", "acceptance_info"),
    ("MR_05_SOURCE_PRESERVATION", "source_preservation_acceptance_domain", "datalake_storage", "inspect source preservation blockers", "acceptance_info"),
    ("MR_06_COMPONENT_ACCEPTANCE", "matrix_validation_acceptance_domain", "regime_components", "inspect component acceptance blockers", "acceptance_info"),
    ("MR_07_VALIDATION_DEPENDENCY", "validation_dependency_acceptance_domain", "phase_121_to_132", "inspect validation dependency blockers", "acceptance_info"),
    ("MR_08_QUALITY_DEPENDENCY", "quality_dependency_acceptance_domain", "quality_metrics", "inspect quality dependency blockers", "acceptance_info"),
    ("MR_09_PHASE_134_READINESS", "phase_134_handoff_domain", "featurestore_handoff", "inspect Phase 134 blockers", "acceptance_info"),
]

FORBIDDEN_REVIEW_ACTIONS = [
    "auto-delete",
    "auto-overwrite",
    "auto-impute",
    "enable scraping",
    "download article body",
    "generate sentiment",
    "generate embedding",
    "generate signal",
    "train model",
    "run clustering",
    "approve production",
    "approve broker readiness",
]


def build_regime_manual_review_acceptance_queue(
    profile: Optional[RegimeValidationAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for the manual review queue."""
    p = profile or get_default_regime_validation_acceptance_profile()

    rows = []
    for item_id, domain, component, suggestion, severity in PERMITTED_REVIEW_TASKS:
        rows.append(
            {
                "review_id": item_id,
                "domain": domain,
                "subject_component": component,
                "suggested_action": suggestion,
                "severity": severity,
                "status": "CLEAR",
                "destructive_action_allowed": False,
                "auto_fix_allowed": False,
                "auto_drop_allowed": False,
                "non_signal": True,
                "profile_name": p.profile_name,
                "official_approval": False,
                "production_ready": False,
                "broker_ready": False,
            }
        )

    df = pd.DataFrame(rows)
    summary = {
        "total_queue_items": len(df),
        "pending_critical_reviews": 0,
        "destructive_actions_allowed": False,
        "profile_name": p.profile_name,
        "non_signal": True,
        "source_preserved": True,
    }
    return df, summary


def summarize_regime_manual_review_acceptance_queue(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize manual review queue DataFrame."""
    total = len(df)
    return {
        "total_items": total,
        "zero_destructive_actions": bool((~df["destructive_action_allowed"]).all()) if "destructive_action_allowed" in df.columns else True,
        "non_signal": True,
    }
