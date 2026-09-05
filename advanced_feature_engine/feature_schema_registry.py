from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_feature_engine.feature_engine_config import FeatureEngineProfile
from advanced_feature_engine.feature_engine_models import (
    FeatureSchema,
    build_feature_schema_id,
)

DEFAULT_FEATURE_SCHEMAS: List[Dict[str, Any]] = [
    {
        "feature_name": "close_return_1",
        "feature_type": "feature_type_price",
        "dataset_type": "dataset_fx_ohlcv",
        "output_field": "close_return_1",
        "value_type": "float",
        "lookback_window": 1,
        "required_input_fields": ["close"],
        "non_signal": True,
        "manual_review_required": False,
    },
    {
        "feature_name": "close_return_5",
        "feature_type": "feature_type_price",
        "dataset_type": "dataset_fx_ohlcv",
        "output_field": "close_return_5",
        "value_type": "float",
        "lookback_window": 5,
        "required_input_fields": ["close"],
        "non_signal": True,
        "manual_review_required": False,
    },
    {
        "feature_name": "log_return_1",
        "feature_type": "feature_type_price",
        "dataset_type": "dataset_fx_ohlcv",
        "output_field": "log_return_1",
        "value_type": "float",
        "lookback_window": 1,
        "required_input_fields": ["close"],
        "non_signal": True,
        "manual_review_required": False,
    },
    {
        "feature_name": "rolling_mean_20",
        "feature_type": "feature_type_price",
        "dataset_type": "dataset_fx_ohlcv",
        "output_field": "rolling_mean_20",
        "value_type": "float",
        "lookback_window": 20,
        "required_input_fields": ["close"],
        "non_signal": True,
        "manual_review_required": False,
    },
    {
        "feature_name": "rolling_std_20",
        "feature_type": "feature_type_volatility",
        "dataset_type": "dataset_fx_ohlcv",
        "output_field": "rolling_std_20",
        "value_type": "float",
        "lookback_window": 20,
        "required_input_fields": ["close"],
        "non_signal": True,
        "manual_review_required": False,
    },
    {
        "feature_name": "sma_20",
        "feature_type": "feature_type_trend",
        "dataset_type": "dataset_fx_ohlcv",
        "output_field": "sma_20",
        "value_type": "float",
        "lookback_window": 20,
        "required_input_fields": ["close"],
        "non_signal": True,
        "manual_review_required": False,
    },
    {
        "feature_name": "ema_20",
        "feature_type": "feature_type_trend",
        "dataset_type": "dataset_fx_ohlcv",
        "output_field": "ema_20",
        "value_type": "float",
        "lookback_window": 20,
        "required_input_fields": ["close"],
        "non_signal": True,
        "manual_review_required": False,
    },
    {
        "feature_name": "rsi_14",
        "feature_type": "feature_type_momentum",
        "dataset_type": "dataset_fx_ohlcv",
        "output_field": "rsi_14",
        "value_type": "float",
        "lookback_window": 14,
        "required_input_fields": ["close"],
        "non_signal": True,
        "manual_review_required": False,
    },
    {
        "feature_name": "macd_line_placeholder",
        "feature_type": "feature_type_trend",
        "dataset_type": "dataset_fx_ohlcv",
        "output_field": "macd_line_placeholder",
        "value_type": "float",
        "lookback_window": 26,
        "required_input_fields": ["close"],
        "non_signal": True,
        "manual_review_required": False,
    },
    {
        "feature_name": "atr_14",
        "feature_type": "feature_type_volatility",
        "dataset_type": "dataset_fx_ohlcv",
        "output_field": "atr_14",
        "value_type": "float",
        "lookback_window": 14,
        "required_input_fields": ["high", "low", "close"],
        "non_signal": True,
        "manual_review_required": False,
    },
    {
        "feature_name": "bollinger_zscore_20",
        "feature_type": "feature_type_mean_reversion",
        "dataset_type": "dataset_fx_ohlcv",
        "output_field": "bollinger_zscore_20",
        "value_type": "float",
        "lookback_window": 20,
        "required_input_fields": ["close"],
        "non_signal": True,
        "manual_review_required": False,
    },
    {
        "feature_name": "donchian_position_20",
        "feature_type": "feature_type_trend",
        "dataset_type": "dataset_fx_ohlcv",
        "output_field": "donchian_position_20",
        "value_type": "float",
        "lookback_window": 20,
        "required_input_fields": ["high", "low", "close"],
        "non_signal": True,
        "manual_review_required": False,
    },
    {
        "feature_name": "quote_spread",
        "feature_type": "feature_type_quote",
        "dataset_type": "dataset_fx_quote",
        "output_field": "quote_spread",
        "value_type": "float",
        "lookback_window": None,
        "required_input_fields": ["bid", "ask"],
        "non_signal": True,
        "manual_review_required": False,
    },
    {
        "feature_name": "quote_mid",
        "feature_type": "feature_type_quote",
        "dataset_type": "dataset_fx_quote",
        "output_field": "quote_mid",
        "value_type": "float",
        "lookback_window": None,
        "required_input_fields": ["bid", "ask"],
        "non_signal": True,
        "manual_review_required": False,
    },
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
    },
    {
        "feature_name": "calendar_event_flag_placeholder",
        "feature_type": "feature_type_calendar",
        "dataset_type": "dataset_calendar_event",
        "output_field": "calendar_event_flag_placeholder",
        "value_type": "int",
        "lookback_window": None,
        "required_input_fields": ["timestamp", "event_id"],
        "non_signal": True,
        "manual_review_required": False,
    },
    {
        "feature_name": "news_topic_flag_placeholder",
        "feature_type": "feature_type_news_metadata",
        "dataset_type": "dataset_news_metadata",
        "output_field": "news_topic_flag_placeholder",
        "value_type": "int",
        "lookback_window": None,
        "required_input_fields": ["timestamp", "news_id"],
        "non_signal": True,
        "manual_review_required": False,
    },
]


def build_default_feature_schemas(
    profile: FeatureEngineProfile,
) -> List[FeatureSchema]:
    schemas: List[FeatureSchema] = []
    for item in DEFAULT_FEATURE_SCHEMAS:
        s = FeatureSchema(
            schema_id=build_feature_schema_id(item["feature_name"], item["dataset_type"]),
            feature_name=item["feature_name"],
            feature_type=item["feature_type"],
            dataset_type=item["dataset_type"],
            output_field=item["output_field"],
            value_type=item["value_type"],
            lookback_window=item["lookback_window"],
            required_input_fields=list(item["required_input_fields"]),
            non_signal=True,
            manual_review_required=item["manual_review_required"],
        )
        schemas.append(s)
    return schemas


def build_feature_schema_registry(
    profile: FeatureEngineProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    schemas = build_default_feature_schemas(profile)
    records = [s.to_dict() for s in schemas]
    df = pd.DataFrame.from_records(records)
    summary = summarize_feature_schema_registry(df)
    return df, summary


def summarize_feature_schema_registry(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_schemas": len(df),
        "feature_names": df["feature_name"].tolist() if not df.empty and "feature_name" in df.columns else [],
        "feature_types": df["feature_type"].unique().tolist() if not df.empty and "feature_type" in df.columns else [],
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty and "non_signal" in df.columns else True,
        "non_signal": True,
    }
