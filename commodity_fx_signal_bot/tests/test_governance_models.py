from governance.governance_models import (
    ArtifactRecord,
    artifact_record_to_dict,
    build_artifact_id,
    build_lineage_edge_id,
    build_provenance_id,
)


def test_build_artifact_id_deterministic():
    id1 = build_artifact_id("data/test.csv", 1024, "2024-01-01T00:00:00Z")
    id2 = build_artifact_id("data/test.csv", 1024, "2024-01-01T00:00:00Z")
    assert id1 == id2
    assert isinstance(id1, str)

def test_build_provenance_id_deterministic():
    id1 = build_provenance_id("art_123", "feature_pipeline")
    id2 = build_provenance_id("art_123", "feature_pipeline")
    assert id1 == id2

def test_build_lineage_edge_id_deterministic():
    id1 = build_lineage_edge_id("n1", "n2", "derived_from")
    id2 = build_lineage_edge_id("n1", "n2", "derived_from")
    assert id1 == id2

def test_artifact_record_to_dict():
    rec = ArtifactRecord(
        artifact_id="1", artifact_type="raw_data_artifact", path="/a/b", relative_path="b",
        file_name="b", extension=".csv", size_bytes=10, modified_at_utc=None, created_at_utc=None,
        row_count=None, column_count=None, schema_fingerprint=None, content_fingerprint=None, warnings=[]
    )
    d = artifact_record_to_dict(rec)
    assert d["artifact_id"] == "1"
    assert "artifact_type" in d
