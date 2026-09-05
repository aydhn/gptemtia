from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_feature_engine.feature_engine_config import FeatureEngineProfile
from advanced_feature_engine.feature_engine_models import (
    FeatureSchema,
    build_feature_schema_id,
)

VOLUME_LIQUIDITY_FEATURES: List[Dict[str, Any]] = [
    {
        "feature_name": "volume_change_placeholder",
        "feature_type": "feature_type_volume_liquidity_placeholder",
        "dataset_type": "dataset_commodity_ohlcv",
        "output_field": "volume_change_placeholder",
        "value_type": "float",
        "lookback_window": 1,
        "required_input_fields": ["volume"],
        "non_signal": True,
        "manual_review_required": False,
        "formula_note": "volume.pct_change()",
        "description": "Hacim değişim oranı; katılım yoğunluğu metriğidir, sinyal değildir.",
    },
    {
        "feature_name": "rolling_volume_mean_placeholder",
        "feature_type": "feature_type_volume_liquidity_placeholder",
        "dataset_type": "dataset_commodity_ohlcv",
        "output_field": "rolling_volume_mean_placeholder",
        "value_type": "float",
        "lookback_window": 20,
        "required_input_fields": ["volume"],
        "non_signal": True,
        "manual_review_required": False,
        "formula_note": "volume.rolling(20).mean()",
        "description": "Ortalama hacim referans seviyesi; sinyal değildir.",
    },
    {
        "feature_name": "volume_zscore_placeholder",
        "feature_type": "feature_type_volume_liquidity_placeholder",
        "dataset_type": "dataset_commodity_ohlcv",
        "output_field": "volume_zscore_placeholder",
        "value_type": "float",
        "lookback_window": 20,
        "required_input_fields": ["volume"],
        "non_signal": True,
        "manual_review_required": False,
        "formula_note": "(volume - mean(volume)) / std(volume)",
        "description": "Normalize hacim sıçraması; kesin piyasa yönü üretmez.",
    },
    {
        "feature_name": "liquidity_proxy_placeholder",
        "feature_type": "feature_type_volume_liquidity_placeholder",
        "dataset_type": "dataset_commodity_ohlcv",
        "output_field": "liquidity_proxy_placeholder",
        "value_type": "float",
        "lookback_window": 20,
        "required_input_fields": ["close", "volume"],
        "non_signal": True,
        "manual_review_required": False,
        "formula_note": "Hacim ve fiyat bazlı likidite katsayısı placeholder'ı",
        "description": "Piyasa derinlik ve likidite vekili; sinyal üretmez.",
    },
    {
        "feature_name": "open_interest_change_placeholder",
        "feature_type": "feature_type_volume_liquidity_placeholder",
        "dataset_type": "dataset_commodity_ohlcv",
        "output_field": "open_interest_change_placeholder",
        "value_type": "float",
        "lookback_window": 1,
        "required_input_fields": ["open_interest"],
        "non_signal": True,
        "manual_review_required": False,
        "formula_note": "Açık pozisyon sayısı değişimi placeholder'ı",
        "description": "Vadeli açık pozisyon akışı; yönlü emir veya tavsiye değildir.",
    },
]


def build_volume_liquidity_feature_placeholder_catalog(
    profile: FeatureEngineProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    items: List[Dict[str, Any]] = []
    for row in VOLUME_LIQUIDITY_FEATURES:
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
        "catalog": "volume_liquidity_placeholders",
        "total_features": len(df),
        "all_non_signal": True,
        "features": df["feature_name"].tolist() if not df.empty else [],
    }
    return df, summary
