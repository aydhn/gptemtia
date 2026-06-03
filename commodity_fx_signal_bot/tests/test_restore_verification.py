from backup_recovery.restore_verification import verify_restore_manifest_integrity

def test_verify_restore_manifest_integrity():
    res = verify_restore_manifest_integrity({})
    assert res.passed == True
