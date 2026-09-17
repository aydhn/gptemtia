# -*- coding: utf-8 -*-
"""Phase 143: Regime Explainability Linkage."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_explainability_attribution.explainability_config import (
    ExplainabilityProfile,
    get_explainability_profile,
)


def build_regime_explainability_linkage_registry(
    profile: Optional[ExplainabilityProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the DataFrame registry of regime explainability linkage contracts."""
    prof = profile or get_explainability_profile()

    linkages = [
        ("regime_linkage_high_volatility", "high_volatility_regime", "phase_135_macro_regime", "High volatility regime attribution shift linkage placeholder"),
        ("regime_linkage_low_liquidity", "low_liquidity_regime", "phase_135_macro_regime", "Low liquidity regime attribution shift linkage placeholder"),
        ("regime_linkage_trending_bullish", "trending_bullish_regime", "phase_135_macro_regime", "Trending bullish regime attribution linkage placeholder"),
        ("regime_linkage_crisis_shock", "crisis_shock_regime", "phase_135_macro_regime", "Crisis shock regime attribution linkage placeholder"),
    ]

    rows: List[Dict[str, Any]] = []
    for lid, rname, sourceref, desc in linkages:
        rows.append({
            "linkage_id": lid,
            "regime_name": rname,
            "regime_source_ref": sourceref,
            "description": desc,
            "is_linkage_contract": True,
            "non_signal": True,
            "official_approval": False,
            "production_ready": False,
            "broker_ready": False,
        })

    df = pd.DataFrame(rows)
    summary = summarize_regime_explainability_linkage(df)
    return df, summary


def summarize_regime_explainability_linkage(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize regime explainability linkage contracts."""
    return {
        "total_regime_linkages": len(df),
        "all_linkage_contract": bool(df["is_linkage_contract"].all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "current_phase": 143,
        "next_phase": 144,
        "target_final_phase": 160,
    }
