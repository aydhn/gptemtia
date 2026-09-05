"""Phase 127: Regime Matrix Factor Input Registry.

Catalogs factor families and factor metadata mapped from Phase 122 and Phase 123.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_matrix.regime_matrix_config import (
    RegimeMatrixProfile,
    get_default_regime_matrix_profile,
)

FACTOR_INPUTS_CATALOG: List[Dict[str, Any]] = [
    {
        "factor_family": "trend_factor_family",
        "canonical_name": "trend_persistence_factor",
        "source_phase": 122,
        "description": "Multi-window directional persistence and moving average slope factors.",
        "quality_drift_phase": 123,
        "quality_status": "QUALITY_PASS",
        "drift_status": "LOW_DRIFT",
    },
    {
        "factor_family": "momentum_factor_family",
        "canonical_name": "momentum_velocity_factor",
        "source_phase": 122,
        "description": "RSI, MACD, and rate-of-change normalized momentum metrics.",
        "quality_drift_phase": 123,
        "quality_status": "QUALITY_PASS",
        "drift_status": "LOW_DRIFT",
    },
    {
        "factor_family": "volatility_factor_family",
        "canonical_name": "volatility_expansion_factor",
        "source_phase": 122,
        "description": "Realized volatility, Bollinger bandwidth, and ATR ratio factors.",
        "quality_drift_phase": 123,
        "quality_status": "QUALITY_PASS",
        "drift_status": "LOW_DRIFT",
    },
    {
        "factor_family": "mean_reversion_factor_family",
        "canonical_name": "channel_distance_zscore_factor",
        "source_phase": 122,
        "description": "Normalized distance from moving mean and channel boundaries.",
        "quality_drift_phase": 123,
        "quality_status": "QUALITY_PASS",
        "drift_status": "LOW_DRIFT",
    },
    {
        "factor_family": "macro_factor_family",
        "canonical_name": "macro_policy_stance_factor",
        "source_phase": 122,
        "description": "Yield curve steepening/flattening and central bank policy proxies.",
        "quality_drift_phase": 123,
        "quality_status": "QUALITY_PASS",
        "drift_status": "LOW_DRIFT",
    },
    {
        "factor_family": "event_factor_family",
        "canonical_name": "scheduled_event_window_factor",
        "source_phase": 122,
        "description": "Pre/post economic event release time distance factors.",
        "quality_drift_phase": 123,
        "quality_status": "QUALITY_PASS",
        "drift_status": "LOW_DRIFT",
    },
    {
        "factor_family": "news_metadata_factor_family",
        "canonical_name": "news_volume_frequency_factor",
        "source_phase": 122,
        "description": "Metadata-only news count and asset tag concentration (zero full text).",
        "quality_drift_phase": 123,
        "quality_status": "QUALITY_PASS",
        "drift_status": "LOW_DRIFT",
    },
    {
        "factor_family": "cross_asset_factor_family",
        "canonical_name": "intermarket_relative_strength_factor",
        "source_phase": 122,
        "description": "Cross-currency/commodity spread and correlation factor metrics.",
        "quality_drift_phase": 123,
        "quality_status": "QUALITY_PASS",
        "drift_status": "LOW_DRIFT",
    },
]


def build_regime_matrix_factor_input_registry(
    profile: Optional[RegimeMatrixProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the factor input registry for Phase 127."""
    p = profile or get_default_regime_matrix_profile()

    rows = []
    for f in FACTOR_INPUTS_CATALOG:
        f_copy = f.copy()
        f_copy["current_phase"] = p.current_phase
        f_copy["target_final_phase"] = p.target_final_phase
        f_copy["next_phase"] = p.next_phase
        f_copy["non_signal"] = True
        f_copy["source_preserved"] = True
        f_copy["status"] = "matrix_ready"
        rows.append(f_copy)

    df = pd.DataFrame(rows)
    summary = summarize_regime_matrix_factor_inputs(df)
    return df, summary


def summarize_regime_matrix_factor_inputs(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize factor input registry."""
    return {
        "total_factor_inputs": len(df),
        "total_factors": len(df),
        "factor_families": df["factor_family"].tolist() if not df.empty else [],
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "all_source_preserved": bool(df["source_preserved"].all()) if not df.empty else True,
        "status": "matrix_ready",
    }


build_regime_matrix_factor_inputs_registry = build_regime_matrix_factor_input_registry
