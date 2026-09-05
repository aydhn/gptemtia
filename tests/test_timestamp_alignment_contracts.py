"""Unit tests for Phase 119 timestamp alignment contracts and UTC normalization."""

import pytest
import pandas as pd
from advanced_cross_asset_alignment.timestamp_alignment_contracts import (
    normalize_alignment_timestamp_to_utc,
    validate_timestamp_alignment_fields,
    build_timestamp_alignment_contract_registry,
)


def test_utc_normalization():
    assert normalize_alignment_timestamp_to_utc("2026-09-03T12:00:00Z") == "2026-09-03T12:00:00Z"
    assert normalize_alignment_timestamp_to_utc("2026-09-03") == "2026-09-03T00:00:00Z"

    with pytest.raises(ValueError):
        normalize_alignment_timestamp_to_utc("invalid_date_format")


def test_validate_timestamp_fields():
    df = pd.DataFrame({
        "timestamp_utc": ["2026-09-01T00:00:00Z", "2026-09-02T00:00:00Z"],
        "price": [1.08, 1.09],
    })
    res = validate_timestamp_alignment_fields(df, ["timestamp_utc"])
    assert res["is_valid"] is True

    # Missing field
    res2 = validate_timestamp_alignment_fields(df, ["missing_col"])
    assert res2["is_valid"] is False


def test_build_timestamp_contract_registry():
    df, summary = build_timestamp_alignment_contract_registry()
    assert len(df) == 5
    assert summary["all_future_data_blocked"] is True
    assert summary["non_signal"] is True
    assert summary["status"] == "READY"
