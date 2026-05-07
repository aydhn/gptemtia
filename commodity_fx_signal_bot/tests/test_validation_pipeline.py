import pytest
import pandas as pd
from unittest.mock import MagicMock

from validation.validation_pipeline import ValidationPipeline
from config.settings import Settings
from config.symbols import SymbolSpec

@pytest.fixture
def mock_data_lake():
    dl = MagicMock()

    idx = pd.date_range("2020-01-01", periods=1000, freq="D")
    price_df = pd.DataFrame({"close": range(1000)}, index=idx)
    dl.load_processed_ohlcv.return_value = price_df

    trades_df = pd.DataFrame({
        "entry_time": idx[:-1],
        "exit_time": idx[1:],
        "pnl_pct": [0.01, -0.005] * 499 + [0.01]
    })
    dl.load_backtest_trades.return_value = trades_df

    equity = pd.DataFrame({"equity": range(1000)})
    dl.load_backtest_equity_curve.return_value = equity

    summary = {
        "parameters": {"p1": 1, "p2": 2},
        "sharpe_ratio": 1.5,
        "total_return_pct": 20.0,
        "trade_count": 100
    }
    dl.load_backtest_summary.return_value = summary

    return dl

@pytest.fixture
def settings():
    s = Settings()
    s.save_walk_forward_results = False
    s.save_parameter_sensitivity = False
    s.save_validation_results = False
    return s

@pytest.fixture
def spec():
    return SymbolSpec(symbol="TEST", name="Test", asset_class="test", sub_class="test", currency="USD")

def test_load_validation_inputs(mock_data_lake, settings, spec):
    pipeline = ValidationPipeline(mock_data_lake, settings)
    p, t, e, s = pipeline.load_validation_inputs(spec, "1d", "prof")

    assert p is not None
    assert t is not None
    assert e is not None
    assert s is not None

def test_run_walk_forward_validation(mock_data_lake, settings, spec):
    pipeline = ValidationPipeline(mock_data_lake, settings)
    df, summary = pipeline.run_walk_forward_validation(spec, save=False)

    assert not df.empty
    assert "symbol" in summary
    assert "robustness" in summary
    assert "overfitting" in summary
    assert "quality_report" in summary
    assert summary["quality_report"]["passed"] is True

def test_run_parameter_sensitivity(mock_data_lake, settings, spec):
    pipeline = ValidationPipeline(mock_data_lake, settings)
    df, summary = pipeline.run_parameter_sensitivity(spec, save=False)

    assert not df.empty
    assert "symbol" in summary
    assert "quality_report" in summary
    assert summary["quality_report"]["passed"] is True

def test_run_optimizer_candidate_analysis(mock_data_lake, settings, spec):
    pipeline = ValidationPipeline(mock_data_lake, settings)
    df, summary = pipeline.run_optimizer_candidate_analysis(spec, save=False)

    assert not df.empty
    assert "total_candidates" in summary
    assert "quality_report" in summary
    assert summary["quality_report"]["passed"] is True

def test_run_universe_validation(mock_data_lake, settings, spec):
    pipeline = ValidationPipeline(mock_data_lake, settings)
    spec2 = SymbolSpec(symbol="TEST2", name="Test 2", asset_class="test", sub_class="test", currency="USD")
    res = pipeline.run_universe_validation([spec, spec2], limit=2, save=False)

    assert res["processed_count"] == 2
    assert len(res["ranking"]) == 2
    assert "validation_status" in res["ranking"][0]
