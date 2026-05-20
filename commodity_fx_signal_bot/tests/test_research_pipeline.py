import pytest
from unittest.mock import MagicMock
import pandas as pd
from research_reports.research_pipeline import ResearchReportPipeline
from config.symbols import SymbolSpec
from config.settings import Settings
from research_reports.research_config import ResearchReportProfile

@pytest.fixture
def mock_data_lake():
    dl = MagicMock()
    dl.load_processed_ohlcv.return_value = pd.DataFrame({"close": [1]}, index=pd.date_range("2023-01-01", periods=1))
    return dl

def test_build_symbol_report(mock_data_lake):
    settings = Settings()
    prof = ResearchReportProfile("test", "test")
    pipeline = ResearchReportPipeline(mock_data_lake, settings, prof)

    spec = SymbolSpec("AAPL", "Apple", "equities", "stock", "USD")
    report, quality = pipeline.build_symbol_report(spec, "1d", save=False)

    assert report.report_type == "symbol_research"
    assert "AAPL" in report.symbols
    assert quality["passed"] is True
    # Test that save wasn't called
    mock_data_lake.save_symbol_research_report.assert_not_called()

def test_build_universe_report(mock_data_lake):
    settings = Settings()
    prof = ResearchReportProfile("test", "test")
    pipeline = ResearchReportPipeline(mock_data_lake, settings, prof)

    specs = [SymbolSpec("AAPL", "Apple", "equities", "stock", "USD"), SymbolSpec("MSFT", "Microsoft", "equities", "stock", "USD")]
    report, quality = pipeline.build_universe_report(specs, "1d", save=False)

    assert report.report_type == "universe_research"
    assert "ranking" in report.tables
    assert report.summary["total_symbols_ranked"] == 2

def test_build_daily_digest(mock_data_lake):
    settings = Settings()
    prof = ResearchReportProfile("test", "test")
    pipeline = ResearchReportPipeline(mock_data_lake, settings, prof)

    specs = [SymbolSpec("AAPL", "Apple", "equities", "stock", "USD")]
    report, quality = pipeline.build_daily_digest(specs, "1d", save=False)

    assert report.report_type == "daily_digest"
    assert "ranking" in report.tables
