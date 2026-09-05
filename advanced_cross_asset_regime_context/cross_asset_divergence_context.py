"""Phase 131: Cross-Asset Divergence Context Registry.

Defines non-signal divergence diagnostic context records (decoupling observations,
spread dispersion, discordant regime behavior). Strictly NOT pairs trading or trade entry signals.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_cross_asset_regime_context.cross_asset_regime_config import (
    CrossAssetRegimeProfile,
    get_default_cross_asset_regime_profile,
)

DIVERGENCE_CONTEXT_RECORDS: List[Dict[str, Any]] = [
    {
        "divergence_id": "div_fx_cmd_spread_dispersion",
        "divergence_name": "FX to Commodity State Divergence Diagnostic",
        "divergence_category": "divergence_context",
        "pair_ref": "pair_fx_eurusd_to_cmd_xauusd",
        "primary_entity": "fx_eurusd",
        "secondary_entity": "cmd_xauusd",
        "description": "Diagnostic tracking of regime discordance where EUR/USD is rangebound but Gold trends; strictly NOT trade entry.",
        "diagnostic_score": 0.85,
        "is_trade_signal": False,
        "requires_no_lookahead": True,
    },
    {
        "divergence_id": "div_aud_copper_decoupling",
        "divergence_name": "AUD/USD vs Copper Growth Divergence Diagnostic",
        "divergence_category": "divergence_context",
        "pair_ref": "pair_fx_audusd_to_cmd_copper",
        "primary_entity": "fx_audusd",
        "secondary_entity": "cmd_copper",
        "description": "Observation of industrial metal decoupling from currency momentum.",
        "diagnostic_score": 0.83,
        "is_trade_signal": False,
        "requires_no_lookahead": True,
    },
    {
        "divergence_id": "div_yield_gold_discordance",
        "divergence_name": "Real Yield vs Gold Divergence Diagnostic",
        "divergence_category": "divergence_context",
        "pair_ref": "pair_cmd_xauusd_to_macro_us_fedfunds",
        "primary_entity": "cmd_xauusd",
        "secondary_entity": "macro_us_fedfunds",
        "description": "Diagnostic tracking of breakdown in real interest rate vs bullion relationship.",
        "diagnostic_score": 0.88,
        "is_trade_signal": False,
        "requires_no_lookahead": True,
    },
]


def build_cross_asset_divergence_context_registry(
    profile: Optional[CrossAssetRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build divergence context registry dataframe and summary."""
    if profile is None:
        profile = get_default_cross_asset_regime_profile()

    rows = []
    for item in DIVERGENCE_CONTEXT_RECORDS:
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
    summary = summarize_cross_asset_divergence_context(df)
    summary["active_profile"] = profile.profile_name
    return df, summary


def summarize_cross_asset_divergence_context(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize divergence context records."""
    return {
        "total_divergences": len(df),
        "mean_diagnostic_score": float(df["diagnostic_score"].mean()) if not df.empty else 0.0,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "all_source_preserved": bool(df["source_preserved"].all()) if not df.empty else True,
        "zero_trading_signals": bool((~df["is_trade_signal"]).all()) if not df.empty else True,
        "zero_pairs_trading_rules": True,
    }
