import pytest
import pandas as pd
import numpy as np
from advanced_feature_validation.feature_infinite_value_validation import validate_feature_infinite_values


def test_feature_infinite_value_validation():
    clean_df = pd.DataFrame({
        "timestamp": [1, 2],
        "feat_a": [1.0, 2.0],
    })
    res_clean = validate_feature_infinite_values(clean_df)
    assert res_clean["is_valid"] is True
    assert res_clean["infinite_count"] == 0

    inf_df = pd.DataFrame({
        "timestamp": [1, 2],
        "feat_a": [1.0, np.inf],
        "feat_b": [-np.inf, 2.0],
    })
    res_inf = validate_feature_infinite_values(inf_df)
    assert res_inf["is_valid"] is False
    assert res_inf["infinite_count"] == 2
    assert res_inf["destructive_action_allowed"] is False
