from typing import Tuple, Dict, Any, List
import pandas as pd
import numpy as np

from advanced_feature_fusion.fusion_feature_config import (
    FusionFeatureProfile,
    get_default_fusion_feature_profile,
)


MACRO_FEATURES: List[Dict[str, Any]] = [
    {
        "feature_name": "macro_value_change",
        "fusion_family": "fusion_family_macro",
        "description": "Makro gösterge değerinin bir önceki release değerine göre değişimi.",
        "input_field": "value",
        "non_signal": True,
        "status_label": "fusion_ready",
    },
    {
        "feature_name": "macro_frequency_flag_placeholder",
        "fusion_family": "fusion_family_macro",
        "description": "Makro serinin yayın frekansı kategorik temsilcisi (aylık/çeyreklik).",
        "input_field": "frequency",
        "non_signal": True,
        "status_label": "fusion_ready",
    },
]


def build_macro_feature_fusion_registry(
    profile: FusionFeatureProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_fusion_feature_profile()
    df = pd.DataFrame(MACRO_FEATURES)
    summary = summarize_macro_feature_fusion(df)
    summary["active_profile"] = active_profile.name
    summary["status"] = "READY"
    return df, summary


def add_macro_value_change_feature(
    df: pd.DataFrame,
    value_field: str = "value",
    output_field: str = "macro_value_change",
) -> pd.DataFrame:
    result = df.copy()
    if value_field in result.columns:
        result[output_field] = result[value_field].diff().fillna(0.0)
    else:
        result[output_field] = 0.0
    return result


def add_macro_frequency_flag_placeholder(
    df: pd.DataFrame,
    frequency_field: str = "frequency",
    output_field: str = "macro_frequency_flag_placeholder",
) -> pd.DataFrame:
    result = df.copy()
    if frequency_field in result.columns:
        result[output_field] = result[frequency_field].astype(str).str.upper()
    else:
        result[output_field] = "UNKNOWN"
    return result


def summarize_macro_feature_fusion(df: pd.DataFrame) -> Dict[str, Any]:
    if df.empty:
        return {"total_features": 0, "status": "EMPTY"}
    return {
        "total_features": len(df),
        "non_signal_guaranteed": bool(df["non_signal"].all()),
        "status": "READY",
    }
