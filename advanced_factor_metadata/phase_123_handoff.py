"""Phase 123 Feature Quality and Drift Diagnostics Handoff.

Prepares factor-level quality, drift baseline, missingness, and stability
specifications required for Phase 123 diagnostics.
Strictly non-signal and research-only.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_factor_metadata.factor_metadata_config import (
    FactorMetadataProfile,
    get_default_factor_metadata_profile,
)

PHASE_123_HANDOFF_ITEMS: List[Dict[str, Any]] = [
    {
        "handoff_id": "HO-123-01",
        "topic": "factor_level_missingness_diagnostics_prerequisites",
        "description": "Baseline feature missingness thresholds (<= 35%) mapped to each factor family.",
        "status": "READY",
        "downstream_consumer": "Phase 123 Missingness Diagnostics",
    },
    {
        "handoff_id": "HO-123-02",
        "topic": "factor_level_infinite_value_diagnostics_prerequisites",
        "description": "Zero +inf/-inf invariant rules mapped to all numerical factor contracts.",
        "status": "READY",
        "downstream_consumer": "Phase 123 Infinite Value Diagnostics",
    },
    {
        "handoff_id": "HO-123-03",
        "topic": "factor_level_duplicate_namespace_diagnostics_prerequisites",
        "description": "Namespace uniqueness standards established with factor_ prefix and snake_case.",
        "status": "READY",
        "downstream_consumer": "Phase 123 Namespace Diagnostics",
    },
    {
        "handoff_id": "HO-123-04",
        "topic": "factor_level_stability_diagnostics_prerequisites",
        "description": "Rolling window lookback lengths defined for statistical stability assessments.",
        "status": "READY",
        "downstream_consumer": "Phase 123 Factor Stability Engine",
    },
    {
        "handoff_id": "HO-123-05",
        "topic": "factor_level_drift_diagnostics_prerequisites",
        "description": "Distributional reference windows configured for KS-test and Wasserstein drift tests.",
        "status": "READY",
        "downstream_consumer": "Phase 123 Distributional Drift Monitor",
    },
    {
        "handoff_id": "HO-123-06",
        "topic": "feature_availability_by_factor_family",
        "description": "Dependency coverage matrix verifying all required inputs from Phases 116-121.",
        "status": "READY",
        "downstream_consumer": "Phase 123 Availability Checker",
    },
    {
        "handoff_id": "HO-123-07",
        "topic": "validation_blockers_by_factor_family",
        "description": "Validation dependency gates preventing unverified features from entering drift evaluation.",
        "status": "READY",
        "downstream_consumer": "Phase 123 Validation Gatekeeper",
    },
    {
        "handoff_id": "HO-123-08",
        "topic": "quality_dependencies_by_factor_family",
        "description": "Quality criteria thresholds formalized in factor quality dependency registry.",
        "status": "READY",
        "downstream_consumer": "Phase 123 Quality Scorer",
    },
    {
        "handoff_id": "HO-123-09",
        "topic": "macro_calendar_news_metadata_only_quality_checks",
        "description": "Strict verification that news factors remain frequency-based and text-free.",
        "status": "READY",
        "downstream_consumer": "Phase 123 Metadata Hygiene Auditor",
    },
    {
        "handoff_id": "HO-123-10",
        "topic": "cross_asset_context_quality_dependencies",
        "description": "Backward-asof timestamp alignment verification across multi-asset calendars.",
        "status": "READY",
        "downstream_consumer": "Phase 123 Cross-Asset Alignment Quality",
    },
    {
        "handoff_id": "HO-123-11",
        "topic": "manual_review_blockers_before_quality_drift_diagnostics",
        "description": "Review queue integration ensuring placeholder factors require sign-off before drift monitoring.",
        "status": "READY",
        "downstream_consumer": "Phase 123 Governance Blocker Interface",
    },
]


def build_phase_123_feature_quality_drift_handoff_report(
    profile: FactorMetadataProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build Phase 123 Feature Quality and Drift Diagnostics Handoff Report."""
    active_profile = profile or get_default_factor_metadata_profile()

    records = [dict(item) for item in PHASE_123_HANDOFF_ITEMS]
    df = pd.DataFrame(records)

    ready_count = sum(1 for r in records if r["status"] == "READY")
    total_count = len(records)

    summary = {
        "active_profile": active_profile.name,
        "source_phase": 122,
        "next_phase": 123,
        "next_phase_name": "Feature Quality and Drift Diagnostics",
        "target_final_phase": 160,
        "total_items": total_count,
        "ready_items": ready_count,
        "handoff_status": "READY" if ready_count == total_count else "IN_PROGRESS",
        "non_signal": True,
    }
    return df, summary


def summarize_phase_123_handoff(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize Phase 123 handoff DataFrame."""
    total = len(df)
    ready = int((df["status"] == "READY").sum()) if "status" in df else 0
    return {
        "total_items": total,
        "ready_items": ready,
        "handoff_status": "READY" if ready == total else "IN_PROGRESS",
        "source_phase": 122,
        "next_phase": 123,
        "non_signal": True,
    }
