# -*- coding: utf-8 -*-
"""Phase 140: Ensemble Manual Review Queue."""

from typing import Any, Dict, List
from advanced_ensemble_model_registry.ensemble_model_models import EnsembleManualReviewItem


def build_ensemble_manual_review_queue() -> List[EnsembleManualReviewItem]:
    """Build manual review items for candidate model contracts and ensemble governance.
    
    Returns:
        List[EnsembleManualReviewItem]: List of review queue items.
    """
    items = [
        EnsembleManualReviewItem(
            review_id="REV-140-001",
            finding_ref="FIND-140-INIT-001",
            ensemble_domain="candidate_model_registry",
            severity="info",
            description="Candidate model contracts successfully initialized in non-executing mode.",
            recommended_action="Confirm candidate families align with planned research scopes.",
            non_signal=True,
            auto_fix_allowed=False,
            destructive_action_allowed=False,
        ),
        EnsembleManualReviewItem(
            review_id="REV-140-002",
            finding_ref="FIND-140-INIT-002",
            ensemble_domain="ensemble_strategy_layer",
            severity="info",
            description="Ensemble strategy contracts initialized; voting/blending/stacking execution blocked.",
            recommended_action="Verify downstream Phase 141 handoff requirements before scheduling execution.",
            non_signal=True,
            auto_fix_allowed=False,
            destructive_action_allowed=False,
        ),
        EnsembleManualReviewItem(
            review_id="REV-140-003",
            finding_ref="FIND-140-INIT-003",
            ensemble_domain="candidate_model_governance",
            severity="info",
            description="Eligibility gates and compatibility matrix active; no lookahead confirmed.",
            recommended_action="Conduct regular review of GPU resource governance bounds.",
            non_signal=True,
            auto_fix_allowed=False,
            destructive_action_allowed=False,
        ),
    ]
    return items


def validate_ensemble_manual_review_queue(items: List[EnsembleManualReviewItem]) -> bool:
    """Validate manual review queue items.
    
    Args:
        items: List of review items.
        
    Returns:
        bool: True if valid, False otherwise.
    """
    if not isinstance(items, list) or len(items) == 0:
        return False
    for item in items:
        if not isinstance(item, EnsembleManualReviewItem):
            return False
        if item.auto_fix_allowed:
            return False
        if item.destructive_action_allowed:
            return False
        if not item.non_signal:
            return False
    return True


def summarize_ensemble_manual_review_queue(items: List[EnsembleManualReviewItem]) -> Dict[str, Any]:
    """Summarize manual review queue.
    
    Args:
        items: List of review items.
        
    Returns:
        Dict[str, Any]: Summary dictionary.
    """
    return {
        "total_items": len(items),
        "review_ids": [i.review_id for i in items],
        "all_auto_fix_blocked": all(not i.auto_fix_allowed for i in items),
        "all_destructive_blocked": all(not i.destructive_action_allowed for i in items),
        "all_non_signal": all(i.non_signal for i in items),
        "dry_run": True,
    }
