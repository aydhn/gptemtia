import pytest
import pandas as pd
from unittest.mock import MagicMock
from backtesting.performance_pipeline import PerformanceAnalysisPipeline
from config.settings import Settings
from config.symbols import SymbolSpec


def test_pipeline():
    settings = Settings()
    data_lake = MagicMock()

    # Mock data
    idx = pd.date_range("2024-01-01", periods=10)
    trades = pd.DataFrame(
        {
            "net_pnl": [10.0] * 5,
            "return_pct": [0.1] * 5,
            "holding_bars": [2] * 5,
            "result_label": ["win"] * 5,
        }
    )
    equity = pd.DataFrame({"equity": [100.0 + i * 10 for i in range(10)]}, index=idx)
    macro = pd.DataFrame(
        {"bench_usdtry_index": [100.0 + i for i in range(10)]}, index=idx
    )

    data_lake.load_backtest_trades.return_value = trades
    data_lake.load_backtest_equity_curve.return_value = equity
    data_lake.load_macro_features.return_value = macro

    pipeline = PerformanceAnalysisPipeline(data_lake, settings)

    spec = SymbolSpec("GC=F", "Gold", "metals", "gold", "USD")
    summary, _ = pipeline.analyze_symbol_performance(spec, save=False)

    assert summary is not None
    assert "advanced_metrics" in summary
    assert "quality_report" in summary

    batch = pipeline.analyze_universe_performance([spec], save=False)
    assert len(batch["ranking"]) == 1
