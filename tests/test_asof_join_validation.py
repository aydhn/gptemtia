import pytest
from advanced_feature_validation.asof_join_validation import (
    validate_asof_join_direction,
    validate_asof_join_timestamps,
)
import pandas as pd


def test_asof_join_validation():
    res_bwd = validate_asof_join_direction("backward")
    assert res_bwd["is_valid"] is True

    res_fwd = validate_asof_join_direction("forward")
    assert res_fwd["is_valid"] is False

    res_nr = validate_asof_join_direction("nearest")
    assert res_nr["is_valid"] is False

    # Timestamps check
    base_ts = pd.to_datetime(["2024-01-02", "2024-01-03"])
    context_ts_valid = pd.to_datetime(["2024-01-01", "2024-01-02"])
    context_ts_future = pd.to_datetime(["2024-01-03", "2024-01-04"])

    res_ts_valid = validate_asof_join_timestamps(base_ts, context_ts_valid)
    assert res_ts_valid["is_valid"] is True

    res_ts_future = validate_asof_join_timestamps(base_ts, context_ts_future)
    assert res_ts_future["is_valid"] is False
