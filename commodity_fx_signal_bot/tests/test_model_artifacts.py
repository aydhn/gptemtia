import pytest
from pathlib import Path
from ml.model_artifacts import build_model_artifact_bundle

def test_build_model_artifact_bundle():
    bundle = build_model_artifact_bundle(
        model_id="test_id",
        model_family="dummy",
        task_type="classification",
        target_column="target",
        model_path="path/to/model",
        preprocessor_path="path/to/prep",
        metadata_path="path/to/meta",
        feature_schema_path="path/to/fs",
        target_schema_path="path/to/ts"
    )

    assert bundle.model_id == "test_id"
    assert bundle.model_path == "path/to/model"
