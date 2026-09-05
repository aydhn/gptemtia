from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_feature_engine.feature_engine_config import FeatureEngineProfile
from advanced_feature_engine.feature_engine_models import (
    IndicatorCatalogItem,
    build_indicator_catalog_id,
)

PRICE_INDICATORS: List[Dict[str, Any]] = [
    {
        "indicator_name": "close_return",
        "indicator_family": "price",
        "feature_type": "feature_type_price",
        "dataset_types": ["dataset_fx_ohlcv", "dataset_commodity_ohlcv"],
        "required_fields": ["close"],
        "default_windows": [1, 5, 20],
        "formula_note": "close.pct_change(window)",
        "non_signal_usage_note": "Fiyat getiri yüzdesi; trade sinyali veya tavsiye değildir.",
        "manual_review_required": False,
    },
    {
        "indicator_name": "log_return",
        "indicator_family": "price",
        "feature_type": "feature_type_price",
        "dataset_types": ["dataset_fx_ohlcv", "dataset_commodity_ohlcv"],
        "required_fields": ["close"],
        "default_windows": [1, 5],
        "formula_note": "np.log(close / close.shift(window))",
        "non_signal_usage_note": "Logaritmik getiri; simetrik getiri analiz metriğidir.",
        "manual_review_required": False,
    },
    {
        "indicator_name": "high_low_range",
        "indicator_family": "price",
        "feature_type": "feature_type_price",
        "dataset_types": ["dataset_fx_ohlcv", "dataset_commodity_ohlcv"],
        "required_fields": ["high", "low"],
        "default_windows": [1],
        "formula_note": "(high - low) / close",
        "non_signal_usage_note": "Normalleştirilmiş çubuk aralığı; yön bilgisi içermez.",
        "manual_review_required": False,
    },
    {
        "indicator_name": "close_to_open_return",
        "indicator_family": "price",
        "feature_type": "feature_type_price",
        "dataset_types": ["dataset_fx_ohlcv", "dataset_commodity_ohlcv"],
        "required_fields": ["open", "close"],
        "default_windows": [1],
        "formula_note": "(close - open) / open",
        "non_signal_usage_note": "Seans içi getiri metriği; sinyal değildir.",
        "manual_review_required": False,
    },
    {
        "indicator_name": "gap_placeholder",
        "indicator_family": "price",
        "feature_type": "feature_type_price",
        "dataset_types": ["dataset_fx_ohlcv", "dataset_commodity_ohlcv"],
        "required_fields": ["open", "close"],
        "default_windows": [1],
        "formula_note": "(open - close.shift(1)) / close.shift(1)",
        "non_signal_usage_note": "Açılış boşluğu büyüklüğü; yönlü tahmin iddiası içermez.",
        "manual_review_required": False,
    },
    {
        "indicator_name": "rolling_mean",
        "indicator_family": "price",
        "feature_type": "feature_type_price",
        "dataset_types": ["dataset_fx_ohlcv", "dataset_commodity_ohlcv"],
        "required_fields": ["close"],
        "default_windows": [10, 20, 50],
        "formula_note": "close.rolling(window).mean()",
        "non_signal_usage_note": "Fiyat seviyesi hareketli ortalaması; sinyal değildir.",
        "manual_review_required": False,
    },
    {
        "indicator_name": "rolling_median",
        "indicator_family": "price",
        "feature_type": "feature_type_price",
        "dataset_types": ["dataset_fx_ohlcv", "dataset_commodity_ohlcv"],
        "required_fields": ["close"],
        "default_windows": [10, 20],
        "formula_note": "close.rolling(window).median()",
        "non_signal_usage_note": "Dayanıklı merkezi eğilim ölçüsü; sinyal değildir.",
        "manual_review_required": False,
    },
    {
        "indicator_name": "rolling_min",
        "indicator_family": "price",
        "feature_type": "feature_type_price",
        "dataset_types": ["dataset_fx_ohlcv", "dataset_commodity_ohlcv"],
        "required_fields": ["low"],
        "default_windows": [10, 20],
        "formula_note": "low.rolling(window).min()",
        "non_signal_usage_note": "Pencere içi en düşük değer referansı; sinyal değildir.",
        "manual_review_required": False,
    },
    {
        "indicator_name": "rolling_max",
        "indicator_family": "price",
        "feature_type": "feature_type_price",
        "dataset_types": ["dataset_fx_ohlcv", "dataset_commodity_ohlcv"],
        "required_fields": ["high"],
        "default_windows": [10, 20],
        "formula_note": "high.rolling(window).max()",
        "non_signal_usage_note": "Pencere içi en yüksek değer referansı; sinyal değildir.",
        "manual_review_required": False,
    },
]


def build_price_indicator_catalog(
    profile: FeatureEngineProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    items: List[Dict[str, Any]] = []
    for row in PRICE_INDICATORS:
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
        "family": "price",
        "total_indicators": len(df),
        "all_non_signal": True,
        "indicators": df["indicator_name"].tolist() if not df.empty else [],
    }
    return df, summary
