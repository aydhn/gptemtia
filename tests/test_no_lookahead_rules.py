import pytest
import pandas as pd
from advanced_feature_validation.no_lookahead_rules import (
    get_no_lookahead_rules,
    check_no_lookahead_rules,
)


def test_no_lookahead_rules():
    rules = get_no_lookahead_rules()
    assert len(rules) >= 5

    clean_df = pd.DataFrame({
        "timestamp": pd.date_range("2024-01-01", periods=5),
        "feat_lag_1": [1, 2, 3, 4, 5],
    })
    res_clean = check_no_lookahead_rules(clean_df)
    assert res_clean["is_valid"] is True

    dirty_df = pd.DataFrame({
        "timestamp": pd.date_range("2024-01-01", periods=5),
        "feat_lead_1": [2, 3, 4, 5, 6],
        "future_ret": [0.01, 0.02, 0.03, 0.04, 0.05],
    })
    res_dirty = check_no_lookahead_rules(dirty_df)
    assert res_dirty["is_valid"] is False
    assert len(res_dirty["violations"]) >= 1
