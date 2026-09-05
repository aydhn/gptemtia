from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_technical_indicators.technical_indicator_config import TechnicalIndicatorProfile
from advanced_technical_indicators.technical_indicator_models import (
    IndicatorOutputSchema,
    build_indicator_output_schema_id,
)

FORBIDDEN_COLUMN_SUBSTRINGS = [
    "signal", "buy", "sell", "long", "short", "position",
    "target", "label", "prediction", "recommendation",
    "future_return", "forward_return", "next_return"
]

OUTPUT_SCHEMAS_DATA = [
    {"indicator": "high_low_range", "field": "high_low_range", "type": "float64", "nan_exp": False},
    {"indicator": "close_open_range", "field": "close_open_range", "type": "float64", "nan_exp": False},
    {"indicator": "range_pct", "field": "range_pct", "type": "float64", "nan_exp": False},
    {"indicator": "gap_from_prev_close", "field": "gap_from_prev_close", "type": "float64", "nan_exp": True},
    {"indicator": "close_location_value", "field": "close_location_value", "type": "float64", "nan_exp": False},
    {"indicator": "simple_return", "field": "simple_return_1", "type": "float64", "nan_exp": True},
    {"indicator": "log_return", "field": "log_return_1", "type": "float64", "nan_exp": True},
    {"indicator": "sma", "field": "sma_20", "type": "float64", "nan_exp": True},
    {"indicator": "ema", "field": "ema_20", "type": "float64", "nan_exp": False},
    {"indicator": "macd", "field": "macd_line", "type": "float64", "nan_exp": False},
    {"indicator": "macd", "field": "macd_smooth", "type": "float64", "nan_exp": False},
    {"indicator": "macd", "field": "macd_hist", "type": "float64", "nan_exp": False},
    {"indicator": "rsi", "field": "rsi_14", "type": "float64", "nan_exp": True},
    {"indicator": "stochastic", "field": "stoch_k_14", "type": "float64", "nan_exp": True},
    {"indicator": "stochastic", "field": "stoch_d_14_3", "type": "float64", "nan_exp": True},
    {"indicator": "true_range", "field": "true_range", "type": "float64", "nan_exp": True},
    {"indicator": "atr", "field": "atr_14", "type": "float64", "nan_exp": True},
    {"indicator": "bollinger_bands", "field": "bb_upper_20", "type": "float64", "nan_exp": True},
    {"indicator": "bollinger_bands", "field": "bb_mid_20", "type": "float64", "nan_exp": True},
    {"indicator": "bollinger_bands", "field": "bb_lower_20", "type": "float64", "nan_exp": True},
    {"indicator": "candle_body_size", "field": "candle_body_size", "type": "float64", "nan_exp": False},
    {"indicator": "quote_mid", "field": "quote_mid", "type": "float64", "nan_exp": False},
    {"indicator": "quote_spread", "field": "quote_spread", "type": "float64", "nan_exp": False},
    {"indicator": "rolling_zscore", "field": "rolling_zscore_20", "type": "float64", "nan_exp": True},
]


def validate_indicator_output_schema(df: pd.DataFrame, output_fields: List[str]) -> Dict[str, Any]:
    errors = []
    forbidden_found = []
    for f in output_fields:
        if f not in df.columns:
            errors.append(f"Expected output field '{f}' not found in dataframe.")
            continue
        fl = f.lower()
        for forbidden in FORBIDDEN_COLUMN_SUBSTRINGS:
            if forbidden in fl:
                forbidden_found.append(f"Field '{f}' contains forbidden substring '{forbidden}'.")
    return {
        "valid": len(errors) == 0 and len(forbidden_found) == 0,
        "missing_fields": errors,
        "forbidden_violations": forbidden_found,
    }


def build_indicator_output_schema_registry(
    profile: TechnicalIndicatorProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    items = []
    for s in OUTPUT_SCHEMAS_DATA:
        item = IndicatorOutputSchema(
            schema_id=build_indicator_output_schema_id(s["indicator"], s["field"]),
            indicator_name=s["indicator"],
            output_field=s["field"],
            value_type=s["type"],
            nullable=True,
            warmup_nan_expected=s["nan_exp"],
            non_signal=True,
            forbidden_aliases=FORBIDDEN_COLUMN_SUBSTRINGS,
            manual_review_required=False,
        )
        items.append(item.to_dict())

    df = pd.DataFrame(items)
    summary = {
        "total_schemas": len(df),
        "status": "READY",
        "forbidden_check_active": True,
        "current_phase": profile.current_phase,
    }
    return df, summary


def summarize_indicator_output_schema(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_schemas": len(df),
        "fields": list(df["output_field"].unique()) if not df.empty else [],
    }
