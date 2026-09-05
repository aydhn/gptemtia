from typing import Tuple, Dict, Any, List
import pandas as pd
import numpy as np

from advanced_feature_fusion.fusion_feature_config import (
    FusionFeatureProfile,
    get_default_fusion_feature_profile,
)


MACRO_SURPRISE_FEATURES: List[Dict[str, Any]] = [
    {
        "feature_name": "macro_surprise_placeholder",
        "fusion_family": "fusion_family_release_event",
        "description": "Actual eksi Forecast farkı temsilcisi (nötr büyüklük, sinyal değildir).",
        "input_fields": ["actual", "forecast"],
        "non_signal": True,
        "status_label": "fusion_placeholder_only",
    },
]


def build_macro_surprise_feature_placeholder_registry(
    profile: FusionFeatureProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_fusion_feature_profile()
    df = pd.DataFrame(MACRO_SURPRISE_FEATURES)
    summary = summarize_macro_surprise_feature_placeholders(df)
    summary["active_profile"] = active_profile.name
    summary["status"] = "READY"
    return df, summary


def add_macro_surprise_placeholder(
    df: pd.DataFrame,
    actual_field: str = "actual",
    forecast_field: str = "forecast",
    output_field: str = "macro_surprise_placeholder",
) -> pd.DataFrame:
    result = df.copy()
    if actual_field in result.columns and forecast_field in result.columns:
        act = pd.to_numeric(result[actual_field], errors="coerce")
        fc = pd.to_numeric(result[forecast_field], errors="coerce")
        result[output_field] = (act - fc).fillna(0.0)
    else:
        result[output_field] = 0.0
    return result


def summarize_macro_surprise_feature_placeholders(df: pd.DataFrame) -> Dict[str, Any]:
    if df.empty:
        return {"total_placeholders": 0, "status": "EMPTY"}
    return {
        "total_placeholders": len(df),
        "non_signal_guaranteed": bool(df["non_signal"].all()),
        "status": "READY",
    }
