# -*- coding: utf-8 -*-
"""Phase 143: Explainability Manual Review Queue."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_explainability_attribution.explainability_config import (
    ExplainabilityProfile,
    get_explainability_profile,
)


def build_explainability_manual_review_queue(
    profile: Optional[ExplainabilityProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the DataFrame of explainability manual review items."""
    prof = profile or get_explainability_profile()

    review_items = [
        ("review_global_tree_shap_brent", "contract_review", "global_explanation", "Verify tree SHAP attribution contract parameters for Brent model", "Verify baseline background dataset size and feature alignment"),
        ("review_local_lime_gold", "contract_review", "local_explanation", "Verify LIME perturbation configuration for Gold baseline model", "Inspect kernel width and sample count before any future execution"),
        ("review_drift_linkage_brent", "linkage_review", "attribution_drift", "Inspect PSI attribution drift linkage thresholds", "Confirm warning and alert thresholds align with Phase 142 drift registry"),
        ("review_counterfactual_recourse_fx", "placeholder_review", "counterfactual", "Review counterfactual recourse feasibility constraints", "Check bounding box on USD/TRY macro features to prevent unrealistic counterfactuals"),
    ]

    rows: List[Dict[str, Any]] = []
    for rid, itype, domain, reason, action in review_items:
        rows.append({
            "review_id": rid,
            "item_type": itype,
            "domain": domain,
            "reason": reason,
            "required_action": action,
            "urgency": "medium",
            "status": "pending",
            "manual_review_required": True,
            "non_signal": True,
            "official_approval": False,
            "production_ready": False,
            "broker_ready": False,
        })

    df = pd.DataFrame(rows)
    summary = summarize_explainability_manual_review(df)
    return df, summary


def summarize_explainability_manual_review(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize explainability manual review queue."""
    return {
        "total_manual_reviews": len(df),
        "all_pending": bool((df["status"] == "pending").all()) if not df.empty else True,
        "all_manual_review_required": bool(df["manual_review_required"].all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "current_phase": 143,
        "next_phase": 144,
        "target_final_phase": 160,
    }
