from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_feature_fusion.fusion_feature_config import (
    FusionFeatureProfile,
    get_default_fusion_feature_profile,
)


NEWS_TAG_FEATURES: List[Dict[str, Any]] = [
    {
        "feature_name": "news_asset_tag_count_placeholder",
        "fusion_family": "fusion_family_news_metadata",
        "description": "Haber metadata kaydında bulunan varlık etiketleri sayısı.",
        "input_field": "asset_tags",
        "non_signal": True,
        "status_label": "fusion_ready",
    },
    {
        "feature_name": "news_macro_tag_count_placeholder",
        "fusion_family": "fusion_family_news_metadata",
        "description": "Haber metadata kaydında bulunan makro etiketleri sayısı.",
        "input_field": "macro_tags",
        "non_signal": True,
        "status_label": "fusion_ready",
    },
]


def build_news_asset_tag_feature_fusion_registry(
    profile: FusionFeatureProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_fusion_feature_profile()
    df = pd.DataFrame(NEWS_TAG_FEATURES)
    summary = summarize_news_asset_tag_feature_fusion(df)
    summary["active_profile"] = active_profile.name
    summary["status"] = "READY"
    return df, summary


def add_news_asset_tag_count_placeholder(
    df: pd.DataFrame,
    tag_field: str = "asset_tags",
    output_field: str = "news_asset_tag_count_placeholder",
) -> pd.DataFrame:
    result = df.copy()
    if tag_field in result.columns:
        result[output_field] = result[tag_field].apply(
            lambda x: len(str(x).split(",")) if pd.notna(x) and str(x).strip() != "" else 0
        )
    else:
        result[output_field] = 0
    return result


def add_news_macro_tag_count_placeholder(
    df: pd.DataFrame,
    tag_field: str = "macro_tags",
    output_field: str = "news_macro_tag_count_placeholder",
) -> pd.DataFrame:
    result = df.copy()
    if tag_field in result.columns:
        result[output_field] = result[tag_field].apply(
            lambda x: len(str(x).split(",")) if pd.notna(x) and str(x).strip() != "" else 0
        )
    else:
        result[output_field] = 0
    return result


def summarize_news_asset_tag_feature_fusion(df: pd.DataFrame) -> Dict[str, Any]:
    if df.empty:
        return {"total_features": 0, "status": "EMPTY"}
    return {
        "total_features": len(df),
        "metadata_only": True,
        "non_signal_guaranteed": bool(df["non_signal"].all()),
        "status": "READY",
    }
