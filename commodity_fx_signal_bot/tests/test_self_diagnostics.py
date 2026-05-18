import pytest
from pathlib import Path

from config.settings import Settings
from config.symbols import SymbolSpec
from data.storage.data_lake import DataLake
from observability.observability_config import ObservabilityProfile
from observability.self_diagnostics import SelfDiagnosticsRunner

class MockPaths:
    def __init__(self, root: Path):
        self.lake_dir = root / "lake"
        self.LAKE_DIR = self.lake_dir
        self.DATA_DIR = root / "data"
        self.REPORTS_DIR = root / "reports"
        self.LAKE_PROCESSED_OHLCV_DIR = self.lake_dir / "processed" / "ohlcv"
        self.LAKE_FEATURES_TECHNICAL_DIR = self.lake_dir / "features" / "technical"
        self.LAKE_DIR.mkdir(parents=True, exist_ok=True)
        self.DATA_DIR.mkdir(parents=True, exist_ok=True)
        self.REPORTS_DIR.mkdir(parents=True, exist_ok=True)
        self.LAKE_PROCESSED_OHLCV_DIR.mkdir(parents=True, exist_ok=True)
        self.LAKE_FEATURES_TECHNICAL_DIR.mkdir(parents=True, exist_ok=True)

def test_self_diagnostics_runner(tmp_path):
    settings = Settings()
    profile = ObservabilityProfile(name="test", description="test")
    paths = MockPaths(tmp_path)
    lake = DataLake(paths)
    lake.paths = paths

    runner = SelfDiagnosticsRunner(lake, settings, profile)
    spec = SymbolSpec(symbol="GC=F", name="Gold", asset_class="metals", sub_class="precious", currency="USD", data_source="yahoo")

    details, summary = runner.run_symbol_diagnostics(spec, "1d")

    assert "basic_health" in details
    assert "data_freshness" in details
    assert "artifact_integrity" in details
    assert "pipeline_health" in details

    assert "overall_health_status" in summary
    assert "recommended_system_actions" in summary
    assert isinstance(summary["recommended_system_actions"], list)

    # Check that recommendations don't contain trade terminology
    trade_terms = ["LIVE_ORDER", "BROKER_ORDER", "SEND_ORDER", "EXECUTE_TRADE"]
    for act in summary["recommended_system_actions"]:
        for term in trade_terms:
            assert term not in act.upper()
