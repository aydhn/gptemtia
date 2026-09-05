from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_feature_engine.feature_engine_config import FeatureEngineProfile
from advanced_feature_engine.feature_engine_models import (
    IndicatorCatalogItem,
    build_indicator_catalog_id,
)

MOMENTUM_INDICATORS: List[Dict[str, Any]] = [
    {
        "indicator_name": "RSI",
        "indicator_family": "momentum",
        "feature_type": "feature_type_momentum",
        "dataset_types": ["dataset_fx_ohlcv", "dataset_commodity_ohlcv"],
        "required_fields": ["close"],
        "default_windows": [14],
        "formula_note": "100 - (100 / (1 + RS)) where RS = rolling_gain / rolling_loss",
        "non_signal_usage_note": "Göreceli güç endeksi osilatörü; 'RSI düşük -> kesin al' yorumu kesinlikle yasaktır.",
        "manual_review_required": False,
    },
    {
        "indicator_name": "ROC",
        "indicator_family": "momentum",
        "feature_type": "feature_type_momentum",
        "dataset_types": ["dataset_fx_ohlcv", "dataset_commodity_ohlcv"],
        "required_fields": ["close"],
        "default_windows": [10, 20],
        "formula_note": "(close - close.shift(window)) / close.shift(window) * 100",
        "non_signal_usage_note": "Değişim oranı momentum göstergesi; sinyal üretmez.",
        "manual_review_required": False,
    },
    {
        "indicator_name": "momentum",
        "indicator_family": "momentum",
        "feature_type": "feature_type_momentum",
        "dataset_types": ["dataset_fx_ohlcv", "dataset_commodity_ohlcv"],
        "required_fields": ["close"],
        "default_windows": [10, 14],
        "formula_note": "close - close.shift(window)",
        "non_signal_usage_note": "Fiyat farkı metriği; sinyal veya işlem tavsiyesi değildir.",
        "manual_review_required": False,
    },
    {
        "indicator_name": "stochastic_placeholder",
        "indicator_family": "momentum",
        "feature_type": "feature_type_momentum",
        "dataset_types": ["dataset_fx_ohlcv", "dataset_commodity_ohlcv"],
        "required_fields": ["high", "low", "close"],
        "default_windows": [14, 3],
        "formula_note": "%K = (close - lowest_low)/(highest_high - lowest_low)*100 placeholder",
        "non_signal_usage_note": "Stokastik osilatör konumu; alım satım kararı üretmez.",
        "manual_review_required": False,
    },
    {
        "indicator_name": "williams_r_placeholder",
        "indicator_family": "momentum",
        "feature_type": "feature_type_momentum",
        "dataset_types": ["dataset_fx_ohlcv", "dataset_commodity_ohlcv"],
        "required_fields": ["high", "low", "close"],
        "default_windows": [14],
        "formula_note": "(highest_high - close)/(highest_high - lowest_low)*(-100) placeholder",
        "non_signal_usage_note": "Williams %R osilatörü; sinyal değildir.",
        "manual_review_required": False,
    },
    {
        "indicator_name": "CCI_placeholder",
        "indicator_family": "momentum",
        "feature_type": "feature_type_momentum",
        "dataset_types": ["dataset_fx_ohlcv", "dataset_commodity_ohlcv"],
        "required_fields": ["high", "low", "close"],
        "default_windows": [20],
        "formula_note": "(Typical_Price - SMA) / (0.015 * Mean_Deviation) placeholder",
        "non_signal_usage_note": "Emtia kanal endeksi placeholder'ı; sinyal üretmez.",
        "manual_review_required": False,
    },
]


def build_momentum_indicator_catalog(
    profile: FeatureEngineProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    items: List[Dict[str, Any]] = []
    for row in MOMENTUM_INDICATORS:
        item = IndicatorCatalogItem(
            indicator_id=build_indicator_catalog_id(row["indicator_name"], row["indicator_family"]),
            indicator_name=row["indicator_name"],
            indicator_family=row["indicator_family"],
            feature_type=row["feature_type"],
            dataset_types=list(row["dataset_types"]),
            required_fields=list(row["required_fields"]),
            default_windows=list(row["default_windows"]),
            formula_note=row["formula_note"],
            non_signal_usage_note=row["non_signal_usage_note"],
            manual_review_required=row["manual_review_required"],
        )
        items.append(item.to_dict())

    df = pd.DataFrame.from_records(items)
    summary = {
        "family": "momentum",
        "total_indicators": len(df),
        "all_non_signal": True,
        "indicators": df["indicator_name"].tolist() if not df.empty else [],
    }
    return df, summary
