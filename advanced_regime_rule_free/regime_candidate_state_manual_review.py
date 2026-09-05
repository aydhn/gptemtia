"""Phase 128: Regime Candidate State Manual Review Queue.

Provides an offline, non-destructive manual review queue for human researchers.
Automated destructive actions (auto-delete, auto-impute, clustering, trading approval) are strictly blocked.
"""

from typing import Dict, Tuple
import pandas as pd

from advanced_regime_rule_free.regime_rule_free_config import (
    RegimeRuleFreeProfile,
    get_default_regime_rule_free_profile,
)
from advanced_regime_rule_free.regime_rule_free_models import CandidateStateManualReviewItem

MANUAL_REVIEW_QUEUE_ITEMS = [
    CandidateStateManualReviewItem(
        review_id="rev_001_unresolved_matrix_validation",
        review_domain="matrix_validation",
        reason="Unresolved matrix validation dependency requiring human inspection.",
        source_ref="technical_indicator_matrix_contract",
    ),
    CandidateStateManualReviewItem(
        review_id="rev_002_unresolved_quality_dependency",
        review_domain="quality_dependency",
        reason="Elevated feature drift or missingness approaching gating threshold.",
        source_ref="quality_drift_factor_family",
    ),
    CandidateStateManualReviewItem(
        review_id="rev_003_insufficient_candidate_context",
        review_domain="context_sufficiency",
        reason="Context observations below minimal threshold for candidate assignment.",
        source_ref="candidate_state_uncertain_context",
    ),
    CandidateStateManualReviewItem(
        review_id="rev_004_candidate_state_schema_ambiguity",
        review_domain="schema_governance",
        reason="Unassigned or novel feature tag requiring schema classification confirmation.",
        source_ref="candidate_state_schema",
    ),
    CandidateStateManualReviewItem(
        review_id="rev_005_pseudo_state_schema_ambiguity",
        review_domain="schema_governance",
        reason="Ambiguity in pseudo-state mapping note for future unsupervised phases.",
        source_ref="pseudo_state_schema",
    ),
    CandidateStateManualReviewItem(
        review_id="rev_006_clustering_input_readiness_review",
        review_domain="clustering_prep",
        reason="Verification of feature scaling and normalization suitability prior to Phase 129.",
        source_ref="clustering_input_contracts",
    ),
    CandidateStateManualReviewItem(
        review_id="rev_007_no_lookahead_policy_review",
        review_domain="temporal_integrity",
        reason="Verification of point-in-time timestamp alignment across release event windows.",
        source_ref="macro_event_context_matrix_contract",
    ),
    CandidateStateManualReviewItem(
        review_id="rev_008_news_metadata_boundary_review",
        review_domain="copyright_boundary",
        reason="Audit confirming zero full-text news retention across news attention candidate states.",
        source_ref="news_metadata_context_matrix_contract",
    ),
    CandidateStateManualReviewItem(
        review_id="rev_009_phase_129_readiness_review",
        review_domain="phase_handoff",
        reason="Verification that all candidate state quality prerequisites are satisfied before Phase 129.",
        source_ref="phase_129_handoff",
    ),
]

FORBIDDEN_MANUAL_REVIEW_ACTIONS = [
    "auto_delete",
    "auto_overwrite",
    "auto_impute",
    "enable_scraping",
    "generate_signal",
    "run_clustering",
    "train_model",
    "run_dimensionality_reduction",
    "approve_production",
    "approve_broker_readiness",
]


def build_regime_candidate_state_manual_review_queue(
    profile: RegimeRuleFreeProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and summary metadata for candidate state manual review queue."""
    active_profile = profile or get_default_regime_rule_free_profile()

    rows = []
    for item in MANUAL_REVIEW_QUEUE_ITEMS:
        row = item.__dict__.copy()
        row["current_phase"] = active_profile.current_phase
        row["next_phase"] = active_profile.next_phase
        row["target_final_phase"] = active_profile.target_final_phase
        rows.append(row)

    df = pd.DataFrame(rows)
    summary = summarize_candidate_state_manual_review_queue(df)
    return df, summary


def summarize_candidate_state_manual_review_queue(df: pd.DataFrame) -> Dict:
    """Summarize manual review queue."""
    total = len(df)
    all_signoff_required = bool(df["requires_human_signoff"].all()) if not df.empty else True
    all_destructive_blocked = bool((~df["destructive_action_permitted"]).all()) if not df.empty else True
    all_autofix_blocked = bool((~df["auto_fix_permitted"]).all()) if not df.empty else True

    return {
        "total_queued_items": total,
        "all_require_human_signoff": all_signoff_required,
        "all_destructive_blocked": all_destructive_blocked,
        "all_autofix_blocked": all_autofix_blocked,
        "forbidden_automated_actions": list(FORBIDDEN_MANUAL_REVIEW_ACTIONS),
        "queue_status": "ACTIVE_NON_DESTRUCTIVE" if all_destructive_blocked and all_autofix_blocked else "UNSAFE",
    }
