from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_feature_fusion.fusion_feature_config import (
    FusionFeatureProfile,
    get_default_fusion_feature_profile,
)


CALENDAR_WINDOW_FEATURES: List[Dict[str, Any]] = [
    {
        "feature_name": "pre_event_window_placeholder",
        "fusion_family": "fusion_family_calendar",
        "description": "Planlanan olay öncesi zaman penceresi bayrağı (scheduled_time bazlı).",
        "non_signal": True,
        "status_label": "fusion_ready",
    },
    {
        "feature_name": "post_event_window_placeholder",
        "fusion_family": "fusion_family_calendar",
        "description": "Gerçekleşen olay sonrası zaman penceresi bayrağı (actual_release_time bazlı).",
        "non_signal": True,
        "status_label": "fusion_ready",
    },
]


def build_calendar_event_window_feature_registry(
    profile: FusionFeatureProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_fusion_feature_profile()
    df = pd.DataFrame(CALENDAR_WINDOW_FEATURES)
    summary = summarize_calendar_event_window_features(df)
    summary["active_profile"] = active_profile.name
    summary["status"] = "READY"
    return df, summary


def add_pre_event_window_placeholder(
    df: pd.DataFrame,
    timestamp_field: str = "timestamp",
    event_time_field: str = "scheduled_time",
    window_hours: int = 24,
    output_field: str | None = None,
) -> pd.DataFrame:
    result = df.copy()
    col = output_field or f"is_pre_event_{window_hours}h"
    if timestamp_field in result.columns and event_time_field in result.columns:
        ts = pd.to_datetime(result[timestamp_field])
        ev = pd.to_datetime(result[event_time_field])
        diff_h = (ev - ts).dt.total_seconds() / 3600.0
        result[col] = (diff_h > 0) & (diff_h <= window_hours)
    else:
        result[col] = False
    return result


def add_post_event_window_placeholder(
    df: pd.DataFrame,
    timestamp_field: str = "timestamp",
    event_time_field: str = "actual_release_time",
    window_hours: int = 24,
    output_field: str | None = None,
) -> pd.DataFrame:
    result = df.copy()
    col = output_field or f"is_post_event_{window_hours}h"
    if timestamp_field in result.columns and event_time_field in result.columns:
        ts = pd.to_datetime(result[timestamp_field])
        ev = pd.to_datetime(result[event_time_field])
        diff_h = (ev - ts).dt.total_seconds() / 3600.0
        result[col] = (diff_h <= 0) & (abs(diff_h) <= window_hours)
    else:
        result[col] = False
    return result


def summarize_calendar_event_window_features(df: pd.DataFrame) -> Dict[str, Any]:
    if df.empty:
        return {"total_features": 0, "status": "EMPTY"}
    return {
        "total_features": len(df),
        "non_signal_guaranteed": bool(df["non_signal"].all()),
        "status": "READY",
    }
