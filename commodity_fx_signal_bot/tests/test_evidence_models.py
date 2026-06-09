import pytest
from evidence_governance.evidence_models import (
    build_evidence_artifact_id,
    build_policy_id,
    build_control_id,
    build_control_evidence_mapping_id,
    build_evidence_gap_id,
    EvidenceArtifact,
    evidence_artifact_to_dict
)

def test_build_evidence_artifact_id():
    id1 = build_evidence_artifact_id("path/to/file.txt")
    id2 = build_evidence_artifact_id("path/to/file.txt")
    assert id1 == id2
    assert id1.startswith("art_")

def test_build_policy_id():
    id1 = build_policy_id("name", "domain")
    assert id1.startswith("pol_")

def test_build_control_id():
    id1 = build_control_id("name", "domain")
    assert id1.startswith("ctl_")

def test_build_control_evidence_mapping_id():
    id1 = build_control_evidence_mapping_id("c1", "a1")
    assert id1.startswith("map_")

def test_dataclass_to_dict():
    art = EvidenceArtifact(
        artifact_id="a1",
        relative_path="a/b",
        artifact_label="report_evidence",
        module_name="test",
        evidence_title="Test",
        evidence_summary="Summary",
        created_or_modified_at_utc="2023-01-01T00:00:00",
        content_hash="hash",
        size_bytes=100,
        freshness_label="evidence_fresh",
        warnings=[]
    )
    d = evidence_artifact_to_dict(art)
    assert d["artifact_id"] == "a1"
    assert "relative_path" in d
