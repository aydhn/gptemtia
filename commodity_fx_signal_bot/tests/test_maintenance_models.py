from maintenance.maintenance_models import (
    StorageArtifactRecord, build_storage_artifact_id,
    build_retention_policy_id, build_maintenance_candidate_id,
    build_archive_id, storage_artifact_record_to_dict
)

def test_deterministic_ids():
    id1 = build_storage_artifact_id("test/path.txt", 100, "2023-01-01")
    id2 = build_storage_artifact_id("test/path.txt", 100, "2023-01-01")
    assert id1 == id2

    assert build_retention_policy_id("raw_data") == "policy_raw_data"

    cand1 = build_maintenance_candidate_id("art1", "action1")
    assert cand1 == "cand_art1_action1"

    arch1 = build_archive_id("test", "2023-01-01")
    arch2 = build_archive_id("test", "2023-01-01")
    assert arch1 == arch2

def test_to_dict():
    record = StorageArtifactRecord(
        artifact_id="1", path="a", relative_path="a", artifact_type="t",
        retention_category="r", size_bytes=10, modified_at_utc="2023-01-01",
        age_days=1.0, extension=".txt", protected=False, lifecycle_label="active",
        warnings=[]
    )
    d = storage_artifact_record_to_dict(record)
    assert "artifact_id" in d
    assert d["artifact_id"] == "1"
