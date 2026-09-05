from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_feature_fusion.fusion_feature_config import (
    FusionFeatureProfile,
    get_default_fusion_feature_profile,
)


MACRO_REVISION_FEATURES: List[Dict[str, Any]] = [
    {
        "feature_name": "macro_revision_flag_placeholder",
        "fusion_family": "fusion_family_macro",
        "description": "Veri serisinde geçmiş döneme ait revizyon yapılıp yapılmadığını belirten bayrak temsilcisi.",
        "input_field": "revision_status",
        "non_signal": True,
        "status_label": "fusion_placeholder_only",
    },
]


def build_macro_revision_feature_placeholder_registry(
    profile: FusionFeatureProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_fusion_feature_profile()
    df = pd.DataFrame(MACRO_REVISION_FEATURES)
    summary = summarize_macro_revision_feature_placeholders(df)
    summary["active_profile"] = active_profile.name
    summary["status"] = "READY"
    return df, summary


def add_macro_revision_flag_placeholder(
    df: pd.DataFrame,
    revision_status_field: str = "revision_status",
    output_field: str = "macro_revision_flag_placeholder",
) -> pd.DataFrame:
    result = df.copy()
    if revision_status_field in result.columns:
        result[output_field] = result[revision_status_field].apply(
            lambda x: True if str(x).lower() in ["revised", "revision", "true", "1"] else False
        )
    else:
        result[output_field] = False
    return result


def summarize_macro_revision_feature_placeholders(df: pd.DataFrame) -> Dict[str, Any]:
    if df.empty:
        return {"total_placeholders": 0, "status": "EMPTY"}
    return {
        "total_placeholders": len(df),
        "non_signal_guaranteed": bool(df["non_signal"].all()),
        "status": "READY",
    }
