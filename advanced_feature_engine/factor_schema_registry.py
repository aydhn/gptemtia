from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_feature_engine.feature_engine_config import FeatureEngineProfile
from advanced_feature_engine.feature_engine_models import (
    FactorSchema,
    build_factor_schema_id,
)

DEFAULT_FACTOR_SCHEMAS: List[Dict[str, Any]] = [
    {
        "factor_name": "trend_factor_placeholder",
        "factor_type": "trend_factor",
        "description": "Trend gücü araştırma faktörü placeholder'ı; sinyal içermez.",
        "required_features": ["sma_20", "ema_20", "donchian_position_20"],
        "output_field": "trend_factor_placeholder",
        "non_signal": True,
        "future_phase_owner": "Phase 122",
        "manual_review_required": False,
    },
    {
        "factor_name": "momentum_factor_placeholder",
        "factor_type": "momentum_factor",
        "description": "Momentum araştırma faktörü placeholder'ı; sinyal içermez.",
        "required_features": ["rsi_14", "close_return_5"],
        "output_field": "momentum_factor_placeholder",
        "non_signal": True,
        "future_phase_owner": "Phase 122",
        "manual_review_required": False,
    },
    {
        "factor_name": "volatility_factor_placeholder",
        "factor_type": "volatility_factor",
        "description": "Volatilite risk faktörü placeholder'ı; sinyal içermez.",
        "required_features": ["rolling_std_20", "atr_14"],
        "output_field": "volatility_factor_placeholder",
        "non_signal": True,
        "future_phase_owner": "Phase 122",
        "manual_review_required": False,
    },
    {
        "factor_name": "mean_reversion_factor_placeholder",
        "factor_type": "mean_reversion_factor",
        "description": "Ortalamaya dönüş mesafe faktörü placeholder'ı; sinyal içermez.",
        "required_features": ["bollinger_zscore_20"],
        "output_field": "mean_reversion_factor_placeholder",
        "non_signal": True,
        "future_phase_owner": "Phase 122",
        "manual_review_required": False,
    },
    {
        "factor_name": "macro_pressure_factor_placeholder",
        "factor_type": "macro_factor",
        "description": "Makroekonomik baskı araştırma faktörü placeholder'ı; sinyal içermez.",
        "required_features": ["macro_value_change"],
        "output_field": "macro_pressure_factor_placeholder",
        "non_signal": True,
        "future_phase_owner": "Phase 122",
        "manual_review_required": False,
    },
    {
        "factor_name": "event_risk_factor_placeholder",
        "factor_type": "event_factor",
        "description": "Takvim olay riski araştırma faktörü placeholder'ı; sinyal içermez.",
        "required_features": ["calendar_event_flag_placeholder"],
        "output_field": "event_risk_factor_placeholder",
        "non_signal": True,
        "future_phase_owner": "Phase 122",
        "manual_review_required": False,
    },
    {
        "factor_name": "news_attention_factor_placeholder",
        "factor_type": "attention_factor",
        "description": "Haber dikkat ve konu yoğunluğu faktörü placeholder'ı; sinyal içermez.",
        "required_features": ["news_topic_flag_placeholder"],
        "output_field": "news_attention_factor_placeholder",
        "non_signal": True,
        "future_phase_owner": "Phase 122",
        "manual_review_required": False,
    },
    {
        "factor_name": "cross_asset_context_factor_placeholder",
        "factor_type": "cross_asset_factor",
        "description": "Çapraz varlık korelasyon ve makro rejim faktörü placeholder'ı; sinyal içermez.",
        "required_features": ["close_return_1", "macro_value_change"],
        "output_field": "cross_asset_context_factor_placeholder",
        "non_signal": True,
        "future_phase_owner": "Phase 122",
        "manual_review_required": False,
    },
]


def build_default_factor_schemas(
    profile: FeatureEngineProfile,
) -> List[FactorSchema]:
    schemas: List[FactorSchema] = []
    for item in DEFAULT_FACTOR_SCHEMAS:
        s = FactorSchema(
            factor_id=build_factor_schema_id(item["factor_name"]),
            factor_name=item["factor_name"],
            factor_type=item["factor_type"],
            description=item["description"],
            required_features=list(item["required_features"]),
            output_field=item["output_field"],
            non_signal=True,
            future_phase_owner=item["future_phase_owner"],
            manual_review_required=item["manual_review_required"],
        )
        schemas.append(s)
    return schemas


def build_factor_schema_registry(
    profile: FeatureEngineProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    schemas = build_default_factor_schemas(profile)
    records = [s.to_dict() for s in schemas]
    df = pd.DataFrame.from_records(records)
    summary = summarize_factor_schema_registry(df)
    return df, summary


def summarize_factor_schema_registry(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_factor_schemas": len(df),
        "factor_names": df["factor_name"].tolist() if not df.empty and "factor_name" in df.columns else [],
        "factor_types": df["factor_type"].unique().tolist() if not df.empty and "factor_type" in df.columns else [],
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty and "non_signal" in df.columns else True,
        "non_signal": True,
    }
