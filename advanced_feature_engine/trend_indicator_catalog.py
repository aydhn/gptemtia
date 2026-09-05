from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_feature_engine.feature_engine_config import FeatureEngineProfile
from advanced_feature_engine.feature_engine_models import (
    IndicatorCatalogItem,
    build_indicator_catalog_id,
)

TREND_INDICATORS: List[Dict[str, Any]] = [
    {
        "indicator_name": "SMA",
        "indicator_family": "trend",
        "feature_type": "feature_type_trend",
        "dataset_types": ["dataset_fx_ohlcv", "dataset_commodity_ohlcv"],
        "required_fields": ["close"],
        "default_windows": [10, 20, 50, 200],
        "formula_note": "Simple moving average over specified window",
        "non_signal_usage_note": "Fiyat trend seviyesi referansı; kesişim kuralı veya AL/SAT sinyali değildir.",
        "manual_review_required": False,
    },
    {
        "indicator_name": "EMA",
        "indicator_family": "trend",
        "feature_type": "feature_type_trend",
        "dataset_types": ["dataset_fx_ohlcv", "dataset_commodity_ohlcv"],
        "required_fields": ["close"],
        "default_windows": [12, 20, 26],
        "formula_note": "Exponential moving average with smoothing alpha = 2/(span+1)",
        "non_signal_usage_note": "Ağırlıklı trend metriği; sinyal üretmez.",
        "manual_review_required": False,
    },
    {
        "indicator_name": "WMA_placeholder",
        "indicator_family": "trend",
        "feature_type": "feature_type_trend",
        "dataset_types": ["dataset_fx_ohlcv", "dataset_commodity_ohlcv"],
        "required_fields": ["close"],
        "default_windows": [20],
        "formula_note": "Linearly weighted moving average placeholder",
        "non_signal_usage_note": "Ağırlıklı ortalama placeholder'ı; kesin yön tahmini içermez.",
        "manual_review_required": False,
    },
    {
        "indicator_name": "MACD_placeholder",
        "indicator_family": "trend",
        "feature_type": "feature_type_trend",
        "dataset_types": ["dataset_fx_ohlcv", "dataset_commodity_ohlcv"],
        "required_fields": ["close"],
        "default_windows": [12, 26, 9],
        "formula_note": "EMA(fast) - EMA(slow) difference placeholder",
        "non_signal_usage_note": "Fark metriği; 'MACD yukarı -> kesin long' gibi kural kesinlikle yasaktır.",
        "manual_review_required": False,
    },
    {
        "indicator_name": "ADX_placeholder",
        "indicator_family": "trend",
        "feature_type": "feature_type_trend",
        "dataset_types": ["dataset_fx_ohlcv", "dataset_commodity_ohlcv"],
        "required_fields": ["high", "low", "close"],
        "default_windows": [14],
        "formula_note": "Average directional index trend strength placeholder",
        "non_signal_usage_note": "Trend gücü göstergesi; trade sinyali değildir.",
        "manual_review_required": False,
    },
    {
        "indicator_name": "Ichimoku_placeholder",
        "indicator_family": "trend",
        "feature_type": "feature_type_trend",
        "dataset_types": ["dataset_fx_ohlcv", "dataset_commodity_ohlcv"],
        "required_fields": ["high", "low", "close"],
        "default_windows": [9, 26, 52],
        "formula_note": "Tenkan/Kijun/Senkou lines placeholder",
        "non_signal_usage_note": "Çoklu çizgi seviye göstergesi; sinyal içermez.",
        "manual_review_required": False,
    },
    {
        "indicator_name": "Donchian_channel_placeholder",
        "indicator_family": "trend",
        "feature_type": "feature_type_trend",
        "dataset_types": ["dataset_fx_ohlcv", "dataset_commodity_ohlcv"],
        "required_fields": ["high", "low"],
        "default_windows": [20],
        "formula_note": "Highest high & lowest low channel band placeholder",
        "non_signal_usage_note": "Fiyat kanalı bantları; kırılım sinyali veya emir tetiklemez.",
        "manual_review_required": False,
    },
    {
        "indicator_name": "Keltner_channel_placeholder",
        "indicator_family": "trend",
        "feature_type": "feature_type_trend",
        "dataset_types": ["dataset_fx_ohlcv", "dataset_commodity_ohlcv"],
        "required_fields": ["high", "low", "close"],
        "default_windows": [20],
        "formula_note": "EMA +- ATR multiplier channel placeholder",
        "non_signal_usage_note": "Volatilite bazlı trend kanalı; sinyal değildir.",
        "manual_review_required": False,
    },
]


def build_trend_indicator_catalog(
    profile: FeatureEngineProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    items: List[Dict[str, Any]] = []
    for row in TREND_INDICATORS:
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
        "family": "trend",
        "total_indicators": len(df),
        "all_non_signal": True,
        "indicators": df["indicator_name"].tolist() if not df.empty else [],
    }
    return df, summary
