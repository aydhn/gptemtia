from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_feature_fusion.fusion_feature_config import (
    FusionFeatureProfile,
    get_default_fusion_feature_profile,
)


NEWS_LINKAGE_FEATURES: List[Dict[str, Any]] = [
    {
        "feature_name": "news_event_linkage_flag_placeholder",
        "fusion_family": "fusion_family_news_metadata",
        "description": "Haber metadata kaydının belirli bir ekonomik takvim olayıyla bağlantılı olup olmadığı bayrağı.",
        "input_field": "event_reference",
        "non_signal": True,
        "status_label": "fusion_ready",
    },
]


def build_news_event_linkage_feature_registry(
    profile: FusionFeatureProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_fusion_feature_profile()
    df = pd.DataFrame(NEWS_LINKAGE_FEATURES)
    summary = summarize_news_event_linkage_features(df)
    summary["active_profile"] = active_profile.name
    summary["status"] = "READY"
    return df, summary


def add_news_event_linkage_flag_placeholder(
    df: pd.DataFrame,
    event_ref_field: str = "event_reference",
    output_field: str = "news_event_linkage_flag_placeholder",
) -> pd.DataFrame:
    result = df.copy()
    if event_ref_field in result.columns:
        result[output_field] = result[event_ref_field].notna() & (result[event_ref_field].astype(str).str.strip() != "")
    else:
        result[output_field] = False
    return result


def summarize_news_event_linkage_features(df: pd.DataFrame) -> Dict[str, Any]:
    if df.empty:
        return {"total_features": 0, "status": "EMPTY"}
    return {
        "total_features": len(df),
        "metadata_only": True,
        "non_signal_guaranteed": bool(df["non_signal"].all()),
        "status": "READY",
    }
