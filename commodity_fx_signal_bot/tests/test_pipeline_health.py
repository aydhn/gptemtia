import pytest
from pathlib import Path

from config.settings import Settings
from config.symbols import SymbolSpec
from data.storage.data_lake import DataLake
from observability.observability_config import ObservabilityProfile
from observability.pipeline_health import PipelineHealthChecker

class MockPaths:
    def __init__(self, root: Path):
        self.lake_dir = root / "lake"
        self.LAKE_DIR = self.lake_dir
        self.LAKE_PROCESSED_OHLCV_DIR = self.lake_dir / "processed" / "ohlcv"
        self.LAKE_FEATURES_TECHNICAL_DIR = self.lake_dir / "features" / "technical"
        self.LAKE_DIR.mkdir(parents=True, exist_ok=True)

def test_pipeline_health_checker(tmp_path):
    settings = Settings()
    profile = ObservabilityProfile(name="test", description="test")
    paths = MockPaths(tmp_path)
    lake = DataLake(paths)
    lake.paths = paths

    checker = PipelineHealthChecker(lake, settings, profile)
    spec = SymbolSpec(symbol="GC=F", name="Gold", asset_class="metals", sub_class="precious", currency="USD", data_source="yahoo")

    # Missing outputs
    out_check = checker.check_pipeline_outputs("data", spec, "1d")
    assert out_check["required_outputs_available"] == False

    # Create fake output
    safe_symbol = DataLake.safe_symbol_name(spec.symbol)
    f = paths.LAKE_PROCESSED_OHLCV_DIR / "1d" / f"{safe_symbol}.parquet"
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text("dummy content")

    out_check2 = checker.check_pipeline_outputs("data", spec, "1d")
    assert out_check2["required_outputs_available"] == True

    # Build report
    df, summary = checker.build_pipeline_health_report([spec], "1d")
    assert not df.empty
    assert summary["total_pipelines_checked"] == 7
    assert "data" in df["pipeline_name"].values
