import pytest
import pandas as pd
from advanced_feature_validation.non_signal_feature_validation import (
    validate_non_signal_invariants,
    check_signal_like_columns,
)


def test_non_signal_feature_validation():
    clean_df = pd.DataFrame({
        "timestamp": [1, 2],
        "feature_ret": [0.01, 0.02],
    })
    res_clean = validate_non_signal_invariants(clean_df)
    assert res_clean["is_valid"] is True
    assert res_clean["non_signal"] is True

    signal_df = pd.DataFrame({
        "timestamp": [1, 2],
        "buy_signal": [1, 0],
        "recommendation": ["BUY", "HOLD"],
    })
    res_sig = check_signal_like_columns(signal_df)
    assert res_sig["is_valid"] is False
    assert len(res_sig["signal_columns_detected"]) >= 2
