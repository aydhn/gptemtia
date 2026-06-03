from backup_recovery.backup_models import (
    build_project_state_artifact_id,
    build_backup_policy_id,
    build_backup_manifest_id,
    build_restore_item_id,
    build_restore_verification_check_id
)

def test_model_id_builders():
    assert build_project_state_artifact_id("test/path").isalnum()
    assert build_backup_policy_id("test_scope") == "pol_test_scope"
    assert "man_" in build_backup_manifest_id("profile", "time")
    assert "res_" in build_restore_item_id("art1", "action1")
    assert "chk_" in build_restore_verification_check_id("check1")
