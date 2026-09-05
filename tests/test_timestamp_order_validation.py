import pytest
import pandas as pd
from advanced_feature_validation.timestamp_order_validation import validate_timestamp_order


def test_timestamp_order_validation():
    ordered_df = pd.DataFrame({
        "timestamp": pd.to_datetime(["2024-01-01", "2024-01-02", "2024-01-03"]),
        "value": [1, 2, 3],
    })
    res_ordered = validate_timestamp_order(ordered_df)
    assert res_ordered["is_valid"] is True
    assert res_ordered["monotonic_increasing"] is True

    unordered_df = pd.DataFrame({
        "timestamp": pd.to_datetime(["2024-01-03", "2024-01-01", "2024-01-02"]),
        "value": [1, 2, 3],
    })
    res_unordered = validate_timestamp_order(unordered_df)
    assert res_unordered["is_valid"] is False
