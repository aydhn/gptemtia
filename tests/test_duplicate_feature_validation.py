import pytest
import pandas as pd
from advanced_feature_validation.duplicate_feature_validation import validate_duplicate_feature_columns


def test_duplicate_feature_validation():
    clean_df = pd.DataFrame({
        "timestamp": [1, 2],
        "feat_a": [10, 20],
        "feat_b": [30, 40],
    })
    res_clean = validate_duplicate_feature_columns(clean_df)
    assert res_clean["is_valid"] is True
    assert res_clean["duplicate_columns_count"] == 0

    # Duplicate column names
    dup_df = pd.DataFrame([[1, 10, 20]], columns=["timestamp", "feat_a", "feat_a"])
    res_dup = validate_duplicate_feature_columns(dup_df)
    assert res_dup["is_valid"] is False
    assert res_dup["duplicate_columns_count"] > 0
    assert res_dup["destructive_action_allowed"] is False
