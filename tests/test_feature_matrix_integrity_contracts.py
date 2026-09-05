import pytest
import pandas as pd
from advanced_feature_validation.feature_matrix_integrity_contracts import (
    get_feature_matrix_integrity_contracts,
    validate_feature_matrix_integrity,
)


def test_feature_matrix_integrity_contracts():
    contracts = get_feature_matrix_integrity_contracts()
    assert len(contracts) >= 5

    clean_df = pd.DataFrame({
        "timestamp": pd.date_range("2024-01-01", periods=5),
        "feat_ret": [0.01, 0.02, -0.01, 0.005, 0.0],
    })
    res = validate_feature_matrix_integrity(clean_df, matrix_name="test_mat")
    assert res["is_valid"] is True
    assert res["current_phase"] == 121
    assert res["destructive_action_allowed"] is False
