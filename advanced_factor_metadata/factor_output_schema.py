"""Phase 122 Factor Output Schema Registry.

Defines schemas for factor metadata and values, enforcing non-signal output
structures with zero prediction/label columns.
Strictly non-signal and research-only.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_factor_metadata.factor_metadata_config import (
    FactorMetadataProfile,
    get_default_factor_metadata_profile,
)
from advanced_factor_metadata.factor_metadata_labels import FACTOR_READY
from advanced_factor_metadata.factor_metadata_models import FORBIDDEN_FACTOR_TOKENS

SCHEMA_DEFINITIONS: List[Dict[str, Any]] = [
    {
        "schema_ref": "schema_factor_trend_float64",
        "factor_family": "trend",
        "value_dtype": "float64",
        "nullable": True,
        "standard_columns": ["timestamp", "symbol", "factor_trend_multi_window_context"],
        "description": "Continuous trend slope and channel position metric schema.",
    },
    {
        "schema_ref": "schema_factor_momentum_float64",
        "factor_family": "momentum",
        "value_dtype": "float64",
        "nullable": True,
        "standard_columns": ["timestamp", "symbol", "factor_momentum_rsi_roc_context"],
        "description": "Continuous normalized momentum velocity schema.",
    },
    {
        "schema_ref": "schema_factor_volatility_float64",
        "factor_family": "volatility",
        "value_dtype": "float64",
        "nullable": True,
        "standard_columns": ["timestamp", "symbol", "factor_volatility_atr_realized_context"],
        "description": "Continuous non-negative volatility dispersion metric schema.",
    },
    {
        "schema_ref": "schema_factor_mean_reversion_float64",
        "factor_family": "mean_reversion",
        "value_dtype": "float64",
        "nullable": True,
        "standard_columns": ["timestamp", "symbol", "factor_mean_reversion_zscore_context"],
        "description": "Standard score z-score distance-to-mean schema.",
    },
    {
        "schema_ref": "schema_factor_return_float64",
        "factor_family": "return",
        "value_dtype": "float64",
        "nullable": True,
        "standard_columns": ["timestamp", "symbol", "factor_return_multi_horizon_context"],
        "description": "Historical trailing returns metric schema.",
    },
    {
        "schema_ref": "schema_factor_quote_float64",
        "factor_family": "quote_microstructure",
        "value_dtype": "float64",
        "nullable": True,
        "standard_columns": ["timestamp", "symbol", "factor_quote_spread_context_placeholder"],
        "description": "Microstructure spread and order book hygiene placeholder schema.",
    },
    {
        "schema_ref": "schema_factor_macro_float64",
        "factor_family": "macro_context",
        "value_dtype": "float64",
        "nullable": True,
        "standard_columns": ["timestamp", "symbol", "factor_macro_inflation_rate_context"],
        "description": "Macroeconomic point-in-time rate schema.",
    },
    {
        "schema_ref": "schema_factor_event_float64",
        "factor_family": "calendar_event",
        "value_dtype": "float64",
        "nullable": True,
        "standard_columns": ["timestamp", "symbol", "factor_event_release_context"],
        "description": "Scheduled release proximity context schema.",
    },
    {
        "schema_ref": "schema_factor_news_float64",
        "factor_family": "news_attention",
        "value_dtype": "float64",
        "nullable": True,
        "standard_columns": ["timestamp", "symbol", "factor_news_attention_context"],
        "description": "Metadata-only entity frequency count schema.",
    },
    {
        "schema_ref": "schema_factor_cross_asset_float64",
        "factor_family": "cross_asset_context",
        "value_dtype": "float64",
        "nullable": True,
        "standard_columns": ["timestamp", "symbol", "factor_cross_asset_context"],
        "description": "Aligned multi-domain correlation observation schema.",
    },
    {
        "schema_ref": "schema_factor_regime_prep_float64",
        "factor_family": "regime_prep",
        "value_dtype": "float64",
        "nullable": True,
        "standard_columns": ["timestamp", "symbol", "factor_regime_prep_placeholder"],
        "description": "Candidate feature aggregate placeholder schema for Phase 126+.",
    },
    {
        "schema_ref": "schema_factor_composite_float64",
        "factor_family": "composite",
        "value_dtype": "float64",
        "nullable": True,
        "standard_columns": ["timestamp", "symbol", "factor_composite_context_placeholder"],
        "description": "Multi-family feature aggregation placeholder schema.",
    },
]


def build_factor_output_schema_registry(
    profile: FactorMetadataProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build Factor Output Schema Registry DataFrame and summary."""
    active_profile = profile or get_default_factor_metadata_profile()

    records: List[Dict[str, Any]] = []
    for s in SCHEMA_DEFINITIONS:
        records.append(
            {
                "schema_ref": s["schema_ref"],
                "factor_family": s["factor_family"],
                "value_dtype": s["value_dtype"],
                "nullable": s["nullable"],
                "column_count": len(s["standard_columns"]),
                "standard_columns": s["standard_columns"],
                "description": s["description"],
                "non_signal": True,
                "status_label": FACTOR_READY,
            }
        )

    df = pd.DataFrame(records)
    summary = {
        "active_profile": active_profile.name,
        "total_schemas": len(records),
        "current_phase": active_profile.current_phase,
        "target_final_phase": active_profile.target_final_phase,
        "non_signal": True,
        "status": FACTOR_READY,
    }
    return df, summary


def validate_factor_output_schema(df: pd.DataFrame, output_fields: List[str]) -> Dict[str, Any]:
    """Validate that output dataframe contains zero prohibited columns."""
    prohibited_found: List[str] = []

    for col in df.columns:
        col_lower = str(col).lower()
        for token in FORBIDDEN_FACTOR_TOKENS:
            if token in col_lower:
                prohibited_found.append(str(col))

    missing_fields = [f for f in output_fields if f not in df.columns]
    is_valid = len(prohibited_found) == 0 and len(missing_fields) == 0

    return {
        "is_valid": is_valid,
        "prohibited_columns_found": prohibited_found,
        "missing_required_fields": missing_fields,
        "column_count": len(df.columns),
        "non_signal": len(prohibited_found) == 0,
    }


def summarize_factor_output_schema(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize factor output schema registry DataFrame."""
    return {
        "total_schemas": len(df),
        "families_covered": int(df["factor_family"].nunique()) if "factor_family" in df else 0,
        "status": FACTOR_READY,
    }
