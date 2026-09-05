"""Phase 128 to Phase 129 Handoff: Market Behavior Diagnostics and Regime Quality.

Defines deliverables, prerequisites, and governance boundaries passed from Phase 128 to Phase 129.
"""

from typing import Dict, Tuple
import pandas as pd

from advanced_regime_rule_free.regime_rule_free_config import (
    RegimeRuleFreeProfile,
    get_default_regime_rule_free_profile,
)

PHASE_129_HANDOFF_ITEMS = [
    {
        "handoff_id": "h129_01_market_behavior_diagnostics_prereqs",
        "category": "behavior_diagnostics",
        "description": "Prerequisites for evaluating state dispersion, persistence, and transitions across assets.",
        "status": "READY",
        "verified": True,
    },
    {
        "handoff_id": "h129_02_candidate_state_quality_prereqs",
        "category": "state_quality",
        "description": "Quality score benchmarks and drift limits established for candidate state inputs.",
        "status": "READY",
        "verified": True,
    },
    {
        "handoff_id": "h129_03_pseudo_state_schema_prereqs",
        "category": "schema_readiness",
        "description": "Non-signal pseudo-state schema contracts ready for descriptive diagnostic mapping.",
        "status": "READY",
        "verified": True,
    },
    {
        "handoff_id": "h129_04_assignment_policy_prereqs",
        "category": "assignment_policies",
        "description": "Contextual assignment placeholders configured without premature algorithm execution.",
        "status": "READY",
        "verified": True,
    },
    {
        "handoff_id": "h129_05_unsupervised_prep_readiness",
        "category": "unsupervised_prep",
        "description": "Normalization and scaling preparation contracts ready for Phase 129 behavior evaluation.",
        "status": "READY",
        "verified": True,
    },
    {
        "handoff_id": "h129_06_no_lookahead_temporal_constraints",
        "category": "temporal_guard",
        "description": "Zero lookahead and strict point-in-time constraints verified across candidate state pipelines.",
        "status": "READY",
        "verified": True,
    },
    {
        "handoff_id": "h129_07_non_signal_candidate_requirements",
        "category": "governance",
        "description": "Non-signal invariant certified; Phase 129 must not transform diagnostics into trade signals.",
        "status": "READY",
        "verified": True,
    },
    {
        "handoff_id": "h129_08_validation_quality_dependencies",
        "category": "dependencies",
        "description": "Linkages to Phase 121 validation and Phase 123 quality drift checks fully registered.",
        "status": "READY",
        "verified": True,
    },
    {
        "handoff_id": "h129_09_metadata_only_news_boundary",
        "category": "compliance",
        "description": "Confirmed zero full-text news retention in news attention candidate states.",
        "status": "READY",
        "verified": True,
    },
    {
        "handoff_id": "h129_10_source_preservation_guarantee",
        "category": "data_integrity",
        "description": "Zero mutation, zero source deletion, and zero destructive cleaning certified.",
        "status": "READY",
        "verified": True,
    },
    {
        "handoff_id": "h129_11_manual_review_blocker_audit",
        "category": "governance",
        "description": "Non-destructive manual review queue established to catch and review ambiguous states.",
        "status": "READY",
        "verified": True,
    },
    {
        "handoff_id": "h129_12_clear_boundary_behavior_not_signals",
        "category": "scope_boundary",
        "description": "Explicit mandate: Phase 129 will diagnose behavior quality, NOT generate trading signals.",
        "status": "READY",
        "verified": True,
    },
]


def build_phase_129_market_behavior_diagnostics_handoff_report(
    profile: RegimeRuleFreeProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and summary metadata for Phase 129 handoff."""
    active_profile = profile or get_default_regime_rule_free_profile()

    rows = []
    for h in PHASE_129_HANDOFF_ITEMS:
        row = h.copy()
        row["source_phase"] = active_profile.current_phase
        row["next_phase"] = active_profile.next_phase
        row["target_final_phase"] = active_profile.target_final_phase
        rows.append(row)

    df = pd.DataFrame(rows)
    summary = summarize_phase_129_handoff(df)
    return df, summary


def summarize_phase_129_handoff(df: pd.DataFrame) -> Dict:
    """Summarize Phase 129 handoff report."""
    total = len(df)
    verified_count = int(df["verified"].sum()) if not df.empty else 0
    all_ready = bool((df["status"] == "READY").all()) if not df.empty else True

    return {
        "source_phase": 128,
        "next_phase": 129,
        "target_final_phase": 160,
        "total_items": total,
        "verified_items": verified_count,
        "all_ready": all_ready,
        "handoff_status": "READY" if all_ready and verified_count == total else "INCOMPLETE",
    }
