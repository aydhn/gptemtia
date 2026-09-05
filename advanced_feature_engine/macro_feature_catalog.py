from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_feature_engine.feature_engine_config import FeatureEngineProfile
from advanced_feature_engine.feature_engine_models import (
    FeatureSchema,
    build_feature_schema_id,
)

MACRO_FEATURES: List[Dict[str, Any]] = [
    {
        "feature_name": "macro_value_change",
        "feature_type": "feature_type_macro",
        "dataset_type": "dataset_macro_timeseries",
        "output_field": "macro_value_change",
        "value_type": "float",
        "lookback_window": 1,
        "required_input_fields": ["value"],
        "non_signal": True,
        "manual_review_required": False,
        "formula_note": "value - value.shift(1)",
        "description": "Makro gösterge periyodik mutlak değişimi; sinyal değildir.",
    },
    {
        "feature_name": "macro_rolling_change_placeholder",
        "feature_type": "feature_type_macro",
        "dataset_type": "dataset_macro_timeseries",
        "output_field": "macro_rolling_change_placeholder",
        "value_type": "float",
        "lookback_window": 12,
        "required_input_fields": ["value"],
        "non_signal": True,
        "manual_review_required": False,
        "formula_note": "value.pct_change(12) yıllık değişim placeholder'ı",
        "description": "Yıllıklandırılmış makro değişim eğilimi; sinyal değildir.",
    },
    {
        "feature_name": "macro_surprise_placeholder",
        "feature_type": "feature_type_macro",
        "dataset_type": "dataset_macro_timeseries",
        "output_field": "macro_surprise_placeholder",
        "value_type": "float",
        "lookback_window": None,
        "required_input_fields": ["value"],
        "non_signal": True,
        "manual_review_required": False,
        "formula_note": "Açıklanan - Beklenti sürpriz farkı placeholder'ı",
        "description": "Makro sürpriz sapması; piyasa reaksiyon tahmini veya emir değildir.",
    },
    {
        "feature_name": "macro_revision_flag_placeholder",
        "feature_type": "feature_type_macro",
        "dataset_type": "dataset_macro_timeseries",
        "output_field": "macro_revision_flag_placeholder",
        "value_type": "int",
        "lookback_window": None,
        "required_input_fields": ["revision_flag"],
        "non_signal": True,
        "manual_review_required": False,
        "formula_note": "Veri revizyonu varlık bayrağı (1=revize, 0=ilk açıklama)",
        "description": "Tarihsel revizyon etiketleme bayrağı; kalite filtresidir.",
    },
    {
        "feature_name": "macro_frequency_flag_placeholder",
        "feature_type": "feature_type_macro",
        "dataset_type": "dataset_macro_timeseries",
        "output_field": "macro_frequency_flag_placeholder",
        "value_type": "str",
        "lookback_window": None,
        "required_input_fields": ["frequency"],
        "non_signal": True,
        "manual_review_required": False,
        "formula_note": "Veri yayın sıklığı (M=Aylık, Q=Çeyreklik, W=Haftalık)",
        "description": "Frekans hizalama etiketidir; sinyal üretmez.",
    },
]


def build_macro_feature_catalog(
    profile: FeatureEngineProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    items: List[Dict[str, Any]] = []
    for row in MACRO_FEATURES:
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
        "catalog": "macro_features",
        "total_features": len(df),
        "all_non_signal": True,
        "features": df["feature_name"].tolist() if not df.empty else [],
    }
    return df, summary
