from typing import Tuple, Dict, Any, List
import pandas as pd
import numpy as np

from advanced_feature_grid.feature_grid_config import FeatureGridProfile, get_default_feature_grid_profile
from advanced_feature_grid.feature_grid_models import (
    FeatureGridOutputSchema,
    build_feature_grid_output_schema_id,
    FORBIDDEN_OUTPUT_WORDS,
)


SCHEMA_CATALOG = [
    {
        "grid_name": "moving_average_grid",
        "output_field_pattern": "{ma_type}_w{window}",
        "value_type": "float64",
        "nullable": True,
        "warmup_nan_expected": True,
    },
    {
        "grid_name": "momentum_grid",
        "output_field_pattern": "{momentum_type}_w{window}",
        "value_type": "float64",
        "nullable": True,
        "warmup_nan_expected": True,
    },
    {
        "grid_name": "volatility_grid",
        "output_field_pattern": "{vol_type}_w{window}",
        "value_type": "float64",
        "nullable": True,
        "warmup_nan_expected": True,
    },
    {
        "grid_name": "range_channel_grid",
        "output_field_pattern": "{channel_type}_{part}_w{window}",
        "value_type": "float64",
        "nullable": True,
        "warmup_nan_expected": True,
    },
    {
        "grid_name": "mean_reversion_grid",
        "output_field_pattern": "{mr_type}_w{window}",
        "value_type": "float64",
        "nullable": True,
        "warmup_nan_expected": True,
    },
    {
        "grid_name": "return_grid",
        "output_field_pattern": "return_w{window}",
        "value_type": "float64",
        "nullable": True,
        "warmup_nan_expected": True,
    },
]


def build_feature_grid_output_schema_registry(
    profile: FeatureGridProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_feature_grid_profile()
    rows = []

    for item in SCHEMA_CATALOG:
        schema = FeatureGridOutputSchema(
            schema_id=build_feature_grid_output_schema_id(item["grid_name"], item["output_field_pattern"]),
            grid_name=item["grid_name"],
            output_field_pattern=item["output_field_pattern"],
            value_type=item["value_type"],
            nullable=item["nullable"],
            warmup_nan_expected=item["warmup_nan_expected"],
            forbidden_aliases=list(FORBIDDEN_OUTPUT_WORDS),
            non_signal=True,
            manual_review_required=False,
        )
        rows.append(schema.to_dict())

    df = pd.DataFrame(rows)
    summary = summarize_feature_grid_output_schema(df)
    summary["profile"] = active_profile.name
    return df, summary


def validate_feature_grid_output_schema(
    df: pd.DataFrame, output_fields: List[str]
) -> Dict[str, Any]:
    errors = []
    warnings = []

    for col in output_fields:
        if col not in df.columns:
            errors.append(f"Beklenen çıktı kolonu bulunamadı: {col}")
            continue

        series = df[col]
        # Check numeric type
        if not np.issubdtype(series.dtype, np.number):
            errors.append(f"Kolon {col} sayısal (numeric) değil: {series.dtype}")

        # Check for forbidden aliases
        col_lower = col.lower()
        for forbidden in FORBIDDEN_OUTPUT_WORDS:
            if forbidden in col_lower:
                errors.append(f"Kolon {col} yasaklı sinyal/hedef kelimesi içeriyor: {forbidden}")

    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "warnings": warnings,
        "fields_validated": len(output_fields),
    }


def summarize_feature_grid_output_schema(df: pd.DataFrame) -> Dict[str, Any]:
    if df.empty:
        return {"total_schemas": 0, "status": "EMPTY"}

    return {
        "total_schemas": len(df),
        "all_numeric": True,
        "all_nullable": True,
        "warmup_nan_expected": True,
        "status": "READY",
    }
