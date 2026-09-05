from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_feature_engine.feature_engine_config import FeatureEngineProfile
from advanced_feature_engine.feature_engine_models import (
    IndicatorCatalogItem,
    build_indicator_catalog_id,
)

VOLATILITY_INDICATORS: List[Dict[str, Any]] = [
    {
        "indicator_name": "rolling_std",
        "indicator_family": "volatility",
        "feature_type": "feature_type_volatility",
        "dataset_types": ["dataset_fx_ohlcv", "dataset_commodity_ohlcv"],
        "required_fields": ["close"],
        "default_windows": [10, 20, 50],
        "formula_note": "close.rolling(window).std()",
        "non_signal_usage_note": "Fiyat standart sapması; risk ölçüsü olarak kullanılır, sinyal değildir.",
        "manual_review_required": False,
    },
    {
        "indicator_name": "ATR",
        "indicator_family": "volatility",
        "feature_type": "feature_type_volatility",
        "dataset_types": ["dataset_fx_ohlcv", "dataset_commodity_ohlcv"],
        "required_fields": ["high", "low", "close"],
        "default_windows": [14],
        "formula_note": "Average True Range rolling mean over window",
        "non_signal_usage_note": "Volatilite büyüklüğü metriğidir; kesin işlem tavsiyesi içermez.",
        "manual_review_required": False,
    },
    {
        "indicator_name": "true_range",
        "indicator_family": "volatility",
        "feature_type": "feature_type_volatility",
        "dataset_types": ["dataset_fx_ohlcv", "dataset_commodity_ohlcv"],
        "required_fields": ["high", "low", "close"],
        "default_windows": [1],
        "formula_note": "max(high - low, abs(high - close.shift(1)), abs(low - close.shift(1)))",
        "non_signal_usage_note": "Tek çubuk gerçek aralık metriği; sinyal üretmez.",
        "manual_review_required": False,
    },
    {
        "indicator_name": "bollinger_band_width_placeholder",
        "indicator_family": "volatility",
        "feature_type": "feature_type_volatility",
        "dataset_types": ["dataset_fx_ohlcv", "dataset_commodity_ohlcv"],
        "required_fields": ["close"],
        "default_windows": [20],
        "formula_note": "(Upper_Band - Lower_Band) / Middle_Band placeholder",
        "non_signal_usage_note": "Bant genişliği sıkışma ölçüsü; patlama/kırılım sinyali değildir.",
        "manual_review_required": False,
    },
    {
        "indicator_name": "parkinson_volatility_placeholder",
        "indicator_family": "volatility",
        "feature_type": "feature_type_volatility",
        "dataset_types": ["dataset_fx_ohlcv", "dataset_commodity_ohlcv"],
        "required_fields": ["high", "low"],
        "default_windows": [20],
        "formula_note": "High-Low bazlı Parkinson volatilite tahmincisi placeholder'ı",
        "non_signal_usage_note": "Volatilite kestirimi; işlem sinyali değildir.",
        "manual_review_required": False,
    },
    {
        "indicator_name": "garman_klass_volatility_placeholder",
        "indicator_family": "volatility",
        "feature_type": "feature_type_volatility",
        "dataset_types": ["dataset_fx_ohlcv", "dataset_commodity_ohlcv"],
        "required_fields": ["open", "high", "low", "close"],
        "default_windows": [20],
        "formula_note": "OHLC bazlı Garman-Klass volatilite tahmincisi placeholder'ı",
        "non_signal_usage_note": "Genişletilmiş volatilite tahmincisi; sinyal üretmez.",
        "manual_review_required": False,
    },
    {
        "indicator_name": "realized_volatility_placeholder",
        "indicator_family": "volatility",
        "feature_type": "feature_type_volatility",
        "dataset_types": ["dataset_fx_ohlcv", "dataset_commodity_ohlcv"],
        "required_fields": ["close"],
        "default_windows": [20],
        "formula_note": "sqrt(sum(return^2)) * sqrt(annualization_factor) placeholder",
        "non_signal_usage_note": "Gerçekleşen volatilite; risk yönetimi analiz metriğidir, sinyal değildir.",
        "manual_review_required": False,
    },
]


def build_volatility_indicator_catalog(
    profile: FeatureEngineProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    items: List[Dict[str, Any]] = []
    for row in VOLATILITY_INDICATORS:
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
        "family": "volatility",
        "total_indicators": len(df),
        "all_non_signal": True,
        "indicators": df["indicator_name"].tolist() if not df.empty else [],
    }
    return df, summary
