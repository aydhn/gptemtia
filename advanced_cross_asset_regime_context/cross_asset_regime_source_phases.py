"""Phase 131: Cross-Asset Regime Source Phases Registry.

Defines lineage and source phase dependencies for Cross-Asset Regime Context Expansion.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_cross_asset_regime_context.cross_asset_regime_config import (
    CrossAssetRegimeProfile,
    get_default_cross_asset_regime_profile,
)

SOURCE_PHASES: List[Dict[str, Any]] = [
    {
        "source_phase_num": 119,
        "phase_name": "Phase 119 Cross-Asset Feature Alignment",
        "contribution": "Multi-asset time-series synchronization contracts and canonical alignment policies.",
        "status": "COMPLETED",
        "verified": True,
    },
    {
        "source_phase_num": 120,
        "phase_name": "Phase 120 Macro/Calendar/News Feature Fusion",
        "contribution": "Lag-tolerant macro fusion, calendar window features, and metadata-only news tags.",
        "status": "COMPLETED",
        "verified": True,
    },
    {
        "source_phase_num": 121,
        "phase_name": "Phase 121 Feature Validation and No-Lookahead Guard",
        "contribution": "Zero negative shift validation and forbidden column rejection mechanisms.",
        "status": "COMPLETED",
        "verified": True,
    },
    {
        "source_phase_num": 123,
        "phase_name": "Phase 123 Feature Quality and Drift Diagnostics",
        "contribution": "Distribution drift monitoring and missingness quality baselines.",
        "status": "COMPLETED",
        "verified": True,
    },
    {
        "source_phase_num": 124,
        "phase_name": "Phase 124 Feature Store Integration Expansion",
        "contribution": "Centralized metadata catalogs and read-only feature access contracts.",
        "status": "COMPLETED",
        "verified": True,
    },
    {
        "source_phase_num": 126,
        "phase_name": "Phase 126 Regime Classification and Market Behavior Foundation",
        "contribution": "Regime families (volatility, trend, range) and foundational taxonomy.",
        "status": "COMPLETED",
        "verified": True,
    },
    {
        "source_phase_num": 127,
        "phase_name": "Phase 127 Regime Feature Matrix and State Dataset Contracts",
        "contribution": "Regime feature matrices and non-target candidate context specifications.",
        "status": "COMPLETED",
        "verified": True,
    },
    {
        "source_phase_num": 129,
        "phase_name": "Phase 129 Market Behavior Diagnostics and Regime Quality",
        "contribution": "Market behavior diagnostic coverage and regime quality scoring.",
        "status": "COMPLETED",
        "verified": True,
    },
    {
        "source_phase_num": 130,
        "phase_name": "Phase 130 Regime Transition and Stability Analysis",
        "contribution": "State sequence continuity, empirical transition frequency, and stability scoring.",
        "status": "COMPLETED",
        "verified": True,
    },
]


def build_cross_asset_regime_source_phase_registry(
    profile: Optional[CrossAssetRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build source phase registry dataframe and summary."""
    if profile is None:
        profile = get_default_cross_asset_regime_profile()

    rows = []
    for item in SOURCE_PHASES:
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
    summary = summarize_cross_asset_source_phases(df)
    summary["active_profile"] = profile.profile_name
    return df, summary


def summarize_cross_asset_source_phases(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize source phase registry."""
    return {
        "total_source_phases": len(df),
        "all_completed": bool((df["status"] == "COMPLETED").all()) if not df.empty else True,
        "all_verified": bool(df["verified"].all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "all_source_preserved": bool(df["source_preserved"].all()) if not df.empty else True,
    }
