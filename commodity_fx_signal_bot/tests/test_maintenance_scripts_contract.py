import pytest

def test_maintenance_scripts_importable():
    import scripts.run_storage_inventory_report
    import scripts.run_retention_policy_report
    import scripts.run_cleanup_dry_run_report
    import scripts.run_archive_dry_run_report
    import scripts.run_storage_lifecycle_report
    import scripts.run_maintenance_status

    assert True
