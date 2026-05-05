from unittest.mock import MagicMock

import pandas as pd
import pytest

from config.symbols import SymbolSpec
from strategies.strategy_context import StrategyContextLoader


@pytest.fixture
def mock_data_lake():
    lake = MagicMock()
    lake.has_features.side_effect = lambda spec, tf, fset: True
    df = pd.DataFrame({"decision_score": [0.8]}, index=[pd.Timestamp("2023-01-01")])
    lake.load_features.return_value = df
    return lake


def test_load_decision_candidates(mock_data_lake):
    loader = StrategyContextLoader(mock_data_lake)
    spec = SymbolSpec("TEST", "TEST", "crypto", "test", "USD")
    df, summary = loader.load_decision_candidates(spec, "1d")
    assert not df.empty
    assert "missing_decision_candidates" in summary
    assert summary["missing_decision_candidates"] is False


def test_load_strategy_context_frames(mock_data_lake):
    loader = StrategyContextLoader(mock_data_lake)
    spec = SymbolSpec("TEST", "TEST", "crypto", "test", "USD")
    frames, summary = loader.load_strategy_context_frames(spec, "1d")
    assert isinstance(frames, dict)
    assert "missing_context_frames" in summary


def test_get_context_snapshot():
    loader = StrategyContextLoader(MagicMock())
    ts1 = pd.Timestamp("2023-01-01")
    ts2 = pd.Timestamp("2023-01-02")
    df = pd.DataFrame({"regime_label": ["bullish", "bearish"]}, index=[ts1, ts2])
    frames = {"regime": df}

    snap1 = loader.get_context_snapshot(frames, ts1)
    assert snap1["regime"]["regime_label"] == "bullish"

    snap2 = loader.get_context_snapshot(frames, ts2)
    assert snap2["regime"]["regime_label"] == "bearish"
