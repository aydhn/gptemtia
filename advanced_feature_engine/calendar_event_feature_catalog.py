from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_feature_engine.feature_engine_config import FeatureEngineProfile
from advanced_feature_engine.feature_engine_models import (
    FeatureSchema,
    build_feature_schema_id,
)

CALENDAR_EVENT_FEATURES: List[Dict[str, Any]] = [
    {
        "feature_name": "event_day_flag_placeholder",
        "feature_type": "feature_type_calendar",
        "dataset_type": "dataset_calendar_event",
        "output_field": "event_day_flag_placeholder",
        "value_type": "int",
        "lookback_window": None,
        "required_input_fields": ["timestamp", "event_id"],
        "non_signal": True,
        "manual_review_required": False,
        "formula_note": "Olay günü ikili göstergesi (1=olay günü, 0=diğer)",
        "description": "Ekonomik takvim olay günü göstergesi; volatilite rejimi filtresidir, sinyal değildir.",
    },
    {
        "feature_name": "pre_event_window_flag_placeholder",
        "feature_type": "feature_type_calendar",
        "dataset_type": "dataset_calendar_event",
        "output_field": "pre_event_window_flag_placeholder",
        "value_type": "int",
        "lookback_window": None,
        "required_input_fields": ["timestamp", "event_id"],
        "non_signal": True,
        "manual_review_required": False,
        "formula_note": "Olaydan önceki N saatlik pencere bayrağı",
        "description": "Olay öncesi bekleme penceresi bayrağı; risk azaltma filtresidir.",
    },
    {
        "feature_name": "post_event_window_flag_placeholder",
        "feature_type": "feature_type_calendar",
        "dataset_type": "dataset_calendar_event",
        "output_field": "post_event_window_flag_placeholder",
        "value_type": "int",
        "lookback_window": None,
        "required_input_fields": ["timestamp", "event_id"],
        "non_signal": True,
        "manual_review_required": False,
        "formula_note": "Olaydan sonraki N saatlik pencere bayrağı",
        "description": "Olay sonrası sindirme penceresi; sinyal veya yönlü işlem üretmez.",
    },
    {
        "feature_name": "event_importance_weight_placeholder",
        "feature_type": "feature_type_calendar",
        "dataset_type": "dataset_calendar_event",
        "output_field": "event_importance_weight_placeholder",
        "value_type": "float",
        "lookback_window": None,
        "required_input_fields": ["impact"],
        "non_signal": True,
        "manual_review_required": False,
        "formula_note": "Önem derecesi ağırlığı (High=1.0, Medium=0.5, Low=0.2)",
        "description": "Takvim olayı etki ağırlığı; sinyal değildir.",
    },
    {
        "feature_name": "release_delay_placeholder",
        "feature_type": "feature_type_calendar",
        "dataset_type": "dataset_release_event",
        "output_field": "release_delay_placeholder",
        "value_type": "int",
        "lookback_window": None,
        "required_input_fields": ["scheduled_time", "release_time"],
        "non_signal": True,
        "manual_review_required": False,
        "formula_note": "(release_time - scheduled_time).total_seconds()",
        "description": "Veri açıklanma gecikmesi saniyesi; operasyonel kalite metriğidir.",
    },
    {
        "feature_name": "event_surprise_placeholder",
        "feature_type": "feature_type_calendar",
        "dataset_type": "dataset_calendar_event",
        "output_field": "event_surprise_placeholder",
        "value_type": "float",
        "lookback_window": None,
        "required_input_fields": ["actual", "consensus"],
        "non_signal": True,
        "manual_review_required": False,
        "formula_note": "actual - consensus sapma büyüklüğü",
        "description": "Takvim beklenti sapması; yön tahmini veya işlem tavsiyesi içermez.",
    },
]


def build_calendar_event_feature_catalog(
    profile: FeatureEngineProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    items: List[Dict[str, Any]] = []
    for row in CALENDAR_EVENT_FEATURES:
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
        "catalog": "calendar_event_features",
        "total_features": len(df),
        "all_non_signal": True,
        "features": df["feature_name"].tolist() if not df.empty else [],
    }
    return df, summary
