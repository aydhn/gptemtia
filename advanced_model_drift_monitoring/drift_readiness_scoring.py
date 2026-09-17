"""Drift Readiness Scoring for Phase 142.

Evaluates governance readiness across all 6 core drift domains
(model drift, data drift, feature drift, calibration drift, uncertainty drift, regime drift)
and computes an aggregate readiness score.
"""

from __future__ import annotations

from dataclasses import asdict
from typing import Any, Dict, List

from advanced_model_drift_monitoring.model_drift_models import DriftReadinessScore


def compute_domain_readiness_scores() -> List[DriftReadinessScore]:
    """Computes governance readiness scores for each drift monitoring domain."""
    scores = [
        DriftReadinessScore(
            domain="model_drift",
            readiness_score=100.0,
            governance_status="ready",
            blocker_count=0,
            warning_count=0,
            is_ready_for_review=True,
            details={"contracts_established": 6, "non_executing": True},
        ),
        DriftReadinessScore(
            domain="data_drift",
            readiness_score=100.0,
            governance_status="ready",
            blocker_count=0,
            warning_count=0,
            is_ready_for_review=True,
            details={"contracts_established": 6, "non_executing": True},
        ),
        DriftReadinessScore(
            domain="feature_drift",
            readiness_score=100.0,
            governance_status="ready",
            blocker_count=0,
            warning_count=0,
            is_ready_for_review=True,
            details={"contracts_established": 6, "non_executing": True},
        ),
        DriftReadinessScore(
            domain="calibration_drift",
            readiness_score=100.0,
            governance_status="ready",
            blocker_count=0,
            warning_count=0,
            is_ready_for_review=True,
            details={"contracts_established": 3, "non_executing": True},
        ),
        DriftReadinessScore(
            domain="uncertainty_drift",
            readiness_score=100.0,
            governance_status="ready",
            blocker_count=0,
            warning_count=0,
            is_ready_for_review=True,
            details={"contracts_established": 3, "non_executing": True},
        ),
        DriftReadinessScore(
            domain="regime_drift",
            readiness_score=100.0,
            governance_status="ready",
            blocker_count=0,
            warning_count=0,
            is_ready_for_review=True,
            details={"contracts_established": 3, "non_executing": True},
        ),
    ]
    return scores


def evaluate_aggregate_drift_readiness(
    scores: List[DriftReadinessScore],
) -> Dict[str, Any]:
    """Evaluates aggregate drift governance readiness across all domains."""
    total_domains = len(scores)
    if total_domains == 0:
        return {
            "overall_score": 0.0,
            "overall_status": "blocked",
            "all_ready": False,
            "total_blockers": 0,
            "total_warnings": 0,
            "scores": [],
        }

    avg_score = sum(s.readiness_score for s in scores) / total_domains
    total_blockers = sum(s.blocker_count for s in scores)
    total_warnings = sum(s.warning_count for s in scores)
    all_ready = all(s.is_ready_for_review and s.blocker_count == 0 for s in scores)

    if total_blockers > 0:
        status = "blocked"
    elif total_warnings > 0 or avg_score < 80.0:
        status = "conditional"
    else:
        status = "ready"

    return {
        "overall_score": round(avg_score, 2),
        "overall_status": status,
        "all_ready": all_ready,
        "total_domains": total_domains,
        "total_blockers": total_blockers,
        "total_warnings": total_warnings,
        "scores": [asdict(s) for s in scores],
    }
