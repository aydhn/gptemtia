import pytest
import pandas as pd
import numpy as np
from ml.preprocessing import BasicPreprocessor

def test_basic_preprocessor():
    df = pd.DataFrame({
        "num1": [1, np.nan, 3],
        "cat1": ["a", "b", np.nan],
        "target_val": [0, 1, 0],
        "high_nan": [1, np.nan, np.nan]
    })

    y = df["target_val"]

    prep = BasicPreprocessor(drop_high_nan_features=True, max_nan_ratio=0.5, enable_imputation=True, enable_scaling=False)
    X_trans = prep.fit_transform(df, y)

    assert "target_val" not in prep.get_feature_names()
    assert "high_nan" not in prep.get_feature_names()
    assert "num1" in prep.get_feature_names()

    # Imputation check
    assert not X_trans["num1"].isna().any()
    assert X_trans["num1"].iloc[1] == 2.0  # Median of 1 and 3

    # Categorical encoding check
    assert any(c.startswith("cat1_") for c in X_trans.columns)
