from typing import Any

import numpy as np
import pandas as pd

from advanced_feature_fusion.fusion_feature_config import (
    FusionFeatureProfile,
    get_default_fusion_feature_profile,
)

NEWS_TOPIC_FEATURES: list[dict[str, Any]] = [
    {
        "feature_name": "news_topic_flag_placeholder",
        "fusion_family": "fusion_family_news_metadata",
        "description": "Haber metadata konusunun belirli bir makro kategoriye (faiz, enflasyon, enerji) ait olup olmadığını belirten bayrak.",
        "non_signal": True,
        "status_label": "fusion_ready",
    },
    {
        "feature_name": "news_topic_count_placeholder",
        "fusion_family": "fusion_family_news_metadata",
        "description": "Haber metadata kaydında bulunan konu kategorisi sayısı.",
        "non_signal": True,
        "status_label": "fusion_ready",
    },
]


def build_news_topic_feature_fusion_registry(
    profile: FusionFeatureProfile | None = None,
) -> tuple[pd.DataFrame, dict[str, Any]]:
    active_profile = profile or get_default_fusion_feature_profile()
    df = pd.DataFrame(NEWS_TOPIC_FEATURES)
    summary = summarize_news_topic_feature_fusion(df)
    summary["active_profile"] = active_profile.name
    summary["status"] = "READY"
    return df, summary


def add_news_topic_flag_placeholder(
    df: pd.DataFrame,
    topic_field: str = "topic",
    topic_value: str | None = None,
    output_field: str | None = None,
) -> pd.DataFrame:
    result = df.copy()
    target_topic = topic_value or "rates"
    col = output_field or f"has_topic_{target_topic}"
    if topic_field in result.columns:
        result[col] = (
            result[topic_field]
            .astype(str)
            .str.lower()
            .str.contains(target_topic.lower())
        )
    else:
        result[col] = False
    return result


def add_news_topic_count_placeholder(
    df: pd.DataFrame,
    topic_field: str = "topic",
    output_field: str = "news_topic_count_placeholder",
) -> pd.DataFrame:
    result = df.copy()
    if topic_field in result.columns:
        s_str = result[topic_field].fillna("").astype(str)
        counts = s_str.str.count(",") + 1
        result[output_field] = np.where(s_str.str.strip() == "", 0, counts)
    else:
        result[output_field] = 0
    return result


def summarize_news_topic_feature_fusion(df: pd.DataFrame) -> dict[str, Any]:
    if df.empty:
        return {"total_features": 0, "status": "EMPTY"}
    return {
        "total_features": len(df),
        "metadata_only": True,
        "non_signal_guaranteed": bool(df["non_signal"].all()),
        "status": "READY",
    }
