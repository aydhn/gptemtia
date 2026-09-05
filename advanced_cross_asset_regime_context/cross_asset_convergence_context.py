"""Phase 131: Cross-Asset Convergence Context Registry.

Defines non-signal convergence diagnostic context records (re-coupling observations,
regime re-alignment, spread narrowing). Strictly NOT mean-reversion trading rules or arbitrage strategies.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_cross_asset_regime_context.cross_asset_regime_config import (
    CrossAssetRegimeProfile,
    get_default_cross_asset_regime_profile,
)

CONVERGENCE_CONTEXT_RECORDS: List[Dict[str, Any]] = [
    {
        "convergence_id": "conv_fx_cmd_re_coupling",
        "convergence_name": "FX to Commodity State Re-Coupling Diagnostic",
        "convergence_category": "convergence_context",
        "pair_ref": "pair_fx_eurusd_to_cmd_xauusd",
        "primary_entity": "fx_eurusd",
        "secondary_entity": "cmd_xauusd",
        "description": "Diagnostic tracking of regime re-synchronization; strictly NOT a mean-reversion trading rule.",
        "diagnostic_score": 0.86,
        "is_trade_signal": False,
        "requires_no_lookahead": True,
    },
    {
        "convergence_id": "conv_energy_fx_alignment",
        "convergence_name": "Crude Oil to USD/JPY Regime Convergence Diagnostic",
        "convergence_category": "convergence_context",
        "pair_ref": "pair_cmd_brent_to_macro_us_gdp",
        "primary_entity": "cmd_brent",
        "secondary_entity": "fx_usdjpy",
        "description": "Observation of narrowing divergence between terms-of-trade and exchange rate volatility.",
        "diagnostic_score": 0.84,
        "is_trade_signal": False,
        "requires_no_lookahead": True,
    },
    {
        "convergence_id": "conv_precious_metals_co_movement",
        "convergence_name": "Gold to Silver Volatility Regime Convergence Diagnostic",
        "convergence_category": "convergence_context",
        "pair_ref": "pair_fx_eurusd_to_cross_asset_context",
        "primary_entity": "cmd_xauusd",
        "secondary_entity": "cmd_xagusd",
        "description": "Normalization of Gold/Silver ratio regime dispersion without spread trading instructions.",
        "diagnostic_score": 0.89,
        "is_trade_signal": False,
        "requires_no_lookahead": True,
    },
]


def build_cross_asset_convergence_context_registry(
    profile: Optional[CrossAssetRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build convergence context registry dataframe and summary."""
    if profile is None:
        profile = get_default_cross_asset_regime_profile()

    rows = []
    for item in CONVERGENCE_CONTEXT_RECORDS:
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
    summary = summarize_cross_asset_convergence_context(df)
    summary["active_profile"] = profile.profile_name
    return df, summary


def summarize_cross_asset_convergence_context(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize convergence context records."""
    return {
        "total_convergences": len(df),
        "mean_diagnostic_score": float(df["diagnostic_score"].mean()) if not df.empty else 0.0,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "all_source_preserved": bool(df["source_preserved"].all()) if not df.empty else True,
        "zero_trading_signals": bool((~df["is_trade_signal"]).all()) if not df.empty else True,
        "zero_mean_reversion_strategies": True,
    }
