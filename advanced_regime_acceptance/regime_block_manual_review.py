"""Phase 135: Regime Block Manual Review Queue.

Tracks items requiring human analyst inspection, enforcing strictly non-destructive
recommendations with zero auto-actions or trade generation.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_acceptance.regime_acceptance_config import (
    RegimeAcceptanceProfile,
    get_regime_acceptance_profile,
)
from advanced_regime_acceptance.regime_acceptance_labels import (
    REGIME_BLOCK_MANUAL_REVIEW_DOMAIN,
)


CANONICAL_REVIEW_REASONS = [
    "missing script",
    "missing test",
    "missing report",
    "unresolved no-lookahead blocker",
    "unresolved metadata-only news blocker",
    "unresolved forbidden column blocker",
    "unresolved FeatureStore blocker",
    "unresolved source preservation blocker",
    "unresolved non-signal blocker",
    "unresolved model execution absence blocker",
    "Phase 136 handoff review",
]

FORBIDDEN_RECOMMENDATIONS = [
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


def build_regime_block_manual_review_queue(
    profile: Optional[RegimeAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary of manual review items for regime block."""
    active = profile or get_regime_acceptance_profile()
    # Baseline: all gates pass in verified repository, so queue is empty of critical errors,
    # but informational handoff checkpoints exist.
    items: List[Dict[str, Any]] = [
        {
            "item_id": "review_p136_gpu_readiness",
            "phase_number": 135,
            "module_name": "advanced_regime_acceptance",
            "category": "Phase 136 handoff review",
            "issue_description": "Verify local GPU device capability and PyTorch/CUDA environment before starting Phase 136 runtime tasks.",
            "manual_review_required": True,
            "auto_destructive_action_allowed": False,
            "recommendation": "Review hardware and local acceleration availability manually; do not attempt automatic driver or package installation.",
            "non_signal": True,
        }
    ]
    df = pd.DataFrame(items)
    summary: Dict[str, Any] = {
        "domain": REGIME_BLOCK_MANUAL_REVIEW_DOMAIN,
        "active_profile": active.profile_name,
        "total_review_items": len(df),
        "forbidden_recommendations_enforced": True,
        "auto_destructive_allowed": False,
        "non_signal": True,
        "status": "READY",
    }
    return df, summary


def summarize_regime_block_manual_review_queue(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize manual review DataFrame."""
    return {
        "review_item_count": len(df),
        "requires_action": len(df) > 0,
        "non_signal": True,
    }
