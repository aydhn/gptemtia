import pandas as pd
import pytest
from advanced_factor_metadata.factor_output_schema import (
    build_factor_output_schema_registry,
    validate_factor_output_schema,
)


def test_build_factor_output_schema_registry():
    df, summary = build_factor_output_schema_registry()
    assert not df.empty
    assert summary["total_schemas"] == 12
    assert summary["non_signal"] is True
    assert "schema_ref" in df.columns
    assert "standard_columns" in df.columns


def test_validate_factor_output_schema():
    valid_df = pd.DataFrame(
        {
            "timestamp": ["2026-01-01"],
            "symbol": ["USDTRY"],
            "factor_trend_multi_window_context": [0.5],
        }
    )
    res = validate_factor_output_schema(valid_df, ["factor_trend_multi_window_context"])
    assert res["is_valid"] is True
    assert len(res["prohibited_columns_found"]) == 0

    # Prohibited column
    invalid_df = pd.DataFrame(
        {
            "timestamp": ["2026-01-01"],
            "symbol": ["USDTRY"],
            "factor_trend_prediction": [0.5],
        }
    )
    res_inv = validate_factor_output_schema(invalid_df, ["factor_trend_prediction"])
    assert res_inv["is_valid"] is False
    assert len(res_inv["prohibited_columns_found"]) > 0
