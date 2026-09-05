"""Phase 128: Regime Candidate State Metadata.

Defines comprehensive metadata records linking candidate state families with upstream matrices and safety policies.
"""

from typing import Dict, Tuple
import pandas as pd

from advanced_regime_rule_free.regime_rule_free_config import (
    RegimeRuleFreeProfile,
    get_default_regime_rule_free_profile,
)
from advanced_regime_rule_free.regime_rule_free_models import CandidateStateMetadataItem

CANDIDATE_STATE_METADATA_ITEMS = [
    CandidateStateMetadataItem(
        candidate_state_family="volatility",
        source_matrix_ref="regime_feature_matrix_contract",
        source_feature_refs=["rolling_std", "atr", "realized_volatility"],
        assignment_policy_ref="percentile_context_assignment_placeholder",
        quality_dependency_ref="quality_score_ge_0_70",
        validation_dependency_ref="no_lookahead_pass",
        no_lookahead_policy_ref="temporal_order_guard",
    ),
    CandidateStateMetadataItem(
        candidate_state_family="trend",
        source_matrix_ref="regime_feature_matrix_contract",
        source_feature_refs=["ma_distance", "adx_dmi", "rsi"],
        assignment_policy_ref="threshold_free_context_assignment_placeholder",
        quality_dependency_ref="drift_score_lt_0_25",
        validation_dependency_ref="no_lookahead_pass",
        no_lookahead_policy_ref="temporal_order_guard",
    ),
    CandidateStateMetadataItem(
        candidate_state_family="range",
        source_matrix_ref="regime_feature_matrix_contract",
        source_feature_refs=["bollinger_bandwidth", "range_zscore"],
        assignment_policy_ref="threshold_free_context_assignment_placeholder",
        quality_dependency_ref="quality_score_ge_0_70",
        validation_dependency_ref="no_lookahead_pass",
        no_lookahead_policy_ref="temporal_order_guard",
    ),
    CandidateStateMetadataItem(
        candidate_state_family="macro_event",
        source_matrix_ref="macro_event_context_matrix_contract",
        source_feature_refs=["macro_surprise_index", "event_impact_weight"],
        assignment_policy_ref="transition_context_placeholder",
        quality_dependency_ref="release_staleness_pass",
        validation_dependency_ref="metadata_only_news_pass",
        no_lookahead_policy_ref="release_time_alignment_guard",
    ),
    CandidateStateMetadataItem(
        candidate_state_family="news_attention",
        source_matrix_ref="news_metadata_context_matrix_contract",
        source_feature_refs=["headline_volume_24h", "urgency_flag_ratio"],
        assignment_policy_ref="threshold_free_context_assignment_placeholder",
        quality_dependency_ref="license_provenance_pass",
        validation_dependency_ref="metadata_only_news_pass",
        no_lookahead_policy_ref="publication_ts_guard",
    ),
    CandidateStateMetadataItem(
        candidate_state_family="cross_asset",
        source_matrix_ref="cross_asset_alignment_matrix_contract",
        source_feature_refs=["rolling_correlation_30d", "cross_asset_spread"],
        assignment_policy_ref="rank_context_assignment_placeholder",
        quality_dependency_ref="session_alignment_ge_0_80",
        validation_dependency_ref="timestamp_order_pass",
        no_lookahead_policy_ref="temporal_order_guard",
    ),
    CandidateStateMetadataItem(
        candidate_state_family="transition",
        source_matrix_ref="regime_feature_matrix_contract",
        source_feature_refs=["volatility_breakout", "acceleration_factor"],
        assignment_policy_ref="transition_context_placeholder",
        quality_dependency_ref="quality_score_ge_0_70",
        validation_dependency_ref="no_lookahead_pass",
        no_lookahead_policy_ref="temporal_order_guard",
    ),
    CandidateStateMetadataItem(
        candidate_state_family="uncertain",
        source_matrix_ref="regime_feature_matrix_contract",
        source_feature_refs=["missing_rate_window", "feature_drift_psi"],
        assignment_policy_ref="uncertainty_context_placeholder",
        quality_dependency_ref="fallback_trigger_pass",
        validation_dependency_ref="validation_rule_review",
        no_lookahead_policy_ref="temporal_order_guard",
    ),
]


def build_regime_candidate_state_metadata_registry(
    profile: RegimeRuleFreeProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and summary metadata for candidate state metadata."""
    active_profile = profile or get_default_regime_rule_free_profile()

    rows = []
    for m in CANDIDATE_STATE_METADATA_ITEMS:
        row = m.__dict__.copy()
        row["source_feature_count"] = len(m.source_feature_refs)
        row["current_phase"] = active_profile.current_phase
        row["next_phase"] = active_profile.next_phase
        row["target_final_phase"] = active_profile.target_final_phase
        rows.append(row)

    df = pd.DataFrame(rows)
    summary = summarize_regime_candidate_state_metadata(df)
    return df, summary


def summarize_regime_candidate_state_metadata(df: pd.DataFrame) -> Dict:
    """Summarize candidate state metadata."""
    total = len(df)
    all_non_signal = bool(df["non_signal"].all()) if not df.empty else True
    all_phase_129_ready = bool(df["phase_129_ready"].all()) if not df.empty else True

    return {
        "total_candidate_metadata_records": total,
        "all_non_signal": all_non_signal,
        "all_phase_129_ready": all_phase_129_ready,
        "status": "VALID" if all_non_signal and all_phase_129_ready else "INVALID",
    }
