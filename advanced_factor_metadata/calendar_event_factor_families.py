"""Phase 122 Calendar Event Factor Families Registry.

Defines scheduled economic release proximity, event windows, importance weights,
and delay factors. Strictly non-signal and research-only.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_factor_metadata.factor_metadata_config import (
    FactorMetadataProfile,
    get_default_factor_metadata_profile,
)
from advanced_factor_metadata.factor_metadata_labels import FACTOR_READY

CALENDAR_EVENT_FACTOR_METADATA: List[Dict[str, Any]] = [
    {
        "factor_name": "factor_event_pre_release_context",
        "factor_family": "calendar_event",
        "input_features": ["fusion__event_pre_release_window"],
        "calculation_type": "binary_pre_event_window_flag",
        "non_signal_usage": "Blackout window identification prior to major macro release.",
        "status_label": FACTOR_READY,
        "manual_review_required": False,
    },
    {
        "factor_name": "factor_event_post_release_context",
        "factor_family": "calendar_event",
        "input_features": ["fusion__event_post_release_window"],
        "calculation_type": "binary_post_event_window_flag",
        "non_signal_usage": "Immediate post-announcement window tracking.",
        "status_label": FACTOR_READY,
        "manual_review_required": False,
    },
    {
        "factor_name": "factor_event_importance_context",
        "factor_family": "calendar_event",
        "input_features": ["fusion__event_importance_weight"],
        "calculation_type": "normalized_event_impact_weight",
        "non_signal_usage": "Ordinal importance weight of scheduled calendar release.",
        "status_label": FACTOR_READY,
        "manual_review_required": False,
    },
    {
        "factor_name": "factor_event_release_delay_context",
        "factor_family": "calendar_event",
        "input_features": ["fusion__release_delay_minutes"],
        "calculation_type": "actual_minus_scheduled_delay_seconds",
        "non_signal_usage": "Measures data dissemination latency from economic calendar source.",
        "status_label": FACTOR_READY,
        "manual_review_required": False,
    },
]


def build_calendar_event_factor_family_registry(
    profile: FactorMetadataProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build Calendar Event Factor Family Registry DataFrame and summary."""
    active_profile = profile or get_default_factor_metadata_profile()

    records = [dict(item) for item in CALENDAR_EVENT_FACTOR_METADATA]
    df = pd.DataFrame(records)

    summary = {
        "active_profile": active_profile.name,
        "total_factors": len(records),
        "current_phase": active_profile.current_phase,
        "target_final_phase": active_profile.target_final_phase,
        "non_signal": True,
        "status": FACTOR_READY,
    }
    return df, summary


def summarize_calendar_event_factor_family(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize calendar event factor family DataFrame."""
    return {
        "total_factors": len(df),
        "status": FACTOR_READY,
        "non_signal": True,
    }
