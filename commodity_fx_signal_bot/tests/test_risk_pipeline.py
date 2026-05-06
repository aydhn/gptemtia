from unittest.mock import MagicMock
import pandas as pd
from risk.risk_pipeline import RiskPipeline
from config.symbols import SymbolSpec
from config.settings import Settings


def test_risk_pipeline_skip_synthetic():
    mock_lake = MagicMock()
    settings = Settings()
    pipeline = RiskPipeline(mock_lake, settings)

    spec = SymbolSpec("SYNTH", "Synthetic", "Index", "Synthetic", "USD")
    df, summary = pipeline.build_for_symbol_timeframe(spec)
    assert df.empty
    assert summary.get("skipped")


def test_risk_pipeline_missing_rule_candidates():
    mock_lake = MagicMock()
    mock_lake.has_features.return_value = False

    settings = Settings()
    pipeline = RiskPipeline(mock_lake, settings)

    spec = SymbolSpec("AAPL", "Equity", "Stock", "Stock", "USD")
    df, summary = pipeline.build_for_symbol_timeframe(spec)
    assert df.empty
    assert "warning" in summary


def test_risk_pipeline_build_universe():
    mock_lake = MagicMock()
    mock_lake.has_features.return_value = False

    settings = Settings()
    pipeline = RiskPipeline(mock_lake, settings)

    spec = SymbolSpec("AAPL", "Equity", "Stock", "Stock", "USD")
    res = pipeline.build_for_universe([spec])
    assert res["processed"] == 1
    assert res["total_candidates"] == 0
