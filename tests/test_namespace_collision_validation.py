import pytest
import pandas as pd
from advanced_feature_validation.namespace_collision_validation import validate_namespace_collisions


def test_namespace_collision_validation():
    clean_df = pd.DataFrame({
        "timestamp": [1, 2],
        "fx_eurusd_ret": [0.01, -0.02],
        "com_brent_ret": [0.02, 0.01],
    })
    res_clean = validate_namespace_collisions(clean_df)
    assert res_clean["is_valid"] is True
    assert res_clean["collision_count"] == 0

    # Ambiguous collision: e.g., stripped/case insensitive match or un-namespaced duplicate base
    collision_df = pd.DataFrame({
        "timestamp": [1, 2],
        "ret": [0.01, 0.02],
        "RET": [0.01, 0.02],
    })
    res_col = validate_namespace_collisions(collision_df)
    assert res_col["is_valid"] is False
    assert res_col["collision_count"] > 0
