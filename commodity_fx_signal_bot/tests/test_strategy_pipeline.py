from unittest.mock import MagicMock

import pandas as pd
import pytest

from config.settings import settings
from config.symbols import SymbolSpec
from strategies.strategy_pipeline import StrategyPipeline


@pytest.fixture
def mock_data_lake():
    lake = MagicMock()
    lake.has_features.side_effect = lambda spec, tf, fset: True
    df = pd.DataFrame(
        {
            "decision_label": ["long_bias_candidate"],
            "candidate_type": ["trend_following"],
            "decision_score": [0.8],
            "quality_score": [0.9],
            "confidence": [0.9],
        },
        index=[pd.Timestamp("2023-01-01")],
    )
    lake.load_features.return_value = df
    return lake


def test_build_for_symbol_timeframe(mock_data_lake):
    pipeline = StrategyPipeline(mock_data_lake, settings)
    spec = SymbolSpec("TEST", "TEST", "crypto", "test", "USD")

    df, summary = pipeline.build_for_symbol_timeframe(spec, "1d", save=False)
    assert not df.empty
    assert summary["strategy_candidate_count"] > 0


def test_skip_synthetic(mock_data_lake):
    pipeline = StrategyPipeline(mock_data_lake, settings)
    spec = SymbolSpec("TEST", "TEST", "synthetic", "test", "USD")
    df, summary = pipeline.build_for_symbol_timeframe(spec, "1d", save=False)
    assert df.empty
    assert summary.get("skipped") is True
