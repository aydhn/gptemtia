import pytest
import pandas as pd
from advanced_feature_validation.macro_release_lag_validation import (
    validate_macro_release_lag,
    get_macro_release_lag_policy,
)


def test_macro_release_lag_validation():
    policy = get_macro_release_lag_policy("cpi")
    assert policy["lag_days"] >= 1

    df_valid = pd.DataFrame({
        "timestamp": pd.to_datetime(["2024-02-15"]),
        "reference_period": pd.to_datetime(["2024-01-31"]),
    })
    res_valid = validate_macro_release_lag(df_valid)
    assert res_valid["is_valid"] is True

    df_invalid = pd.DataFrame({
        "timestamp": pd.to_datetime(["2024-01-15"]),
        "reference_period": pd.to_datetime(["2024-01-31"]),
    })
    res_invalid = validate_macro_release_lag(df_invalid)
    assert res_invalid["is_valid"] is False
