"""Phase 132: Macro/Event/News Regime Profile Registry."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_macro_event_news_regime.macro_event_news_regime_config import (
    MACRO_EVENT_NEWS_REGIME_PROFILES,
    MacroEventNewsRegimeProfile,
    get_macro_event_news_regime_profile,
)


def build_macro_event_news_regime_profile_registry(
    profile: Optional[MacroEventNewsRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build registry DataFrame of operational profiles for Phase 132."""
    active_profile = profile or get_macro_event_news_regime_profile()
    rows = []
    for name, p in MACRO_EVENT_NEWS_REGIME_PROFILES.items():
        rows.append(
            {
                "profile_name": p.profile_name,
                "description": p.description,
                "current_phase": p.current_phase,
                "target_final_phase": p.target_final_phase,
                "next_phase": p.next_phase,
                "dry_run_default": p.dry_run_default,
                "local_only": p.local_only,
                "non_production": p.non_production,
                "research_only": p.research_only,
                "min_context_score": p.min_context_score,
                "is_active": (p.profile_name == active_profile.profile_name),
                "non_signal": True,
                "source_preserved": True,
                "official_approval": False,
                "production_ready": False,
                "broker_ready": False,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "total_profiles": len(df),
        "active_profile": active_profile.profile_name,
        "current_phase": 132,
        "target_final_phase": 160,
        "next_phase": 133,
        "all_non_signal": True,
        "all_source_preserved": True,
        "zero_model_training": True,
        "zero_trading_signals": True,
    }
    return df, summary


def summarize_macro_event_news_regime_profiles(df: pd.DataFrame) -> Dict[str, Any]:
    """Return summary dictionary for profile registry DataFrame."""
    return {
        "total_profiles": len(df),
        "active_profiles": int(df["is_active"].sum()) if "is_active" in df.columns else 0,
        "all_non_signal": bool(df["non_signal"].all()) if "non_signal" in df.columns else True,
        "all_source_preserved": bool(df["source_preserved"].all()) if "source_preserved" in df.columns else True,
    }
