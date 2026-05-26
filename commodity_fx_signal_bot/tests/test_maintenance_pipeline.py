from maintenance.maintenance_pipeline import MaintenancePipeline
from maintenance.maintenance_config import get_default_maintenance_profile
from config.settings import Settings
from config.paths import ProjectPaths
from unittest.mock import MagicMock

def test_maintenance_pipeline(tmp_path):
    settings = Settings()
    paths = ProjectPaths()
    paths.PROJECT_ROOT = tmp_path

    dl_mock = MagicMock()
    profile = get_default_maintenance_profile()

    pipe = MaintenancePipeline(dl_mock, settings, tmp_path, profile)

    # Very basic smoke test
    df, summary = pipe.build_storage_inventory_report(save=False)
    assert df is not None
    assert isinstance(summary, dict)

    df, summary = pipe.build_retention_policy_report(save=False)
    assert not df.empty

    df, summary = pipe.build_cleanup_dry_run_report(save=False)
    assert df is not None
