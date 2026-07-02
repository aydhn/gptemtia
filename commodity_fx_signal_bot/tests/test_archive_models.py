import pytest
from local_archive.archive_models import (
    build_archive_domain_id,
    build_archive_item_id,
    build_snapshot_id,
    build_retention_policy_id,
    ArchiveDomain,
    archive_domain_to_dict
)

def test_deterministic_ids():
    id1 = build_archive_domain_id("test")
    id2 = build_archive_domain_id("test")
    assert id1 == id2

    id3 = build_archive_item_id("path/to/file")
    id4 = build_archive_item_id("path/to/file")
    assert id3 == id4

def test_to_dict():
    domain = ArchiveDomain(
        domain_id="dom_123",
        domain_name="test",
        domain_label="test_archive",
        description="test desc",
        retention_label="retain",
        required_artifacts=[],
        warnings=[]
    )
    d = archive_domain_to_dict(domain)
    assert d["domain_id"] == "dom_123"
    assert d["domain_label"] == "test_archive"
