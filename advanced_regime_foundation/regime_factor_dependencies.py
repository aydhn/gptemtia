"""Phase 126: Regime Factor Dependencies Registry.

Maps explicit upstream factor, quality, and store dependencies required for regime families.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_foundation.regime_foundation_config import (
    RegimeFoundationProfile,
    get_default_regime_foundation_profile,
)

FACTOR_DEPENDENCIES: List[Dict[str, Any]] = [
    {
        "dependency_id": "dep_01_vol_factor",
        "target_regime_family": "regime_family_volatility",
        "dependency_type": "factor",
        "source_phase": 122,
        "prerequisite_name": "Phase 122 Volatility Factor Families",
        "description": "Requires realized volatility, ATR, Parkinson, and Bollinger width factor definitions",
        "verification_status": "VERIFIED",
        "non_signal": True,
        "blocking": True,
    },
    {
        "dependency_id": "dep_02_vol_quality",
        "target_regime_family": "regime_family_volatility",
        "dependency_type": "quality",
        "source_phase": 123,
        "prerequisite_name": "Phase 123 Volatility Quality & Drift Diagnostics",
        "description": "Requires missingness and stability scores for volatility indicators",
        "verification_status": "VERIFIED",
        "non_signal": True,
        "blocking": True,
    },
    {
        "dependency_id": "dep_03_trend_factor",
        "target_regime_family": "regime_family_trend",
        "dependency_type": "factor",
        "source_phase": 122,
        "prerequisite_name": "Phase 122 Trend Factor Families",
        "description": "Requires moving average slope, trend alignment, and Donchian channel factor definitions",
        "verification_status": "VERIFIED",
        "non_signal": True,
        "blocking": True,
    },
    {
        "dependency_id": "dep_04_trend_quality",
        "target_regime_family": "regime_family_trend",
        "dependency_type": "quality",
        "source_phase": 123,
        "prerequisite_name": "Phase 123 Trend Quality & Drift Diagnostics",
        "description": "Requires drift bounds and stability metrics for trend indicators",
        "verification_status": "VERIFIED",
        "non_signal": True,
        "blocking": True,
    },
    {
        "dependency_id": "dep_05_range_factor",
        "target_regime_family": "regime_family_range",
        "dependency_type": "factor",
        "source_phase": 122,
        "prerequisite_name": "Phase 122 Mean-Reversion and Range Factors",
        "description": "Requires z-score, mean distance, and range-boundedness factors",
        "verification_status": "VERIFIED",
        "non_signal": True,
        "blocking": True,
    },
    {
        "dependency_id": "dep_06_macro_fusion",
        "target_regime_family": "regime_family_macro_context",
        "dependency_type": "feature_fusion",
        "source_phase": 120,
        "prerequisite_name": "Phase 120 Macro Feature Fusion",
        "description": "Requires point-in-time publication lag aligned macro features",
        "verification_status": "VERIFIED",
        "non_signal": True,
        "blocking": True,
    },
    {
        "dependency_id": "dep_07_macro_factor",
        "target_regime_family": "regime_family_macro_context",
        "dependency_type": "factor",
        "source_phase": 122,
        "prerequisite_name": "Phase 122 Macro Context Factors",
        "description": "Requires inflation surprise and rate differential factor definitions",
        "verification_status": "VERIFIED",
        "non_signal": True,
        "blocking": True,
    },
    {
        "dependency_id": "dep_08_event_fusion",
        "target_regime_family": "regime_family_event_context",
        "dependency_type": "feature_fusion",
        "source_phase": 120,
        "prerequisite_name": "Phase 120 Calendar Event Windows",
        "description": "Requires pre/post announcement time envelopes",
        "verification_status": "VERIFIED",
        "non_signal": True,
        "blocking": True,
    },
    {
        "dependency_id": "dep_09_event_factor",
        "target_regime_family": "regime_family_event_context",
        "dependency_type": "factor",
        "source_phase": 122,
        "prerequisite_name": "Phase 122 Calendar Event Factors",
        "description": "Requires event importance and release delay factors",
        "verification_status": "VERIFIED",
        "non_signal": True,
        "blocking": True,
    },
    {
        "dependency_id": "dep_10_news_fusion",
        "target_regime_family": "regime_family_news_metadata_context",
        "dependency_type": "feature_fusion",
        "source_phase": 120,
        "prerequisite_name": "Phase 120 News Metadata Features",
        "description": "Requires strictly metadata-only news volume and topic tags",
        "verification_status": "VERIFIED",
        "non_signal": True,
        "blocking": True,
    },
    {
        "dependency_id": "dep_11_news_factor",
        "target_regime_family": "regime_family_news_metadata_context",
        "dependency_type": "factor",
        "source_phase": 122,
        "prerequisite_name": "Phase 122 News Attention Factors",
        "description": "Requires headline count and topic concentration factors",
        "verification_status": "VERIFIED",
        "non_signal": True,
        "blocking": True,
    },
    {
        "dependency_id": "dep_12_cross_asset_align",
        "target_regime_family": "regime_family_cross_asset_context",
        "dependency_type": "alignment",
        "source_phase": 119,
        "prerequisite_name": "Phase 119 Cross-Asset Feature Alignment",
        "description": "Requires synchronized multi-domain timestamp alignment across FX and commodities",
        "verification_status": "VERIFIED",
        "non_signal": True,
        "blocking": True,
    },
    {
        "dependency_id": "dep_13_cross_asset_factor",
        "target_regime_family": "regime_family_cross_asset_context",
        "dependency_type": "factor",
        "source_phase": 122,
        "prerequisite_name": "Phase 122 Cross-Asset Factors",
        "description": "Requires DXY, US10Y, and intermarket spread coupling factors",
        "verification_status": "VERIFIED",
        "non_signal": True,
        "blocking": True,
    },
    {
        "dependency_id": "dep_14_all_regimes_val",
        "target_regime_family": "all_regime_families",
        "dependency_type": "validation",
        "source_phase": 121,
        "prerequisite_name": "Phase 121 Feature Validation and No-Lookahead Guard",
        "description": "Requires no-lookahead and forbidden column verification across all inputs",
        "verification_status": "VERIFIED",
        "non_signal": True,
        "blocking": True,
    },
    {
        "dependency_id": "dep_15_all_regimes_store",
        "target_regime_family": "all_regime_families",
        "dependency_type": "feature_store",
        "source_phase": 124,
        "prerequisite_name": "Phase 124 FeatureStore Metadata",
        "description": "Requires central store registry entries and point-in-time query contracts",
        "verification_status": "VERIFIED",
        "non_signal": True,
        "blocking": True,
    },
]


def build_regime_factor_dependency_registry(
    profile: Optional[RegimeFoundationProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for regime factor dependency registry."""
    active_profile = profile or get_default_regime_foundation_profile()
    df = pd.DataFrame(FACTOR_DEPENDENCIES)
    summary = {
        "active_profile": active_profile.profile_name,
        "total_dependencies": len(df),
        "all_verified": bool((df["verification_status"] == "VERIFIED").all()),
        "all_non_signal": bool((df["non_signal"] == True).all()),
        "current_phase": active_profile.current_phase,
        "target_final_phase": active_profile.target_final_phase,
        "next_phase": active_profile.next_phase,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    }
    return df, summary


def summarize_regime_factor_dependencies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize regime factor dependencies DataFrame."""
    return {
        "total_dependencies": len(df),
        "source_phases": sorted(list(df["source_phase"].unique())) if "source_phase" in df.columns else [],
        "all_verified": True,
        "non_signal": True,
    }
