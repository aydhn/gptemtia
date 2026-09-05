from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_feature_fusion.fusion_feature_config import (
    FusionFeatureProfile,
    get_default_fusion_feature_profile,
)


EVENT_IMPORTANCE_FEATURES: List[Dict[str, Any]] = [
    {
        "feature_name": "event_importance_weight_placeholder",
        "fusion_family": "fusion_family_calendar",
        "description": "Olay önem derecesinin [0, 1] aralığında normalize ağırlık temsilcisi.",
        "input_field": "importance",
        "non_signal": True,
        "status_label": "fusion_placeholder_only",
    },
]


def build_event_importance_feature_placeholder_registry(
    profile: FusionFeatureProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_fusion_feature_profile()
    df = pd.DataFrame(EVENT_IMPORTANCE_FEATURES)
    summary = summarize_event_importance_feature_placeholders(df)
    summary["active_profile"] = active_profile.name
    summary["status"] = "READY"
    return df, summary


def add_event_importance_weight_placeholder(
    df: pd.DataFrame,
    importance_field: str = "importance",
    output_field: str = "event_importance_weight_placeholder",
) -> pd.DataFrame:
    result = df.copy()
    mapping = {"high": 1.0, "medium": 0.5, "low": 0.2, "3": 1.0, "2": 0.5, "1": 0.2}
    if importance_field in result.columns:
        result[output_field] = (
            result[importance_field]
            .astype(str)
            .str.lower()
            .map(mapping)
            .fillna(0.1)
        )
    else:
        result[output_field] = 0.1
    return result


def summarize_event_importance_feature_placeholders(df: pd.DataFrame) -> Dict[str, Any]:
    if df.empty:
        return {"total_placeholders": 0, "status": "EMPTY"}
    return {
        "total_placeholders": len(df),
        "non_signal_guaranteed": bool(df["non_signal"].all()),
        "status": "READY",
    }
