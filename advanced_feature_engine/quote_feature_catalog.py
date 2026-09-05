from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_feature_engine.feature_engine_config import FeatureEngineProfile
from advanced_feature_engine.feature_engine_models import (
    FeatureSchema,
    build_feature_schema_id,
)

QUOTE_FEATURES: List[Dict[str, Any]] = [
    {
        "feature_name": "bid_ask_spread",
        "feature_type": "feature_type_quote",
        "dataset_type": "dataset_fx_quote",
        "output_field": "bid_ask_spread",
        "value_type": "float",
        "lookback_window": None,
        "required_input_fields": ["bid", "ask"],
        "non_signal": True,
        "manual_review_required": False,
        "formula_note": "ask - bid",
        "description": "Kote alış-satış mutlak farkı; likidite maliyeti araştırması içindir, sinyal değildir.",
    },
    {
        "feature_name": "bid_ask_spread_pct",
        "feature_type": "feature_type_quote",
        "dataset_type": "dataset_fx_quote",
        "output_field": "bid_ask_spread_pct",
        "value_type": "float",
        "lookback_window": None,
        "required_input_fields": ["bid", "ask"],
        "non_signal": True,
        "manual_review_required": False,
        "formula_note": "(ask - bid) / ((bid + ask) / 2)",
        "description": "Yüzdesel spread oranı; işlem maliyeti filtresi metriğidir.",
    },
    {
        "feature_name": "mid_price",
        "feature_type": "feature_type_quote",
        "dataset_type": "dataset_fx_quote",
        "output_field": "mid_price",
        "value_type": "float",
        "lookback_window": None,
        "required_input_fields": ["bid", "ask"],
        "non_signal": True,
        "manual_review_required": False,
        "formula_note": "(bid + ask) / 2",
        "description": "Kote orta fiyatı; referans fiyat seviyesidir, sinyal değildir.",
    },
    {
        "feature_name": "quote_imbalance_placeholder",
        "feature_type": "feature_type_quote",
        "dataset_type": "dataset_fx_quote",
        "output_field": "quote_imbalance_placeholder",
        "value_type": "float",
        "lookback_window": None,
        "required_input_fields": ["bid", "ask"],
        "non_signal": True,
        "manual_review_required": False,
        "formula_note": "Kote dengesizlik oranı placeholder'ı",
        "description": "Teklif dengesizliği placeholder'ı; kesin yön tahmini içermez.",
    },
    {
        "feature_name": "quote_staleness_flag_placeholder",
        "feature_type": "feature_type_quote",
        "dataset_type": "dataset_fx_quote",
        "output_field": "quote_staleness_flag_placeholder",
        "value_type": "int",
        "lookback_window": None,
        "required_input_fields": ["timestamp"],
        "non_signal": True,
        "manual_review_required": False,
        "formula_note": "Bayat veri tespit bayrağı (1=bayat, 0=güncel)",
        "description": "Fiyat tazelik kalite bayrağı; filtreleme amaçlıdır.",
    },
]


def build_quote_feature_catalog(
    profile: FeatureEngineProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    items: List[Dict[str, Any]] = []
    for row in QUOTE_FEATURES:
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
        "catalog": "quote_features",
        "total_features": len(df),
        "all_non_signal": True,
        "features": df["feature_name"].tolist() if not df.empty else [],
    }
    return df, summary
