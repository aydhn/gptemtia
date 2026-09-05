"""Phase 131: Cross-Asset Regime Context Contracts.

Defines formal contractual specifications governing cross-asset joins, alignment rules,
timestamp policies, quality gates, and non-signal boundaries.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_cross_asset_regime_context.cross_asset_regime_config import (
    CrossAssetRegimeProfile,
    get_default_cross_asset_regime_profile,
)

CONTEXT_CONTRACTS: List[Dict[str, Any]] = [
    {
        "contract_name": "contract_fx_to_commodity_context",
        "relationship_type": "volatility_linkage_context",
        "left_entity_type": "fx_pair",
        "right_entity_type": "commodity_symbol",
        "timestamp_policy_ref": "utc_monotonic_timestamp_policy",
        "asof_policy_ref": "backward_asof_join_policy",
        "validation_dependency_ref": "phase_121_no_lookahead_validation",
        "quality_dependency_ref": "phase_123_quality_drift_gate",
        "source_phase_refs": ["Phase 119", "Phase 126", "Phase 127", "Phase 130"],
        "metadata_only_news_required": True,
        "no_lookahead_required": True,
        "non_signal_required": True,
        "manual_review_required": False,
    },
    {
        "contract_name": "contract_fx_to_macro_context",
        "relationship_type": "macro_sensitivity_context",
        "left_entity_type": "fx_pair",
        "right_entity_type": "macro_indicator",
        "timestamp_policy_ref": "utc_monotonic_timestamp_policy",
        "asof_policy_ref": "backward_release_lag_asof_policy",
        "validation_dependency_ref": "phase_121_no_lookahead_validation",
        "quality_dependency_ref": "phase_124_feature_store_metadata",
        "source_phase_refs": ["Phase 109", "Phase 120", "Phase 127"],
        "metadata_only_news_required": True,
        "no_lookahead_required": True,
        "non_signal_required": True,
        "manual_review_required": False,
    },
    {
        "contract_name": "contract_commodity_to_macro_context",
        "relationship_type": "macro_sensitivity_context",
        "left_entity_type": "commodity_symbol",
        "right_entity_type": "macro_indicator",
        "timestamp_policy_ref": "utc_monotonic_timestamp_policy",
        "asof_policy_ref": "backward_release_lag_asof_policy",
        "validation_dependency_ref": "phase_121_no_lookahead_validation",
        "quality_dependency_ref": "phase_123_quality_drift_gate",
        "source_phase_refs": ["Phase 108", "Phase 109", "Phase 120"],
        "metadata_only_news_required": True,
        "no_lookahead_required": True,
        "non_signal_required": True,
        "manual_review_required": False,
    },
    {
        "contract_name": "contract_macro_calendar_context",
        "relationship_type": "event_sensitivity_context",
        "left_entity_type": "macro_indicator",
        "right_entity_type": "calendar_event",
        "timestamp_policy_ref": "scheduled_event_window_policy",
        "asof_policy_ref": "backward_asof_join_policy",
        "validation_dependency_ref": "phase_121_no_lookahead_validation",
        "quality_dependency_ref": "phase_124_feature_store_metadata",
        "source_phase_refs": ["Phase 110", "Phase 120"],
        "metadata_only_news_required": True,
        "no_lookahead_required": True,
        "non_signal_required": True,
        "manual_review_required": False,
    },
    {
        "contract_name": "contract_calendar_news_context",
        "relationship_type": "news_metadata_linkage_context",
        "left_entity_type": "calendar_event",
        "right_entity_type": "news_metadata_tag",
        "timestamp_policy_ref": "metadata_only_window_policy",
        "asof_policy_ref": "backward_asof_join_policy",
        "validation_dependency_ref": "metadata_only_news_boundary",
        "quality_dependency_ref": "phase_123_quality_drift_gate",
        "source_phase_refs": ["Phase 111", "Phase 120", "Phase 130"],
        "metadata_only_news_required": True,
        "no_lookahead_required": True,
        "non_signal_required": True,
        "manual_review_required": False,
    },
    {
        "contract_name": "contract_cross_asset_transition_alignment",
        "relationship_type": "transition_alignment_context",
        "left_entity_type": "regime_family",
        "right_entity_type": "transition_context",
        "timestamp_policy_ref": "utc_monotonic_timestamp_policy",
        "asof_policy_ref": "backward_asof_join_policy",
        "validation_dependency_ref": "phase_130_transition_no_lookahead",
        "quality_dependency_ref": "phase_130_transition_stability_diagnostics",
        "source_phase_refs": ["Phase 128", "Phase 129", "Phase 130"],
        "metadata_only_news_required": True,
        "no_lookahead_required": True,
        "non_signal_required": True,
        "manual_review_required": False,
    },
]


def build_cross_asset_regime_context_contract_registry(
    profile: Optional[CrossAssetRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build context contract registry dataframe and summary."""
    if profile is None:
        profile = get_default_cross_asset_regime_profile()

    rows = []
    for item in CONTEXT_CONTRACTS:
        row = dict(item)
        row["non_signal"] = True
        row["source_preserved"] = True
        row["official_approval"] = False
        row["production_ready"] = False
        row["broker_ready"] = False
        row["contains_target_or_prediction"] = False
        row["contains_trading_recommendation"] = False
        rows.append(row)

    df = pd.DataFrame(rows)
    summary = summarize_cross_asset_context_contracts(df)
    summary["active_profile"] = profile.profile_name
    return df, summary


def validate_cross_asset_context_contract(contract: Dict[str, Any]) -> Dict[str, Any]:
    """Validate a single context contract dictionary against strict invariants."""
    required_fields = [
        "contract_name",
        "relationship_type",
        "left_entity_type",
        "right_entity_type",
        "timestamp_policy_ref",
        "asof_policy_ref",
        "validation_dependency_ref",
        "quality_dependency_ref",
        "no_lookahead_required",
        "non_signal_required",
    ]
    missing = [f for f in required_fields if f not in contract]
    if missing:
        return {
            "valid": False,
            "contract_name": contract.get("contract_name", "unknown"),
            "error": f"Missing required fields: {missing}",
        }

    if not contract.get("no_lookahead_required", False):
        return {"valid": False, "contract_name": contract["contract_name"], "error": "no_lookahead_required must be True"}

    if not contract.get("non_signal_required", False):
        return {"valid": False, "contract_name": contract["contract_name"], "error": "non_signal_required must be True"}

    return {
        "valid": True,
        "contract_name": contract["contract_name"],
        "non_signal": True,
        "no_lookahead": True,
    }


def summarize_cross_asset_context_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize cross-asset context contracts."""
    return {
        "total_contracts": len(df),
        "all_non_signal_required": bool(df["non_signal_required"].all()) if not df.empty else True,
        "all_no_lookahead_required": bool(df["no_lookahead_required"].all()) if not df.empty else True,
        "all_metadata_only_news_required": bool(df["metadata_only_news_required"].all()) if not df.empty else True,
        "all_source_preserved": bool(df["source_preserved"].all()) if not df.empty else True,
        "zero_trading_signals": True,
        "zero_predictions": True,
    }
