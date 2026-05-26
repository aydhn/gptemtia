from pathlib import Path
from maintenance.storage_inventory import StorageInventoryBuilder
from maintenance.maintenance_config import get_default_maintenance_profile

def test_inventory_builder_methods(tmp_path):
    builder = StorageInventoryBuilder(tmp_path)

    raw_path = tmp_path / "data" / "lake" / "raw" / "test.csv"
    assert builder.classify_artifact_type(raw_path) == "raw_data"
    assert builder.classify_retention_category(raw_path) == "raw_data_retention"

    assert builder.is_protected_artifact(Path("README.md")) is True
    assert builder.is_protected_artifact(Path("test.py")) is True
    assert builder.is_protected_artifact(Path("config.yaml")) is True
    assert builder.is_protected_artifact(Path("data/test.csv")) is False

    profile = get_default_maintenance_profile()
    df, summary = builder.scan_storage(profile)
    assert df.empty  # Since tmp_path is empty
    assert summary["total_files"] == 0
