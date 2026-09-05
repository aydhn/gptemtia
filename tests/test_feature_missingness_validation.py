import pytest
import pandas as pd
import numpy as np
from advanced_feature_validation.feature_missingness_validation import validate_feature_missingness


def test_feature_missingness_validation():
    clean_df = pd.DataFrame({
        "timestamp": [1, 2, 3, 4, 5],
        "feat_a": [1.0, 2.0, 3.0, 4.0, 5.0],
        "feat_b": [np.nan, 2.0, 3.0, 4.0, 5.0],  # 20% missing
    })
    res_clean = validate_feature_missingness(clean_df, max_missingness_ratio=0.35)
    assert res_clean["is_valid"] is True

    high_missing_df = pd.DataFrame({
        "timestamp": [1, 2, 3, 4, 5],
        "feat_a": [np.nan, np.nan, np.nan, np.nan, 5.0],  # 80% missing
    })
    res_high = validate_feature_missingness(high_missing_df, max_missingness_ratio=0.35)
    assert res_high["is_valid"] is False
    assert len(res_high["excessive_missing_columns"]) > 0
    assert res_high["destructive_action_allowed"] is False
