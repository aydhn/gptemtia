import pytest
import pandas as pd
from unittest.mock import MagicMock
from research_reports.data_collector import ResearchDataCollector
from config.symbols import SymbolSpec

@pytest.fixture
def mock_data_lake():
    dl = MagicMock()
    dl.load_processed_ohlcv.return_value = pd.DataFrame({"close": [1, 2], "volume": [10, 20]}, index=pd.date_range("2023-01-01", periods=2))
    dl.load_technical_features.return_value = {"feat": 1}
    dl.load_signal_candidates.return_value = [{"signal": "long"}]
    dl.load_decision_candidates.return_value = [{"decision": "no_trade"}]
    dl.load_strategy_candidates.side_effect = Exception("Not found")
    return dl

def test_collect_symbol_inputs(mock_data_lake):
    collector = ResearchDataCollector(mock_data_lake)
    spec = SymbolSpec("AAPL", "Apple", "equities", "stock", "USD")
    inputs, metadata = collector.collect_symbol_inputs(spec, "1d")

    assert "ohlcv" in inputs
    assert "technical_features" in inputs
    assert "signal_candidates" in inputs

    assert "strategy_candidates" in metadata["missing_sources"]
    assert metadata["data_available"] is True

def test_collect_universe_inputs(mock_data_lake):
    collector = ResearchDataCollector(mock_data_lake)
    specs = [SymbolSpec("AAPL", "Apple", "equities", "stock", "USD"), SymbolSpec("MSFT", "Microsoft", "equities", "stock", "USD")]

    universe_inputs, metadata = collector.collect_universe_inputs(specs, "1d")

    assert "AAPL" in universe_inputs
    assert "MSFT" in universe_inputs
    assert metadata["symbols_collected"] == 2

def test_single_symbol_error_does_not_crash_universe():
    dl = MagicMock()
    # first call fails, second succeeds
    dl.load_processed_ohlcv.side_effect = [Exception("Crash"), pd.DataFrame({"close": [1]})]

    collector = ResearchDataCollector(dl)
    specs = [SymbolSpec("AAPL", "Apple", "equities", "stock", "USD"), SymbolSpec("MSFT", "Microsoft", "equities", "stock", "USD")]

    universe_inputs, metadata = collector.collect_universe_inputs(specs, "1d")

    # Actually the inner collect_symbol_inputs catches all exceptions per source,
    # so it won't crash either way, but we verify we have 2 symbols processed
    assert "AAPL" in universe_inputs
    assert "MSFT" in universe_inputs
    assert metadata["symbols_collected"] == 2
