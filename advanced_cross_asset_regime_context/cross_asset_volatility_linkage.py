"""Phase 131: Cross-Asset Volatility Linkage Registry.

Defines non-signal cross-asset volatility linkage records (volatility level context,
expansion context, compression context, volatility regime alignment placeholders).
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_cross_asset_regime_context.cross_asset_regime_config import (
    CrossAssetRegimeProfile,
    get_default_cross_asset_regime_profile,
)

VOLATILITY_LINKAGE_RECORDS: List[Dict[str, Any]] = [
    {
        "linkage_id": "vol_link_level_fx_cmd",
        "linkage_name": "FX to Commodity Baseline Volatility Level Context",
        "linkage_category": "cross_asset_volatility_level_context",
        "asset_a": "fx_eurusd",
        "asset_b": "cmd_xauusd",
        "description": "Comparative baseline realized volatility percentiles without trade signaling.",
        "linkage_score": 0.87,
        "is_placeholder": False,
        "requires_no_lookahead": True,
    },
    {
        "linkage_id": "vol_link_expansion_risk_off",
        "linkage_name": "Risk-Off Volatility Expansion Linkage Context",
        "linkage_category": "cross_asset_volatility_expansion_context",
        "asset_a": "fx_usdjpy",
        "asset_b": "cmd_brent",
        "description": "Simultaneous volatility spike co-occurrence diagnostics across energy and FX.",
        "linkage_score": 0.85,
        "is_placeholder": False,
        "requires_no_lookahead": True,
    },
    {
        "linkage_id": "vol_link_compression_summer",
        "linkage_name": "Multi-Asset Volatility Compression Linkage Context",
        "linkage_category": "cross_asset_volatility_compression_context",
        "asset_a": "fx_eurusd",
        "asset_b": "cmd_copper",
        "description": "Joint low-volatility quiet regime persistence diagnostics.",
        "linkage_score": 0.86,
        "is_placeholder": False,
        "requires_no_lookahead": True,
    },
    {
        "linkage_id": "vol_link_regime_alignment_placeholder",
        "linkage_name": "Cross-Asset Volatility Regime Alignment Diagnostic Placeholder",
        "linkage_category": "volatility_regime_alignment_placeholder",
        "asset_a": "regime_volatility_family",
        "asset_b": "candidate_high_vol",
        "description": "High volatility concordance metric placeholder; strictly NOT an option/straddle trade trigger.",
        "linkage_score": 0.82,
        "is_placeholder": True,
        "requires_no_lookahead": True,
    },
]


def build_cross_asset_volatility_linkage_registry(
    profile: Optional[CrossAssetRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build volatility linkage registry dataframe and summary."""
    if profile is None:
        profile = get_default_cross_asset_regime_profile()

    rows = []
    for item in VOLATILITY_LINKAGE_RECORDS:
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
    summary = summarize_cross_asset_volatility_linkage(df)
    summary["active_profile"] = profile.profile_name
    return df, summary


def summarize_cross_asset_volatility_linkage(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize cross-asset volatility linkage records."""
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
