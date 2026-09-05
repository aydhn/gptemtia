"""Phase 126: Event Regime Context Registry.

Registers scheduled event window contexts, release latencies, and event importance bounds.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_foundation.regime_foundation_config import (
    RegimeFoundationProfile,
    get_default_regime_foundation_profile,
)

EVENT_CONTEXTS: List[Dict[str, Any]] = [
    {
        "context_id": "event_ctx_01_pre",
        "context_name": "pre_event_context",
        "regime_family": "regime_family_event_context",
        "description": "Pre-event window context (e.g. 60-15 minutes prior to scheduled release) characterized by order book thinning",
        "underlying_features": "minutes_to_event, pre_event_volatility_dampening",
        "source_phases": [110, 120, 122],
        "non_signal": True,
        "status": "regime_ready",
    },
    {
        "context_id": "event_ctx_02_post",
        "context_name": "post_event_context",
        "regime_family": "regime_family_event_context",
        "description": "Post-event window context (e.g. 0-60 minutes following announcement) characterized by price re-anchoring",
        "underlying_features": "minutes_since_event, post_event_dispersion_ratio",
        "source_phases": [110, 120, 122],
        "non_signal": True,
        "status": "regime_ready",
    },
    {
        "context_id": "event_ctx_03_importance",
        "context_name": "event_importance_context",
        "regime_family": "regime_family_event_context",
        "description": "High/medium/low event importance tiering filtering non-impacting calendar releases",
        "underlying_features": "event_tier_score, historical_market_impact_rank",
        "source_phases": [110, 120, 122],
        "non_signal": True,
        "status": "regime_ready",
    },
    {
        "context_id": "event_ctx_04_delay",
        "context_name": "release_delay_context",
        "regime_family": "regime_family_event_context",
        "description": "Release reporting latency measuring delta between official release timestamp and market publication",
        "underlying_features": "reporting_latency_seconds, embargo_compliance_flag",
        "source_phases": [110, 120, 122],
        "non_signal": True,
        "status": "regime_ready",
    },
    {
        "context_id": "event_ctx_05_window",
        "context_name": "event_window_context",
        "regime_family": "regime_family_event_context",
        "description": "Combined pre/post boundary envelope active window masking normal technical regime attribution",
        "underlying_features": "is_event_window_active, active_event_count",
        "source_phases": [110, 120, 122],
        "non_signal": True,
        "status": "regime_ready",
    },
]


def build_event_regime_context_registry(
    profile: Optional[RegimeFoundationProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for event regime context registry."""
    active_profile = profile or get_default_regime_foundation_profile()
    df = pd.DataFrame(EVENT_CONTEXTS)
    summary = {
        "active_profile": active_profile.profile_name,
        "total_contexts": len(df),
        "regime_family": "regime_family_event_context",
        "all_non_signal": bool((df["non_signal"] == True).all()),
        "current_phase": active_profile.current_phase,
        "target_final_phase": active_profile.target_final_phase,
        "next_phase": active_profile.next_phase,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    }
    return df, summary


def summarize_event_regime_context(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize event regime context DataFrame."""
    return {
        "total_contexts": len(df),
        "context_names": list(df["context_name"].unique()) if "context_name" in df.columns else [],
        "non_signal": True,
    }
