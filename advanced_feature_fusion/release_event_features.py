from typing import Tuple, Dict, Any, List
import pandas as pd
import numpy as np

from advanced_feature_fusion.fusion_feature_config import (
    FusionFeatureProfile,
    get_default_fusion_feature_profile,
)


RELEASE_FEATURES: List[Dict[str, Any]] = [
    {
        "feature_name": "release_delay_placeholder",
        "fusion_family": "fusion_family_release_event",
        "description": "Planlanan zaman ile gerçekleşen yayın zamanı arasındaki gecikme (dakika).",
        "non_signal": True,
        "status_label": "fusion_ready",
    },
    {
        "feature_name": "release_has_actual_flag",
        "fusion_family": "fusion_family_release_event",
        "description": "Actual değerinin yayınlanıp yayınlanmadığını belirten ikili bayrak.",
        "non_signal": True,
        "status_label": "fusion_ready",
    },
    {
        "feature_name": "release_revised_previous_flag",
        "fusion_family": "fusion_family_release_event",
        "description": "Önceki döneme ait değerin bu bültende revize edilip edilmediği bayrağı.",
        "non_signal": True,
        "status_label": "fusion_ready",
    },
]


def build_release_event_feature_registry(
    profile: FusionFeatureProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_fusion_feature_profile()
    df = pd.DataFrame(RELEASE_FEATURES)
    summary = summarize_release_event_features(df)
    summary["active_profile"] = active_profile.name
    summary["status"] = "READY"
    return df, summary


def add_release_delay_placeholder(
    df: pd.DataFrame,
    scheduled_field: str = "scheduled_time",
    actual_field: str = "actual_release_time",
    output_field: str = "release_delay_placeholder",
) -> pd.DataFrame:
    result = df.copy()
    if scheduled_field in result.columns and actual_field in result.columns:
        sch = pd.to_datetime(result[scheduled_field])
        act = pd.to_datetime(result[actual_field])
        result[output_field] = ((act - sch).dt.total_seconds() / 60.0).fillna(0.0)
    else:
        result[output_field] = 0.0
    return result


def add_release_has_actual_flag(
    df: pd.DataFrame,
    actual_field: str = "actual",
    output_field: str = "release_has_actual_flag",
) -> pd.DataFrame:
    result = df.copy()
    if actual_field in result.columns:
        result[output_field] = result[actual_field].notna() & (result[actual_field] != "")
    else:
        result[output_field] = False
    return result


def add_release_revised_previous_flag(
    df: pd.DataFrame,
    revised_field: str = "revised_previous",
    output_field: str = "release_revised_previous_flag",
) -> pd.DataFrame:
    result = df.copy()
    if revised_field in result.columns:
        result[output_field] = result[revised_field].notna() & (result[revised_field] != "")
    else:
        result[output_field] = False
    return result


def summarize_release_event_features(df: pd.DataFrame) -> Dict[str, Any]:
    if df.empty:
        return {"total_features": 0, "status": "EMPTY"}
    return {
        "total_features": len(df),
        "non_signal_guaranteed": bool(df["non_signal"].all()),
        "status": "READY",
    }
