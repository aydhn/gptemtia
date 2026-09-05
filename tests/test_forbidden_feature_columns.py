import pytest
import pandas as pd
from advanced_feature_validation.forbidden_feature_columns import (
    FORBIDDEN_FEATURE_COLUMN_PATTERNS,
    get_forbidden_feature_columns,
    check_forbidden_feature_columns,
)


def test_forbidden_feature_columns_detection():
    forbidden = get_forbidden_feature_columns()
    assert "signal" in forbidden
    assert "buy" in forbidden
    assert "sell" in forbidden
    assert "target" in forbidden
    assert "full_text" in forbidden

    clean_df = pd.DataFrame({
        "timestamp": [1, 2],
        "feature_rsi": [50.0, 55.0],
        "feature_ret": [0.01, 0.02],
    })
    res_clean = check_forbidden_feature_columns(clean_df)
    assert res_clean["is_valid"] is True
    assert len(res_clean["forbidden_columns_found"]) == 0

    dirty_df = pd.DataFrame({
        "timestamp": [1, 2],
        "buy_signal": [1, 0],
        "forward_return": [0.05, 0.01],
        "article_body": ["abc", "def"],
    })
    res_dirty = check_forbidden_feature_columns(dirty_df)
    assert res_dirty["is_valid"] is False
    assert len(res_dirty["forbidden_columns_found"]) == 3
