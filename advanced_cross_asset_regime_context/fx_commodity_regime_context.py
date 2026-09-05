"""Phase 131: FX/Commodity Regime Context Registry.

Defines non-signal cross-asset context records linking FX pairs with commodity regimes
across volatility, trend, range, transition, divergence, and convergence dimensions.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_cross_asset_regime_context.cross_asset_regime_config import (
    CrossAssetRegimeProfile,
    get_default_cross_asset_regime_profile,
)

FX_COMMODITY_CONTEXT_RECORDS: List[Dict[str, Any]] = [
    {
        "context_id": "fxc_vol_eurusd_xauusd",
        "context_name": "EUR/USD to Gold Volatility Regime Context",
        "context_category": "fx_commodity_volatility_context",
        "fx_entity": "fx_eurusd",
        "commodity_entity": "cmd_xauusd",
        "description": "Contemporaneous volatility regime state comparison between EUR/USD and Gold.",
        "readiness_score": 0.88,
        "is_placeholder": False,
        "requires_no_lookahead": True,
    },
    {
        "context_id": "fxc_vol_audusd_copper",
        "context_name": "AUD/USD to Copper Volatility Regime Context",
        "context_category": "fx_commodity_volatility_context",
        "fx_entity": "fx_audusd",
        "commodity_entity": "cmd_copper",
        "description": "Risk asset commodity-currency volatility regime alignment.",
        "readiness_score": 0.85,
        "is_placeholder": False,
        "requires_no_lookahead": True,
    },
    {
        "context_id": "fxc_trend_eurusd_xauusd",
        "context_name": "EUR/USD to Gold Trend Linkage Context",
        "context_category": "fx_commodity_trend_context",
        "fx_entity": "fx_eurusd",
        "commodity_entity": "cmd_xauusd",
        "description": "Non-directional joint trend state mapping against US Dollar backdrop.",
        "readiness_score": 0.86,
        "is_placeholder": False,
        "requires_no_lookahead": True,
    },
    {
        "context_id": "fxc_trend_usdjpy_wti",
        "context_name": "USD/JPY to WTI Trend Linkage Context",
        "context_category": "fx_commodity_trend_context",
        "fx_entity": "fx_usdjpy",
        "commodity_entity": "cmd_wti",
        "description": "Import-dependent energy pricing regime context vs Yen strength.",
        "readiness_score": 0.82,
        "is_placeholder": False,
        "requires_no_lookahead": True,
    },
    {
        "context_id": "fxc_range_eurusd_xagusd",
        "context_name": "EUR/USD to Silver Range Bound Context",
        "context_category": "fx_commodity_range_context",
        "fx_entity": "fx_eurusd",
        "commodity_entity": "cmd_xagusd",
        "description": "Consolidation regime and mean reversion range alignment without trade triggers.",
        "readiness_score": 0.84,
        "is_placeholder": False,
        "requires_no_lookahead": True,
    },
    {
        "context_id": "fxc_trans_eurusd_xauusd",
        "context_name": "EUR/USD to Gold State Transition Alignment",
        "context_category": "fx_commodity_transition_context",
        "fx_entity": "fx_eurusd",
        "commodity_entity": "cmd_xauusd",
        "description": "Synchronization of Phase 130 candidate transition events across FX and Gold.",
        "readiness_score": 0.85,
        "is_placeholder": False,
        "requires_no_lookahead": True,
    },
    {
        "context_id": "fxc_div_placeholder_eurusd_xauusd",
        "context_name": "EUR/USD to Gold Divergence Diagnostic Placeholder",
        "context_category": "fx_commodity_divergence_placeholder",
        "fx_entity": "fx_eurusd",
        "commodity_entity": "cmd_xauusd",
        "description": "Diagnostic divergence observation schema; strictly NOT trade entry or pairs signal.",
        "readiness_score": 0.80,
        "is_placeholder": True,
        "requires_no_lookahead": True,
    },
    {
        "context_id": "fxc_conv_placeholder_audusd_copper",
        "context_name": "AUD/USD to Copper Convergence Diagnostic Placeholder",
        "context_category": "fx_commodity_convergence_placeholder",
        "fx_entity": "fx_audusd",
        "commodity_entity": "cmd_copper",
        "description": "Diagnostic convergence observation schema; strictly NOT mean-reversion trade rule.",
        "readiness_score": 0.80,
        "is_placeholder": True,
        "requires_no_lookahead": True,
    },
]


def build_fx_commodity_regime_context_registry(
    profile: Optional[CrossAssetRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build FX/Commodity regime context registry dataframe and summary."""
    if profile is None:
        profile = get_default_cross_asset_regime_profile()

    rows = []
    for item in FX_COMMODITY_CONTEXT_RECORDS:
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
    summary = summarize_fx_commodity_regime_context(df)
    summary["active_profile"] = profile.profile_name
    return df, summary


def summarize_fx_commodity_regime_context(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize FX/Commodity regime context records."""
    cat_counts = df["context_category"].value_counts().to_dict() if not df.empty else {}
    return {
        "total_records": len(df),
        "context_categories": cat_counts,
        "mean_readiness_score": float(df["readiness_score"].mean()) if not df.empty else 0.0,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "all_source_preserved": bool(df["source_preserved"].all()) if not df.empty else True,
        "zero_trading_signals": True,
        "zero_predictions": True,
    }
