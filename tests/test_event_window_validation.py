import pytest
import pandas as pd
from advanced_feature_validation.event_window_validation import (
    validate_event_window_timestamps,
    check_event_window_leakage,
)


def test_event_window_validation():
    # Pre-event and post-event feature logic
    df_valid = pd.DataFrame({
        "timestamp": pd.to_datetime(["2024-01-01", "2024-01-02"]),
        "event_time": pd.to_datetime(["2024-01-01", "2024-01-01"]),
        "feature_event_passed": [0, 1],
    })
    res_valid = validate_event_window_timestamps(df_valid)
    assert res_valid["is_valid"] is True

    # Post-outcome leaked before event time
    df_leak = pd.DataFrame({
        "timestamp": pd.to_datetime(["2024-01-01 08:00"]),
        "event_time": pd.to_datetime(["2024-01-01 14:00"]),
        "actual_value": [3.5],  # Actual released at 14:00 but present at 08:00
    })
    res_leak = check_event_window_leakage(df_leak)
    assert res_leak["is_valid"] is False
