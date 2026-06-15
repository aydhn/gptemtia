import pandas as pd
import pytest
from pathlib import Path
from artifact_metadata.artifact_inventory import (
    discover_research_artifacts, classify_research_artifact_type, infer_research_artifact_module
)
from artifact_metadata.metadata_config import get_default_artifact_metadata_profile

def test_classify_research_artifact_type():
    root = Path("/dummy")
    assert classify_research_artifact_type(root / "data/lake/ml/models/model.pkl", root) == "model_artifact"
    assert classify_research_artifact_type(root / "experiments/exp1.json", root) == "experiment_artifact"
    assert classify_research_artifact_type(root / "data/lake/raw/data.csv", root) == "dataset_artifact"

def test_infer_research_artifact_module():
    root = Path("/dummy")
    assert infer_research_artifact_module(root / "data/lake/ml/models.pkl", root) == "lake"
    assert infer_research_artifact_module(root / "experiments/exp1.json", root) == "experiments"

def test_discover_research_artifacts(tmp_path):
    root = tmp_path

    (root / "data" / "lake" / "ml" / "models").mkdir(parents=True)
    (root / "data" / "lake" / "ml" / "models" / "m1.pkl").touch()

    (root / "experiments").mkdir()
    (root / "experiments" / "exp1.json").touch()

    (root / "secrets").mkdir()
    (root / "secrets" / "key.txt").touch()

    profile = get_default_artifact_metadata_profile()
    df, summary = discover_research_artifacts(root, profile)

    assert len(df) >= 1
    types = df["artifact_type"].tolist()
    assert "model_artifact" in types


    paths = df["relative_path"].tolist()
    assert not any("secrets" in p for p in paths)
