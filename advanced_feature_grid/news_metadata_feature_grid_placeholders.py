from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_feature_grid.feature_grid_config import FeatureGridProfile, get_default_feature_grid_profile


NEWS_PLACEHOLDERS = [
    {
        "placeholder_name": "news_topic_count",
        "family": "news_placeholder",
        "windows": [1, 3, 5, 10],
        "naming_pattern": "news_topic_cnt_d{window}",
        "description": "Haber başlığı kategori sayısı kayan pencere placeholder gridi.",
    },
    {
        "placeholder_name": "news_asset_tag_count",
        "family": "news_placeholder",
        "windows": [1, 3, 5, 10],
        "naming_pattern": "news_tag_cnt_d{window}",
        "description": "Varlık etiketleme sıklığı kayan pencere placeholder gridi.",
    },
    {
        "placeholder_name": "news_event_linkage",
        "family": "news_placeholder",
        "windows": [3, 7, 14],
        "naming_pattern": "news_event_link_d{window}",
        "description": "Haber-etkinlik bağlam sayısı placeholder gridi.",
    },
    {
        "placeholder_name": "news_freshness_decay",
        "family": "news_placeholder",
        "windows": [1, 3, 7],
        "naming_pattern": "news_freshness_d{window}",
        "description": "Haber tazeliği azalım katsayısı placeholder gridi.",
    },
]


def build_news_metadata_feature_grid_placeholder_registry(
    profile: FeatureGridProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_feature_grid_profile()
    rows = []
    for p in NEWS_PLACEHOLDERS:
        for w in p["windows"]:
            rows.append({
                "placeholder_name": p["placeholder_name"],
                "family": p["family"],
                "window": w,
                "column_name": p["naming_pattern"].format(window=w),
                "is_placeholder": True,
                "no_full_text": True,
                "non_signal": True,
                "directional_claim": False,
            })

    df = pd.DataFrame(rows)
    summary = {
        "profile": active_profile.name,
        "total_placeholders": len(df),
        "no_full_text": True,
        "non_signal": True,
        "status": "PLACEHOLDER_ONLY",
    }
    return df, summary
