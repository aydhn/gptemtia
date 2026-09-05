from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_feature_engine.feature_engine_config import FeatureEngineProfile
from advanced_feature_engine.feature_engine_models import (
    FeatureSchema,
    build_feature_schema_id,
)

NEWS_METADATA_FEATURES: List[Dict[str, Any]] = [
    {
        "feature_name": "news_topic_flag_placeholder",
        "feature_type": "feature_type_news_metadata",
        "dataset_type": "dataset_news_metadata",
        "output_field": "news_topic_flag_placeholder",
        "value_type": "int",
        "lookback_window": None,
        "required_input_fields": ["news_id", "topic_tags"],
        "non_signal": True,
        "manual_review_required": False,
        "formula_note": "Belirli bir makro/emtia konusunun varlık bayrağı (sıfır tam metin)",
        "description": "Konu etiketi varlığı; haber içeriği indirmez, telif korumalıdır, sinyal değildir.",
    },
    {
        "feature_name": "news_asset_tag_count_placeholder",
        "feature_type": "feature_type_news_metadata",
        "dataset_type": "dataset_news_metadata",
        "output_field": "news_asset_tag_count_placeholder",
        "value_type": "int",
        "lookback_window": None,
        "required_input_fields": ["asset_tags"],
        "non_signal": True,
        "manual_review_required": False,
        "formula_note": "Haber kaydına bağlı varlık etiketi adedi",
        "description": "Varlık etiketleme yoğunluğu; içerik metni içermez, sinyal üretmez.",
    },
    {
        "feature_name": "news_macro_tag_count_placeholder",
        "feature_type": "feature_type_news_metadata",
        "dataset_type": "dataset_news_metadata",
        "output_field": "news_macro_tag_count_placeholder",
        "value_type": "int",
        "lookback_window": None,
        "required_input_fields": ["macro_tags"],
        "non_signal": True,
        "manual_review_required": False,
        "formula_note": "Haber kaydına bağlı makroekonomik tema etiketi adedi",
        "description": "Makro etiket sıklığı; haber özet veya metni içermez.",
    },
    {
        "feature_name": "news_event_linkage_flag_placeholder",
        "feature_type": "feature_type_news_metadata",
        "dataset_type": "dataset_news_metadata",
        "output_field": "news_event_linkage_flag_placeholder",
        "value_type": "int",
        "lookback_window": None,
        "required_input_fields": ["news_id"],
        "non_signal": True,
        "manual_review_required": False,
        "formula_note": "Takvim olayı ile haber metadata eşleşme bayrağı",
        "description": "Haber ve ekonomik takvim olayı ilişkilendirme bayrağı; sinyal değildir.",
    },
    {
        "feature_name": "news_freshness_placeholder",
        "feature_type": "feature_type_news_metadata",
        "dataset_type": "dataset_news_metadata",
        "output_field": "news_freshness_placeholder",
        "value_type": "float",
        "lookback_window": None,
        "required_input_fields": ["timestamp"],
        "non_signal": True,
        "manual_review_required": False,
        "formula_note": "exp(-decay * elapsed_hours)",
        "description": "Haber metadata zaman tazeliği katsayısı; sinyal değildir.",
    },
    {
        "feature_name": "news_attention_placeholder",
        "feature_type": "feature_type_news_metadata",
        "dataset_type": "dataset_news_metadata",
        "output_field": "news_attention_placeholder",
        "value_type": "float",
        "lookback_window": 24,
        "required_input_fields": ["news_id"],
        "non_signal": True,
        "manual_review_required": False,
        "formula_note": "24 saatlik pencerede konu etiket frekansı placeholder'ı",
        "description": "Piyasa dikkat/ilgi yoğunluğu; kesin yönlü alım/satım tavsiyesi içermez.",
    },
]


def build_news_metadata_feature_catalog(
    profile: FeatureEngineProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    items: List[Dict[str, Any]] = []
    for row in NEWS_METADATA_FEATURES:
        item = FeatureSchema(
            schema_id=build_feature_schema_id(row["feature_name"], row["dataset_type"]),
            feature_name=row["feature_name"],
            feature_type=row["feature_type"],
            dataset_type=row["dataset_type"],
            output_field=row["output_field"],
            value_type=row["value_type"],
            lookback_window=row["lookback_window"],
            required_input_fields=list(row["required_input_fields"]),
            non_signal=True,
            manual_review_required=row["manual_review_required"],
        )
        d = item.to_dict()
        d["formula_note"] = row["formula_note"]
        d["description"] = row["description"]
        items.append(d)

    df = pd.DataFrame.from_records(items)
    summary = {
        "catalog": "news_metadata_features",
        "total_features": len(df),
        "all_non_signal": True,
        "features": df["feature_name"].tolist() if not df.empty else [],
        "zero_full_text_enforced": True,
    }
    return df, summary
