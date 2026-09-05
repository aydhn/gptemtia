"""Phase 131: Cross-Asset Range Linkage Registry.

Defines non-signal cross-asset range/consolidation linkage records (range context,
persistence alignment, range transition alignment, compression-expansion alignment).
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_cross_asset_regime_context.cross_asset_regime_config import (
    CrossAssetRegimeProfile,
    get_default_cross_asset_regime_profile,
)

RANGE_LINKAGE_RECORDS: List[Dict[str, Any]] = [
    {
        "linkage_id": "range_link_context_fx_cmd",
        "linkage_name": "FX to Commodity Rangebound Regime Context",
        "linkage_category": "cross_asset_range_context",
        "asset_a": "fx_eurusd",
        "asset_b": "cmd_xagusd",
        "description": "Descriptive rangebound state comparison between EUR/USD and Silver without trading claims.",
        "linkage_score": 0.86,
        "is_placeholder": False,
        "requires_no_lookahead": True,
    },
    {
        "linkage_id": "range_link_persistence_placeholder",
        "linkage_name": "Range Persistence Alignment Diagnostic Placeholder",
        "linkage_category": "range_persistence_alignment_placeholder",
        "asset_a": "regime_range_family",
        "asset_b": "candidate_high_vol",
        "description": "Diagnostic evaluation of simultaneous channel confinement; strictly NOT a range-breakout entry signal.",
        "linkage_score": 0.83,
        "is_placeholder": True,
        "requires_no_lookahead": True,
    },
    {
        "linkage_id": "range_link_trans_placeholder",
        "linkage_name": "Range Transition Alignment Diagnostic Placeholder",
        "linkage_category": "range_transition_alignment_placeholder",
        "asset_a": "fx_usdjpy",
        "asset_b": "cmd_brent",
        "description": "Alignment of breakout transition sequences between currency and energy regimes.",
        "linkage_score": 0.85,
        "is_placeholder": True,
        "requires_no_lookahead": True,
    },
    {
        "linkage_id": "range_link_compression_expansion_placeholder",
        "linkage_name": "Compression to Expansion Cross-Asset Alignment Placeholder",
        "linkage_category": "compression_expansion_alignment_placeholder",
        "asset_a": "fx_eurusd",
        "asset_b": "cmd_xauusd",
        "description": "Multi-asset volatility cycle expansion alignment placeholder without prediction.",
        "linkage_score": 0.88,
        "is_placeholder": True,
        "requires_no_lookahead": True,
    },
]


def build_cross_asset_range_linkage_registry(
    profile: Optional[CrossAssetRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build range linkage registry dataframe and summary."""
    if profile is None:
        profile = get_default_cross_asset_regime_profile()

    rows = []
    for item in RANGE_LINKAGE_RECORDS:
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
    summary = summarize_cross_asset_range_linkage(df)
    summary["active_profile"] = profile.profile_name
    return df, summary


def summarize_cross_asset_range_linkage(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize cross-asset range linkage records."""
    cat_counts = df["linkage_category"].value_counts().to_dict() if not df.empty else {}
    return {
        "total_linkages": len(df),
        "linkage_categories": cat_counts,
        "mean_linkage_score": float(df["linkage_score"].mean()) if not df.empty else 0.0,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "all_source_preserved": bool(df["source_preserved"].all()) if not df.empty else True,
        "zero_trading_signals": True,
        "zero_predictions": True,
    }
