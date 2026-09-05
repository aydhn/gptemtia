"""Phase 131: Cross-Asset Transition Alignment Registry.

Defines transition alignment specifications connecting Phase 130 state transition
sequences across FX, commodities, macro, and event domains.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_cross_asset_regime_context.cross_asset_regime_config import (
    CrossAssetRegimeProfile,
    get_default_cross_asset_regime_profile,
)

TRANSITION_ALIGNMENT_RECORDS: List[Dict[str, Any]] = [
    {
        "alignment_id": "trans_align_fx_cmd",
        "alignment_name": "FX to Commodity Transition Sequence Alignment",
        "alignment_category": "fx_commodity_transition_alignment_placeholder",
        "primary_domain": "fx",
        "secondary_domain": "commodity",
        "phase_130_dependency": "state_transition_continuity",
        "description": "Chronological alignment of regime shift timestamps between EUR/USD and Gold.",
        "readiness_score": 0.88,
        "is_placeholder": True,
        "requires_no_lookahead": True,
    },
    {
        "alignment_id": "trans_align_fx_macro",
        "alignment_name": "FX to Macro Tightening/Easing Transition Alignment",
        "alignment_category": "fx_macro_transition_alignment_placeholder",
        "primary_domain": "fx",
        "secondary_domain": "macro",
        "phase_130_dependency": "macro_event_transition_context",
        "description": "Mapping policy rate hike cycle transitions to currency regime exhaustion.",
        "readiness_score": 0.86,
        "is_placeholder": True,
        "requires_no_lookahead": True,
    },
    {
        "alignment_id": "trans_align_cmd_macro",
        "alignment_name": "Commodity to Inflation Transition Alignment",
        "alignment_category": "commodity_macro_transition_alignment_placeholder",
        "primary_domain": "commodity",
        "secondary_domain": "macro",
        "phase_130_dependency": "macro_event_transition_context",
        "description": "Mapping inflation surprise regimes to commodity volatility transitions.",
        "readiness_score": 0.87,
        "is_placeholder": True,
        "requires_no_lookahead": True,
    },
    {
        "alignment_id": "trans_align_macro_event",
        "alignment_name": "Macro Event Window Transition Alignment",
        "alignment_category": "macro_event_transition_alignment_placeholder",
        "primary_domain": "macro",
        "secondary_domain": "calendar",
        "phase_130_dependency": "regime_state_sequence_contracts",
        "description": "State persistence surrounding scheduled high-impact release windows.",
        "readiness_score": 0.90,
        "is_placeholder": True,
        "requires_no_lookahead": True,
    },
    {
        "alignment_id": "trans_align_cross_domain",
        "alignment_name": "Cross-Domain State Sequence Sequence Alignment",
        "alignment_category": "cross_domain_state_sequence_alignment_placeholder",
        "primary_domain": "multi_asset",
        "secondary_domain": "multi_domain",
        "phase_130_dependency": "candidate_state_sequence_schema",
        "description": "Universal alignment schema guaranteeing synchronized backward-looking timestamps.",
        "readiness_score": 0.91,
        "is_placeholder": True,
        "requires_no_lookahead": True,
    },
]


def build_cross_asset_transition_alignment_registry(
    profile: Optional[CrossAssetRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build transition alignment registry dataframe and summary."""
    if profile is None:
        profile = get_default_cross_asset_regime_profile()

    rows = []
    for item in TRANSITION_ALIGNMENT_RECORDS:
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
    summary = summarize_cross_asset_transition_alignment(df)
    summary["active_profile"] = profile.profile_name
    return df, summary


def summarize_cross_asset_transition_alignment(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize transition alignment items and Phase 130 linkages."""
    cat_counts = df["alignment_category"].value_counts().to_dict() if not df.empty else {}
    return {
        "total_alignments": len(df),
        "alignment_categories": cat_counts,
        "mean_readiness_score": float(df["readiness_score"].mean()) if not df.empty else 0.0,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "all_source_preserved": bool(df["source_preserved"].all()) if not df.empty else True,
        "all_require_no_lookahead": bool(df["requires_no_lookahead"].all()) if not df.empty else True,
        "zero_trading_signals": True,
        "zero_predictions": True,
    }
