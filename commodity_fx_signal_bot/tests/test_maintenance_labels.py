import pytest
from maintenance.maintenance_labels import (
    list_artifact_lifecycle_labels, list_retention_category_labels,
    list_maintenance_action_labels, list_storage_health_labels,
    validate_artifact_lifecycle, validate_maintenance_action
)

def test_label_lists_not_empty():
    assert len(list_artifact_lifecycle_labels()) > 0
    assert len(list_retention_category_labels()) > 0
    assert len(list_maintenance_action_labels()) > 0
    assert len(list_storage_health_labels()) > 0

def test_validate_labels():
    validate_artifact_lifecycle("cleanup_candidate")
    validate_maintenance_action("cleanup_dry_run_action")

    with pytest.raises(ValueError):
        validate_artifact_lifecycle("invalid_label")

    with pytest.raises(ValueError):
        validate_maintenance_action("invalid_label")

def test_cleanup_candidate_naming():
    # Should not have "automatic" or "delete" in the label
    assert "cleanup_candidate" in list_artifact_lifecycle_labels()
    assert "automatic_delete" not in list_artifact_lifecycle_labels()
