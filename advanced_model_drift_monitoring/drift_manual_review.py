"""Drift Manual Review Workflows for Phase 142.

Enforces human-in-the-loop manual review contracts for drift findings,
guaranteeing that zero automated replacements, retirements, or retrainings
occur without dual engineering and quantitative signoffs.
"""

from __future__ import annotations

from dataclasses import asdict
from typing import Any, Dict, List

from advanced_model_drift_monitoring.model_drift_models import DriftManualReviewItem


def build_drift_manual_review_items() -> List[DriftManualReviewItem]:
    """Builds standard manual review workflow items for drift governance."""
    return [
        DriftManualReviewItem(
            review_id="rev_drift_001_candidate_models",
            target_name="candidate_models_drift_review",
            drift_domain="model_drift",
            status="pending_review",
            findings_summary="Review baseline and ensemble candidate models for distributional divergence.",
            required_signoffs=["ml_lead", "quant_researcher", "risk_manager"],
            is_approved=False,
            notes="Requires validation on held-out commodity and forex segments before any promotion.",
            metadata={"priority": "high", "phase": 142},
        ),
        DriftManualReviewItem(
            review_id="rev_drift_002_feature_quality_linkage",
            target_name="feature_quality_linkage_review",
            drift_domain="feature_quality_drift",
            status="pending_review",
            findings_summary="Review missingness and schema consistency against Phase 123 diagnostics.",
            required_signoffs=["data_engineer", "ml_lead"],
            is_approved=False,
            notes="Verify zero automated imputation occurred in upstream pipelines.",
            metadata={"priority": "medium", "phase": 142},
        ),
        DriftManualReviewItem(
            review_id="rev_drift_003_calibration_shift",
            target_name="calibration_shift_review",
            drift_domain="calibration_drift",
            status="pending_review",
            findings_summary="Review ECE and Brier score divergence against Phase 141 calibration baselines.",
            required_signoffs=["quant_researcher", "model_validator"],
            is_approved=False,
            notes="Verify temperature scaling and conformal prediction intervals maintain coverage bounds.",
            metadata={"priority": "high", "phase": 142},
        ),
    ]


def summarize_drift_manual_reviews(
    items: List[DriftManualReviewItem],
) -> Dict[str, Any]:
    """Summarizes manual review items and signoff status."""
    total = len(items)
    approved = sum(1 for item in items if item.is_approved)
    pending = total - approved

    return {
        "total_reviews": total,
        "approved_count": approved,
        "pending_count": pending,
        "all_approved": approved == total,
        "reviews": [asdict(item) for item in items],
    }
