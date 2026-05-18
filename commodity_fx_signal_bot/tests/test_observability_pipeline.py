import pytest
from pathlib import Path

from config.settings import Settings
from data.storage.data_lake import DataLake
from observability.observability_config import ObservabilityProfile
from observability.observability_pipeline import ObservabilityPipeline

class MockPaths:
    def __init__(self, root: Path):
        self.lake_dir = root / "lake"
        self.DATA_DIR = root / "data"
        self.REPORTS_DIR = root / "reports"
        self.LAKE_DIR = self.lake_dir
        self.LAKE_PROCESSED_OHLCV_DIR = self.lake_dir / "processed" / "ohlcv"
        self.LAKE_FEATURES_TECHNICAL_DIR = self.lake_dir / "features" / "technical"

        for p in [self.LAKE_DIR, self.DATA_DIR, self.REPORTS_DIR, self.LAKE_PROCESSED_OHLCV_DIR, self.LAKE_FEATURES_TECHNICAL_DIR]:
            p.mkdir(parents=True, exist_ok=True)

class MockDataLake(DataLake):
    def __init__(self, paths):
        self.paths = paths
        self.root_dir = paths.LAKE_DIR
        self.saved_health = False
        self.saved_diagnostics = False

    def save_observability_health_report(self, *args, **kwargs):
        self.saved_health = True

    def save_diagnostics_report(self, *args, **kwargs):
        self.saved_diagnostics = True

def test_observability_pipeline(tmp_path):
    settings = Settings()
    profile = ObservabilityProfile(name="test", description="test")
    paths = MockPaths(tmp_path)
    lake = MockDataLake(paths)

    pipeline = ObservabilityPipeline(lake, settings, profile)

    # Test system healthcheck
    df, summary = pipeline.run_system_healthcheck(save=True)
    assert not df.empty
    assert lake.saved_health == True

    # Test component healthcheck
    df2, summary2 = pipeline.run_component_healthcheck(save=False)
    assert not df2.empty

    # Test self diagnostics
    details, d_sum = pipeline.run_self_diagnostics(save=True)
    assert d_sum["overall_health_score"] >= 0.0
    assert lake.saved_diagnostics == True
