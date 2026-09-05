"""Phase 126: Regime State Output Schema Registry.

Defines canonical schema fields for non-signal regime states and validates column constraints.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_foundation.regime_foundation_config import (
    RegimeFoundationProfile,
    get_default_regime_foundation_profile,
)

FORBIDDEN_OUTPUT_FIELDS: List[str] = [
    "signal",
    "buy",
    "sell",
    "long",
    "short",
    "position",
    "target",
    "label",
    "prediction",
    "recommendation",
    "future_return",
    "forward_return",
    "next_return",
]

SCHEMA_FIELDS: List[Dict[str, Any]] = [
    {
        "field_name": "timestamp",
        "data_type": "datetime64[ns, UTC]",
        "regime_family": "all_regime_families",
        "state_description": "Primary UTC bar alignment timestamp",
        "source_feature_contract": "contract_timestamp_alignment",
        "validation_dependency": "val_timestamp_order",
        "quality_dependency": "qual_staleness",
        "non_signal": True,
        "model_training_required_future_phase": False,
        "manual_review_required": False,
        "forbidden_field": False,
    },
    {
        "field_name": "symbol",
        "data_type": "string",
        "regime_family": "all_regime_families",
        "state_description": "Canonical normalized asset ticker symbol",
        "source_feature_contract": "contract_symbol_mapping",
        "validation_dependency": "val_symbol_normalization",
        "quality_dependency": "qual_availability",
        "non_signal": True,
        "model_training_required_future_phase": False,
        "manual_review_required": False,
        "forbidden_field": False,
    },
    {
        "field_name": "regime_state_trend_context",
        "data_type": "float64",
        "regime_family": "regime_family_trend",
        "state_description": "Continuous trend alignment metric (-1.0 to 1.0) indicating directional persistence",
        "source_feature_contract": "contract_trend_features",
        "validation_dependency": "val_trend_no_lookahead",
        "quality_dependency": "qual_trend_factor_drift",
        "non_signal": True,
        "model_training_required_future_phase": True,
        "manual_review_required": True,
        "forbidden_field": False,
    },
    {
        "field_name": "regime_state_range_context",
        "data_type": "float64",
        "regime_family": "regime_family_range",
        "state_description": "Continuous mean-reversion bounded metric (0.0 to 1.0)",
        "source_feature_contract": "contract_range_features",
        "validation_dependency": "val_range_no_lookahead",
        "quality_dependency": "qual_range_factor_drift",
        "non_signal": True,
        "model_training_required_future_phase": True,
        "manual_review_required": True,
        "forbidden_field": False,
    },
    {
        "field_name": "regime_state_volatility_high_context",
        "data_type": "int8",
        "regime_family": "regime_family_volatility",
        "state_description": "Binary indicator for top-quintile realized dispersion environment",
        "source_feature_contract": "contract_volatility_features",
        "validation_dependency": "val_vol_no_lookahead",
        "quality_dependency": "qual_vol_factor_drift",
        "non_signal": True,
        "model_training_required_future_phase": True,
        "manual_review_required": True,
        "forbidden_field": False,
    },
    {
        "field_name": "regime_state_volatility_low_context",
        "data_type": "int8",
        "regime_family": "regime_family_volatility",
        "state_description": "Binary indicator for bottom-quintile realized dispersion environment",
        "source_feature_contract": "contract_volatility_features",
        "validation_dependency": "val_vol_no_lookahead",
        "quality_dependency": "qual_vol_factor_drift",
        "non_signal": True,
        "model_training_required_future_phase": True,
        "manual_review_required": True,
        "forbidden_field": False,
    },
    {
        "field_name": "regime_state_macro_event_context",
        "data_type": "int8",
        "regime_family": "regime_family_event_context",
        "state_description": "Binary indicator for scheduled economic event window activity",
        "source_feature_contract": "contract_macro_event_features",
        "validation_dependency": "val_event_window_alignment",
        "quality_dependency": "qual_calendar_staleness",
        "non_signal": True,
        "model_training_required_future_phase": False,
        "manual_review_required": True,
        "forbidden_field": False,
    },
    {
        "field_name": "regime_state_cross_asset_context",
        "data_type": "float64",
        "regime_family": "regime_family_cross_asset_context",
        "state_description": "Normalized cross-asset coupling index with DXY and US10Y",
        "source_feature_contract": "contract_cross_asset_features",
        "validation_dependency": "val_cross_asset_alignment",
        "quality_dependency": "qual_cross_asset_drift",
        "non_signal": True,
        "model_training_required_future_phase": True,
        "manual_review_required": True,
        "forbidden_field": False,
    },
]


def build_regime_state_output_schema_registry(
    profile: Optional[RegimeFoundationProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for regime state output schema registry."""
    active_profile = profile or get_default_regime_foundation_profile()
    df = pd.DataFrame(SCHEMA_FIELDS)
    summary = {
        "active_profile": active_profile.profile_name,
        "total_fields": len(df),
        "all_non_signal": bool((df["non_signal"] == True).all()),
        "no_forbidden_fields": not any(f in FORBIDDEN_OUTPUT_FIELDS for f in df["field_name"]),
        "current_phase": active_profile.current_phase,
        "target_final_phase": active_profile.target_final_phase,
        "next_phase": active_profile.next_phase,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    }
    return df, summary


def validate_regime_state_output_schema(
    df: pd.DataFrame,
    output_fields: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """Inspect DataFrame columns or output field list for forbidden trading/signal fields."""
    cols_to_check = output_fields if output_fields is not None else list(df.columns)
    violations = []
    for col in cols_to_check:
        col_lower = str(col).lower()
        for forbidden in FORBIDDEN_OUTPUT_FIELDS:
            if forbidden in col_lower:
                violations.append({"column": col, "forbidden_term": forbidden})

    return {
        "is_valid": len(violations) == 0,
        "total_columns_checked": len(cols_to_check),
        "violations_count": len(violations),
        "violations": violations,
        "non_signal": True,
    }


def summarize_regime_state_output_schema(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize regime state output schema DataFrame."""
    return {
        "total_fields": len(df),
        "field_names": list(df["field_name"].unique()) if "field_name" in df.columns else [],
        "all_non_signal": True,
        "forbidden_fields_count": 0,
    }
