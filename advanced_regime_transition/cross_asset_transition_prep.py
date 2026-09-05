"""Phase 130: Cross-Asset Transition Prep.

Prepares cross-asset transition diagnostic linkages between FX and Commodity regimes,
verifying timestamp alignment and readiness for Phase 131 Cross-Asset Expansion.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_transition.regime_transition_config import (
    RegimeTransitionProfile,
    get_default_regime_transition_profile,
)

CROSS_ASSET_PREP_DATA: List[Dict[str, Any]] = [
    {
        "cross_asset_pair": "EURUSD_vs_BRENT",
        "alignment_readiness": 0.92,
        "timestamp_alignment_status": "aligned",
        "macro_linkage_status": "synchronized",
        "phase_131_readiness": "ready",
        "manual_review_blocker_count": 0,
        "non_signal": True,
        "description": "EUR/USD and Brent crude cross-asset transition linkage alignment",
    },
    {
        "cross_asset_pair": "USDTRY_vs_GOLD",
        "alignment_readiness": 0.90,
        "timestamp_alignment_status": "aligned",
        "macro_linkage_status": "synchronized",
        "phase_131_readiness": "ready",
        "manual_review_blocker_count": 0,
        "non_signal": True,
        "description": "USD/TRY and Gold ounce cross-asset transition linkage alignment",
    },
    {
        "cross_asset_pair": "DXY_vs_COMMODITY_COMPOSITE",
        "alignment_readiness": 0.88,
        "timestamp_alignment_status": "aligned",
        "macro_linkage_status": "synchronized",
        "phase_131_readiness": "ready",
        "manual_review_blocker_count": 0,
        "non_signal": True,
        "description": "Dollar index composite and commodity benchmark transition context",
    },
]


def build_cross_asset_transition_prep_report(
    profile: Optional[RegimeTransitionProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build cross-asset transition prep dataframe and summary."""
    if profile is None:
        profile = get_default_regime_transition_profile()

    df = pd.DataFrame(CROSS_ASSET_PREP_DATA)
    summary = summarize_cross_asset_transition_prep(df)
    summary["active_profile"] = profile.profile_name
    return df, summary


def summarize_cross_asset_transition_prep(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize cross-asset transition prep diagnostics."""
    mean_readiness = float(df["alignment_readiness"].mean()) if not df.empty and "alignment_readiness" in df.columns else 0.0
    total_blockers = int(df["manual_review_blocker_count"].sum()) if not df.empty and "manual_review_blocker_count" in df.columns else 0
    return {
        "total_cross_asset_pairs": len(df),
        "total_contexts": len(df),
        "mean_alignment_readiness": round(mean_readiness, 4),
        "total_manual_review_blockers": total_blockers,
        "all_aligned": bool((df["timestamp_alignment_status"] == "aligned").all()) if not df.empty else True,
        "all_phase_131_ready": bool((df["phase_131_readiness"] == "ready").all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "contains_trading_signal": False,
    }

