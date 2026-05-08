import pytest
import pandas as pd
from ml.model_schema import infer_feature_schema, infer_target_schema, validate_feature_target_schema

def test_infer_feature_schema():
    df = pd.DataFrame({
        "num1": [1, 2, 3],
        "num2": [1.1, 2.2, 3.3],
        "cat1": ["a", "b", "a"]
    })
    schema = infer_feature_schema(df)
    assert len(schema.numeric_columns) == 2
    assert len(schema.categorical_columns) == 1
    assert schema.feature_count == 3

def test_infer_target_schema():
    y = pd.Series([0, 1, 0, 1, 1], name="target")
    schema = infer_target_schema(y, "classification", "target")
    assert schema.target_column == "target"
    assert "1" in schema.class_labels
    assert schema.missing_ratio == 0.0

def test_validate_feature_target_schema():
    X = pd.DataFrame({"target": [1, 2], "feat": [3, 4]})
    y = pd.Series([1, 2], name="target")
    res = validate_feature_target_schema(X, y, "classification")
    assert not res["passed"]
    assert any("found in feature matrix" in w for w in res["warnings"])
