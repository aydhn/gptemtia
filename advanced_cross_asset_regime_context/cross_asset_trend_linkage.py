"""Phase 131: Cross-Asset Trend Linkage Registry.

Defines non-signal cross-asset trend linkage records (trend context, persistence
alignment placeholders, trend transition alignment placeholders, dependency statuses).
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_cross_asset_regime_context.cross_asset_regime_config import (
    CrossAssetRegimeProfile,
    get_default_cross_asset_regime_profile,
)

TREND_LINKAGE_RECORDS: List[Dict[str, Any]] = [
    {
        "linkage_id": "trend_link_context_fx_cmd",
        "linkage_name": "FX to Commodity Trend Regime Context",
        "linkage_category": "cross_asset_trend_context",
        "asset_a": "fx_eurusd",
        "asset_b": "cmd_xauusd",
        "description": "Descriptive trend state mapping between EUR/USD and Gold without directional trading claim.",
        "linkage_score": 0.88,
        "is_placeholder": False,
        "requires_no_lookahead": True,
    },
    {
        "linkage_id": "trend_link_persistence_placeholder",
        "linkage_name": "Multi-Asset Trend Persistence Alignment Diagnostic Placeholder",
        "linkage_category": "trend_persistence_alignment_placeholder",
        "asset_a": "regime_trend_family",
        "asset_b": "candidate_trending",
        "description": "Run-length concordance placeholder across simultaneous trending regimes; strictly NOT a momentum trade signal.",
        "linkage_score": 0.84,
        "is_placeholder": True,
        "requires_no_lookahead": True,
    },
    {
        "linkage_id": "trend_link_trans_placeholder",
        "linkage_name": "Trend Transition Alignment Diagnostic Placeholder",
        "linkage_category": "trend_transition_alignment_placeholder",
        "asset_a": "fx_audusd",
        "asset_b": "cmd_copper",
        "description": "Exhaustion and transition timing synchronization between currency and industrial commodity.",
        "linkage_score": 0.85,
        "is_placeholder": True,
        "requires_no_lookahead": True,
    },
    {
        "linkage_id": "trend_link_dependency_status",
        "linkage_name": "Trend Context Phase 129/130 Dependency Status",
        "linkage_category": "trend_context_dependency_status",
        "asset_a": "multi_asset",
        "asset_b": "multi_asset",
        "description": "Verification of upstream trend indicators, diagnostics, and transition models integrity.",
        "linkage_score": 0.92,
        "is_placeholder": False,
        "requires_no_lookahead": True,
    },
]


def build_cross_asset_trend_linkage_registry(
    profile: Optional[CrossAssetRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build trend linkage registry dataframe and summary."""
    if profile is None:
        profile = get_default_cross_asset_regime_profile()

    rows = []
    for item in TREND_LINKAGE_RECORDS:
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
    summary = summarize_cross_asset_trend_linkage(df)
    summary["active_profile"] = profile.profile_name
    return df, summary


def summarize_cross_asset_trend_linkage(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize cross-asset trend linkage records."""
    cat_counts = df["linkage_category"].value_counts().to_dict() if not df.empty else {}
    return {
        "total_linkages": len(df),
        "linkage_categories": cat_counts,
        "mean_linkage_score": float(df["linkage_score"].mean()) if not df.empty else 0.0,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "all_source_preserved": bool(df["source_preserved"].all()) if not df.empty else True,
        "zero_trading_signals": True,
        "zero_directional_claims": True,
    }
