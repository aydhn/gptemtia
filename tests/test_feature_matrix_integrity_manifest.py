import pytest
import pandas as pd
from advanced_feature_validation.feature_matrix_integrity_manifest import create_feature_matrix_integrity_manifest


def test_feature_matrix_integrity_manifest():
    df = pd.DataFrame({
        "timestamp": pd.date_range("2024-01-01", periods=10),
        "feat_a": range(10),
        "feat_b": [x * 0.1 for x in range(10)],
    })
    manifest = create_feature_matrix_integrity_manifest(df, matrix_name="matrix_manifest_test")
    assert manifest["matrix_name"] == "matrix_manifest_test"
    assert manifest["total_rows"] == 10
    assert manifest["total_columns"] == 3
    assert manifest["current_phase"] == 121
    assert "checksum" in manifest
