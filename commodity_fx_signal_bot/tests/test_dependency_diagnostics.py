import pytest
from pathlib import Path

from config.symbols import SymbolSpec
from data.storage.data_lake import DataLake
from observability.dependency_diagnostics import DependencyDiagnostics

class MockPaths:
    def __init__(self, root: Path):
        self.lake_dir = root / "lake"
        self.LAKE_PROCESSED_OHLCV_DIR = self.lake_dir / "processed" / "ohlcv"
        self.LAKE_FEATURES_DIR = self.lake_dir / "features"
        self.LAKE_DIR = self.lake_dir

        # We must create some mock directories if we want exists to return True for them
        self.LAKE_PROCESSED_OHLCV_DIR.mkdir(parents=True, exist_ok=True)
        self.LAKE_FEATURES_DIR.mkdir(parents=True, exist_ok=True)

@pytest.fixture
def mock_data_lake(tmp_path):
    paths = MockPaths(tmp_path)
    # The __init__ of DataLake might overwrite paths if it's passed directly or it might try to import ProjectPaths
    # Let's bypass internal __init__ logic if it's too tied to globals, or just use the MockPaths
    lake = DataLake(paths)
    lake.paths = paths
    return lake

def test_check_feature_dependencies(mock_data_lake):
    diag = DependencyDiagnostics(mock_data_lake)
    spec = SymbolSpec(symbol="EURUSD=X", asset_class="forex", sub_class="core", currency="USD", name="EURUSD", data_source="yahoo")

    # Check missing
    df, summary = diag.check_feature_dependencies(spec, timeframe="1d")
    assert not df.empty
    assert df.iloc[0]["available"] == False
    assert summary["missing"] == 1

    # Create the file and check again
    safe_symbol = DataLake.safe_symbol_name(spec.symbol)
    p = mock_data_lake.paths.LAKE_PROCESSED_OHLCV_DIR / "1d" / f"{safe_symbol}.parquet"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.touch()

    df, summary = diag.check_feature_dependencies(spec, timeframe="1d")
    assert df.iloc[0]["available"] == True
    assert summary["missing"] == 0

def test_build_full_dependency_diagnostics(mock_data_lake):
    diag = DependencyDiagnostics(mock_data_lake)
    spec = SymbolSpec(symbol="GC=F", asset_class="metals", sub_class="precious", currency="USD", name="Gold", data_source="yahoo")

    df, summary = diag.build_full_dependency_diagnostics(spec, timeframe="1d")

    assert not df.empty
    assert summary["total_dependencies"] > 0
    assert summary["missing_dependencies"] == summary["total_dependencies"]
    assert summary["status"] == "degraded" # because all are missing
