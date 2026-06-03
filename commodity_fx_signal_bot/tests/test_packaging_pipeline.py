from portable_packaging.packaging_pipeline import PortablePackagingPipeline
from portable_packaging.packaging_config import get_default_portable_packaging_profile
from data.storage.data_lake import DataLake
from config.settings import settings
from pathlib import Path

def test_packaging_pipeline(tmp_path):
    profile = get_default_portable_packaging_profile()
    dl = DataLake(tmp_path)

    # Monkeypatch DL methods so they don't actually write to non-existent hardcoded paths if they try
    dl.save_environment_snapshot = lambda a, b, c: None
    dl.save_dependency_inventory = lambda a, b: None
    dl.save_requirements_export_report = lambda a, b: None
    dl.save_install_verification_report = lambda a, b: None
    dl.save_portable_bundle_manifest = lambda a: None
    dl.save_bundle_artifact_inventory = lambda a, b: None

    pipeline = PortablePackagingPipeline(dl, settings, tmp_path, profile)

    _, s1 = pipeline.build_environment_snapshot_report(save=False)
    assert s1 is not None

    _, s2 = pipeline.build_dependency_inventory_report(save=False)
    assert s2 is not None

    # We ignore file paths that are outside of tmp_path since save=False
