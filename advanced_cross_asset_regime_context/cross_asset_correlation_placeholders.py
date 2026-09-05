"""Phase 131: Cross-Asset Correlation Placeholder Registry.

Defines non-signal correlation placeholder specifications across asset classes.
Zero predictive modeling, zero machine learning correlation forecasting, zero trading signals.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_cross_asset_regime_context.cross_asset_regime_config import (
    CrossAssetRegimeProfile,
    get_default_cross_asset_regime_profile,
)

CORRELATION_PLACEHOLDER_RECORDS: List[Dict[str, Any]] = [
    {
        "placeholder_id": "corr_eurusd_xauusd_rolling",
        "placeholder_name": "EUR/USD to Gold Rolling Correlation Placeholder",
        "metric_type": "rolling_pearson_placeholder",
        "asset_pair": "fx_eurusd__cmd_xauusd",
        "window_spec": "w20_w60",
        "description": "Tabular statistical placeholder for multi-window rolling correlation without predictive forecast.",
        "readiness_score": 0.88,
        "is_predictive": False,
        "requires_no_lookahead": True,
    },
    {
        "placeholder_id": "corr_audusd_copper_rolling",
        "placeholder_name": "AUD/USD to Copper Rolling Correlation Placeholder",
        "metric_type": "rolling_spearman_placeholder",
        "asset_pair": "fx_audusd__cmd_copper",
        "window_spec": "w20_w60",
        "description": "Rank correlation schema tracking commodity currency sensitivity without trading triggers.",
        "readiness_score": 0.86,
        "is_predictive": False,
        "requires_no_lookahead": True,
    },
    {
        "placeholder_id": "corr_regime_state_concordance",
        "placeholder_name": "Regime State Concordance Matrix Placeholder",
        "metric_type": "contingency_concordance_placeholder",
        "asset_pair": "multi_asset_matrix",
        "window_spec": "regime_window",
        "description": "Empirical joint state contingency count placeholder without Markov or ML fitting.",
        "readiness_score": 0.87,
        "is_predictive": False,
        "requires_no_lookahead": True,
    },
]


def build_cross_asset_correlation_placeholder_registry(
    profile: Optional[CrossAssetRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build correlation placeholder registry dataframe and summary."""
    if profile is None:
        profile = get_default_cross_asset_regime_profile()

    rows = []
    for item in CORRELATION_PLACEHOLDER_RECORDS:
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
    summary = summarize_cross_asset_correlation_placeholders(df)
    summary["active_profile"] = profile.profile_name
    return df, summary


def summarize_cross_asset_correlation_placeholders(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize correlation placeholder records."""
    return {
        "total_placeholders": len(df),
        "mean_readiness_score": float(df["readiness_score"].mean()) if not df.empty else 0.0,
        "all_non_predictive": bool((~df["is_predictive"]).all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "all_source_preserved": bool(df["source_preserved"].all()) if not df.empty else True,
        "zero_trading_signals": True,
        "zero_predictions": True,
    }
