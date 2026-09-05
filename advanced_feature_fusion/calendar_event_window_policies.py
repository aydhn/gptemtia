from typing import Tuple, Dict, Any, List
import pandas as pd
import numpy as np

from advanced_feature_fusion.fusion_feature_config import (
    FusionFeatureProfile,
    get_default_fusion_feature_profile,
)
from advanced_feature_fusion.fusion_feature_models import (
    FusionPolicy,
    build_fusion_policy_id,
)


CALENDAR_WINDOW_POLICIES: List[Dict[str, Any]] = [
    {
        "policy_name": "pre_event_window_indicator_policy",
        "policy_type": "calendar_window",
        "description": "Planlanan olay zamanından önceki zaman aralığını bayrak olarak temsil eder (yön içermez).",
        "future_data_allowed": False,
        "full_text_allowed": False,
        "destructive_action_allowed": False,
        "non_signal": True,
        "manual_review_required": False,
    },
    {
        "policy_name": "post_event_window_indicator_policy",
        "policy_type": "calendar_window",
        "description": "Gerçekleşen olay sonrasındaki zaman aralığını bayrak olarak temsil eder (sadece actual_release_time sonrası).",
        "future_data_allowed": False,
        "full_text_allowed": False,
        "destructive_action_allowed": False,
        "non_signal": True,
        "manual_review_required": False,
    },
    {
        "policy_name": "event_window_non_signal_boundary_policy",
        "policy_type": "calendar_window",
        "description": "Olay pencereleri yalnızca volatilite/rejim bağlamı içindir; kesinlikle al/sat veya pozisyon kararı oluşturamaz.",
        "future_data_allowed": False,
        "full_text_allowed": False,
        "destructive_action_allowed": False,
        "non_signal": True,
        "manual_review_required": False,
    },
]


def build_calendar_event_window_policy_registry(
    profile: FusionFeatureProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_fusion_feature_profile()
    rows = []
    for spec in CALENDAR_WINDOW_POLICIES:
        p = FusionPolicy(
            policy_id=build_fusion_policy_id(spec["policy_name"], spec["policy_type"]),
            policy_name=spec["policy_name"],
            policy_type=spec["policy_type"],
            description=spec["description"],
            future_data_allowed=spec["future_data_allowed"],
            full_text_allowed=spec["full_text_allowed"],
            destructive_action_allowed=spec["destructive_action_allowed"],
            non_signal=spec["non_signal"],
            manual_review_required=spec["manual_review_required"],
        )
        rows.append(p.to_dict())

    df = pd.DataFrame(rows)
    summary = summarize_calendar_event_window_policies(df)
    summary["active_profile"] = active_profile.name
    summary["status"] = "READY"
    return df, summary


def build_event_window_flags(
    df: pd.DataFrame,
    timestamp_field: str = "timestamp",
    event_time_field: str = "scheduled_time",
    pre_windows: List[int] | None = None,
    post_windows: List[int] | None = None,
) -> pd.DataFrame:
    """Build event window indicators without mutating input df."""
    result = df.copy()
    pre_w = pre_windows or [1, 4, 24]
    post_w = post_windows or [1, 4, 24]

    if timestamp_field not in result.columns or event_time_field not in result.columns:
        return result

    ts = pd.to_datetime(result[timestamp_field])
    ev_ts = pd.to_datetime(result[event_time_field])
    diff_hours = (ev_ts - ts).dt.total_seconds() / 3600.0

    for w in pre_w:
        col = f"is_pre_event_{w}h"
        result[col] = (diff_hours > 0) & (diff_hours <= w)

    for w in post_w:
        col = f"is_post_event_{w}h"
        result[col] = (diff_hours <= 0) & (abs(diff_hours) <= w)

    return result


def summarize_calendar_event_window_policies(df: pd.DataFrame) -> Dict[str, Any]:
    if df.empty:
        return {"total_policies": 0, "status": "EMPTY"}
    return {
        "total_policies": len(df),
        "zero_future_data_enforced": bool((~df["future_data_allowed"]).all()),
        "non_signal_guaranteed": bool(df["non_signal"].all()),
        "status": "READY",
    }


def get_calendar_event_window_policies() -> List[Dict[str, Any]]:
    """Return list of calendar event window policies."""
    return [dict(p) for p in CALENDAR_WINDOW_POLICIES]


def get_calendar_event_window_policies_summary() -> Dict[str, Any]:
    """Return summary dictionary of calendar event window policies."""
    df, summary = build_calendar_event_window_policy_registry()
    summary["policy_count"] = len(df)
    summary["default_pre_window_hours"] = 4
    summary["default_post_window_hours"] = 4
    return summary
