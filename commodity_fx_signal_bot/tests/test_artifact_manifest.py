import pytest
from pathlib import Path
from experiments.artifact_manifest import (
    hash_file,
    build_artifact_record,
    discover_experiment_artifacts,
    build_experiment_artifact_manifest,
    validate_artifact_manifest,
    artifact_manifest_to_dataframe
)

def test_hash_file(tmp_path):
    f = tmp_path / "test.txt"
    f.write_text("hello world")
    h = hash_file(f)
    assert h is not None

    missing = hash_file(tmp_path / "missing.txt")
    assert missing is None

def test_build_artifact_record(tmp_path):
    f = tmp_path / "test2.txt"
    f.write_text("test")
    rec = build_artifact_record(f, "data", required=True)
    assert rec["exists"] is True
    assert rec["artifact_type"] == "data"
    assert rec["hash"] is not None

def test_discover_artifacts():
    class MockDataLake:
        pass

    artifacts = discover_experiment_artifacts(MockDataLake(), ["meta_research"], "1d")
    assert len(artifacts) > 0
    assert any(a["artifact_type"] == "meta" for a in artifacts)

def test_manifest_functions():
    artifacts = [
        {"artifact_type": "meta", "path": "test", "exists": False, "hash": None, "required": True}
    ]
    manifest = build_experiment_artifact_manifest("run_1", artifacts)
    assert manifest["total_artifacts"] == 1
    assert "meta" in manifest["missing_required"]

    val = validate_artifact_manifest(manifest)
    assert val["valid"] is False
    assert len(val["warnings"]) > 0

    df = artifact_manifest_to_dataframe(manifest)
    assert len(df) == 1
    assert "run_id" in df.columns
