import pytest
from pathlib import Path
import pandas as pd
from evidence_governance.evidence_config import get_default_evidence_governance_profile
from evidence_governance.artifact_inventory import (
    discover_evidence_artifacts,
    classify_evidence_artifact,
    infer_evidence_module,
    calculate_evidence_hash
)

def test_discover_evidence_artifacts(tmp_path):
    # Setup mock structure
    reports_dir = tmp_path / "reports" / "output"
    reports_dir.mkdir(parents=True)
    f1 = reports_dir / "test_report.csv"
    f1.write_text("dummy")

    docs_dir = tmp_path / "docs"
    docs_dir.mkdir(parents=True)
    f2 = docs_dir / "TEST.md"
    f2.write_text("docs")

    profile = get_default_evidence_governance_profile()
    df, summary = discover_evidence_artifacts(tmp_path, profile)

    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert "artifact_id" in df.columns

def test_classify_evidence_artifact(tmp_path):
    p1 = tmp_path / "reports" / "output" / "some_report.csv"
    label = classify_evidence_artifact(p1, tmp_path)
    assert label == "report_evidence"

def test_infer_evidence_module(tmp_path):
    p1 = tmp_path / "reports" / "output" / "safety" / "file.csv"
    mod = infer_evidence_module(p1, tmp_path)
    assert mod == "safety"

def test_calculate_evidence_hash_skip_large(tmp_path, monkeypatch):
    import os
    profile = get_default_evidence_governance_profile()

    # Mock max size to very small
    class MockProfile:
        max_artifact_mb = 0 # 0 mb limit

    p1 = tmp_path / "test.txt"
    p1.write_text("hello")

    hash_val, info = calculate_evidence_hash(p1, MockProfile())
    assert hash_val is None
    assert "warning" in info
