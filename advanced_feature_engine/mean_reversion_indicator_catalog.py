from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_feature_engine.feature_engine_config import FeatureEngineProfile
from advanced_feature_engine.feature_engine_models import (
    IndicatorCatalogItem,
    build_indicator_catalog_id,
)

MEAN_REVERSION_INDICATORS: List[Dict[str, Any]] = [
    {
        "indicator_name": "zscore",
        "indicator_family": "mean_reversion",
        "feature_type": "feature_type_mean_reversion",
        "dataset_types": ["dataset_fx_ohlcv", "dataset_commodity_ohlcv"],
        "required_fields": ["close"],
        "default_windows": [20],
        "formula_note": "(close - rolling_mean) / rolling_std",
        "non_signal_usage_note": "Normalleştirilmiş standart sapma mesafesi; kesin dönüş sinyali değildir.",
        "manual_review_required": False,
    },
    {
        "indicator_name": "bollinger_zscore",
        "indicator_family": "mean_reversion",
        "feature_type": "feature_type_mean_reversion",
        "dataset_types": ["dataset_fx_ohlcv", "dataset_commodity_ohlcv"],
        "required_fields": ["close"],
        "default_windows": [20],
        "formula_note": "(close - SMA20) / (2 * STD20)",
        "non_signal_usage_note": "Bollinger orta bandına göre normalize konum; işlem sinyali değildir.",
        "manual_review_required": False,
    },
    {
        "indicator_name": "distance_to_sma",
        "indicator_family": "mean_reversion",
        "feature_type": "feature_type_mean_reversion",
        "dataset_types": ["dataset_fx_ohlcv", "dataset_commodity_ohlcv"],
        "required_fields": ["close"],
        "default_windows": [20, 50],
        "formula_note": "(close - SMA) / SMA",
        "non_signal_usage_note": "Basit hareketli ortalamaya yüzde uzaklık; sinyal değildir.",
        "manual_review_required": False,
    },
    {
        "indicator_name": "distance_to_ema",
        "indicator_family": "mean_reversion",
        "feature_type": "feature_type_mean_reversion",
        "dataset_types": ["dataset_fx_ohlcv", "dataset_commodity_ohlcv"],
        "required_fields": ["close"],
        "default_windows": [20],
        "formula_note": "(close - EMA) / EMA",
        "non_signal_usage_note": "Üstel hareketli ortalamaya yüzde uzaklık; sinyal değildir.",
        "manual_review_required": False,
    },
    {
        "indicator_name": "percentile_rank_placeholder",
        "indicator_family": "mean_reversion",
        "feature_type": "feature_type_mean_reversion",
        "dataset_types": ["dataset_fx_ohlcv", "dataset_commodity_ohlcv"],
        "required_fields": ["close"],
        "default_windows": [50, 100],
        "formula_note": "Pencere içindeki yüzdelik dilim konumu placeholder'ı",
        "non_signal_usage_note": "Yüzdelik sıra konumu; al/sat göstergesi değildir.",
        "manual_review_required": False,
    },
    {
        "indicator_name": "rolling_deviation_placeholder",
        "indicator_family": "mean_reversion",
        "feature_type": "feature_type_mean_reversion",
        "dataset_types": ["dataset_fx_ohlcv", "dataset_commodity_ohlcv"],
        "required_fields": ["close"],
        "default_windows": [20],
        "formula_note": "Ortalama mutlak sapma (MAD) placeholder'ı",
        "non_signal_usage_note": "Fiyat dağılım genişliği; sinyal üretmez.",
        "manual_review_required": False,
    },
]


def build_mean_reversion_indicator_catalog(
    profile: FeatureEngineProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    items: List[Dict[str, Any]] = []
    for row in MEAN_REVERSION_INDICATORS:
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
        "family": "mean_reversion",
        "total_indicators": len(df),
        "all_non_signal": True,
        "indicators": df["indicator_name"].tolist() if not df.empty else [],
    }
    return df, summary
