"""Phase 132: Macro Surprise Placeholders (Strictly Non-Signal, Non-Predictive)."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_macro_event_news_regime.macro_event_news_regime_config import (
    MacroEventNewsRegimeProfile,
    get_macro_event_news_regime_profile,
)

DEFAULT_SURPRISE_PLACEHOLDERS = [
    {
        "surprise_id": "surp_us_cpi_delta",
        "indicator_id": "macro_us_cpi_yoy",
        "contract_type": "consensus_actual_delta_contract",
        "normalized_scale": "z_score_placeholder",
        "threshold_tier": "significant_deviation_context",
        "is_trade_signal": False,
        "is_predictive": False,
        "description": "Offline diagnostic placeholder comparing survey consensus vs actual release value.",
    },
    {
        "surprise_id": "surp_us_nfp_delta",
        "indicator_id": "macro_us_nfp",
        "contract_type": "consensus_actual_delta_contract",
        "normalized_scale": "standard_deviation_placeholder",
        "threshold_tier": "moderate_deviation_context",
        "is_trade_signal": False,
        "is_predictive": False,
        "description": "Labor surprise dispersion placeholder without directional buy/sell recommendation.",
    },
    {
        "surprise_id": "surp_fomc_rate_surprise",
        "indicator_id": "macro_us_fed_funds_rate",
        "contract_type": "market_implied_delta_contract",
        "normalized_scale": "basis_points_placeholder",
        "threshold_tier": "shock_deviation_context",
        "is_trade_signal": False,
        "is_predictive": False,
        "description": "Policy decision vs market-implied pricing differential placeholder.",
    },
]


def build_macro_surprise_placeholder_registry(
    profile: Optional[MacroEventNewsRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build registry DataFrame of macro surprise placeholders."""
    p = profile or get_macro_event_news_regime_profile()
    rows = []
    for item in DEFAULT_SURPRISE_PLACEHOLDERS:
        row = dict(item)
        row["profile_name"] = p.profile_name
        row["is_trade_signal"] = False
        row["is_predictive"] = False
        row["non_signal"] = True
        row["source_preserved"] = True
        row["official_approval"] = False
        row["production_ready"] = False
        row["broker_ready"] = False
        rows.append(row)
    df = pd.DataFrame(rows)
    summary = {
        "total_surprise_placeholders": len(df),
        "zero_signals": True,
        "zero_predictions": True,
        "all_non_signal": True,
        "all_source_preserved": True,
    }
    return df, summary


def summarize_macro_surprise_placeholders(df: pd.DataFrame) -> Dict[str, Any]:
    """Return summary dictionary for macro surprise placeholders."""
    return {
        "total_placeholders": len(df),
        "zero_signals": not bool(df["is_trade_signal"].any()) if "is_trade_signal" in df.columns else True,
        "zero_predictions": not bool(df["is_predictive"].any()) if "is_predictive" in df.columns else True,
        "all_non_signal": bool(df["non_signal"].all()) if "non_signal" in df.columns else True,
    }
