import pytest
from pathlib import Path

from config.settings import Settings
from data.storage.data_lake import DataLake
from observability.observability_config import ObservabilityProfile
from observability.component_health import ComponentHealthChecker

class MockPaths:
    def __init__(self, root: Path):
        self.lake_dir = root / "lake"
        self.LAKE_DIR = self.lake_dir
        self.LAKE_DIR.mkdir(parents=True, exist_ok=True)

def test_component_health_checker(tmp_path):
    settings = Settings()
    profile = ObservabilityProfile(name="test", description="test")
    paths = MockPaths(tmp_path)
    lake = DataLake(paths)
    lake.paths = paths

    checker = ComponentHealthChecker(lake, settings, profile)

    # Test specific components (will likely be degraded/unhealthy due to empty dir)
    ml_health = checker.check_component("ml_pipeline")
    assert ml_health.component == "ml_pipeline"
    assert ml_health.status in ["degraded", "unhealthy", "healthy"]

    # Check all
    df, summary = checker.check_all_components()
    assert not df.empty
    assert "ml_pipeline" in df["component"].values
    assert summary["components_checked"] >= 4
    assert "overall_score" in summary
