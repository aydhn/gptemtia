import pytest
from backup_recovery.backup_labels import (
    list_backup_scope_labels,
    list_backup_status_labels,
    list_restore_status_labels,
    list_recovery_readiness_labels,
    list_artifact_criticality_labels,
    validate_backup_scope,
    validate_backup_status,
    validate_restore_status,
    validate_recovery_readiness,
    validate_artifact_criticality
)

def test_lists_not_empty():
    assert len(list_backup_scope_labels()) > 0
    assert len(list_backup_status_labels()) > 0
    assert len(list_restore_status_labels()) > 0
    assert len(list_recovery_readiness_labels()) > 0
    assert len(list_artifact_criticality_labels()) > 0

def test_validations():
    validate_backup_scope("critical_source_scope")
    validate_backup_status("backup_plan_ready")
    validate_restore_status("restore_plan_ready_dry_run")
    validate_recovery_readiness("recovery_ready_for_local_dry_run")
    validate_artifact_criticality("critical_artifact")

    with pytest.raises(ValueError):
        validate_backup_scope("invalid")
