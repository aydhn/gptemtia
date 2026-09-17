"""Test suite for Phase 137 ML Dataset Schema Policies."""

import pytest
import pandas as pd
from advanced_ml_dataset_registry.ml_dataset_schema import (
    build_ml_dataset_schema_registry,
    validate_ml_dataset_schema,
    summarize_ml_dataset_schema,
)


def test_build_schema_registry():
    df, summary = build_ml_dataset_schema_registry()
    assert not df.empty
    assert summary["total_schemas"] >= 8
    assert summary["forbidden_columns_enforced"] is True
    assert summary["timestamp_utc_required"] is True


def test_validate_schema():
    good_df = pd.DataFrame(columns=["dataset_contract_key", "timestamp_utc"])
    res = validate_ml_dataset_schema(good_df, ["dataset_contract_key", "timestamp_utc"])
    assert res["valid"] is True

    bad_df = pd.DataFrame(columns=["signal", "timestamp_utc"])
    res_bad = validate_ml_dataset_schema(bad_df, ["timestamp_utc"])
    assert res_bad["valid"] is False
