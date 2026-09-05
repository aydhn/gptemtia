import pandas as pd
from advanced_regime_matrix.regime_matrix_schema import (
    MINIMUM_REGIME_MATRIX_COLUMNS,
    REGIME_MATRIX_MINIMUM_COLUMNS,
    build_regime_matrix_schema,
    build_regime_matrix_schema_registry,
    validate_regime_matrix_schema,
)


def test_build_regime_matrix_schema():
    df, s = build_regime_matrix_schema()
    assert len(df) == 16
    assert s["total_schema_fields"] == 16
    assert s["all_non_signal"] is True
    assert "entity_id" in df["column_name"].values
    assert "timestamp_utc" in df["column_name"].values
    assert "symbol" in df["column_name"].values


def test_validate_regime_matrix_schema():
    valid_data = {col: [1] for col in MINIMUM_REGIME_MATRIX_COLUMNS}
    valid_df = pd.DataFrame(valid_data)
    res = validate_regime_matrix_schema(valid_df)
    assert res["is_valid"] is True
    assert len(res["missing_columns"]) == 0
    assert len(res["forbidden_columns_found"]) == 0

    invalid_df = pd.DataFrame({"col_a": [1], "col_b": [2]})
    res_inv = validate_regime_matrix_schema(invalid_df)
    assert res_inv["is_valid"] is False
    assert len(res_inv["missing_columns"]) > 0
