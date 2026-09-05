import pytest
import pandas as pd
from advanced_feature_validation.feature_numeric_sanity_validation import validate_feature_numeric_sanity


def test_feature_numeric_sanity_validation():
    clean_df = pd.DataFrame({
        "timestamp": [1, 2],
        "feat_rsi": [50.0, 70.0],
        "feat_ret": [0.01, -0.02],
    })
    res_clean = validate_feature_numeric_sanity(clean_df)
    assert res_clean["is_valid"] is True

    # Extreme unrealistic outlier (e.g. 1e12 return)
    outlier_df = pd.DataFrame({
        "timestamp": [1, 2],
        "feat_ret": [0.01, 1e15],
    })
    res_outlier = validate_feature_numeric_sanity(outlier_df, abs_max_threshold=1e10)
    assert res_outlier["is_valid"] is False
    assert len(res_outlier["outlier_columns"]) > 0
