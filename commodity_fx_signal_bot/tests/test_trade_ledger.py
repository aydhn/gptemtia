import pytest
import pandas as pd
from backtesting.trade_ledger import TradeLedger
from backtesting.backtest_models import SimulatedTrade


def test_trade_ledger():
    ledger = TradeLedger()
    t = SimulatedTrade(
        symbol="GC=F",
        timeframe="1d",
        trade_id="123",
        source_level_id="",
        source_sizing_id="",
        source_risk_id="",
        strategy_family="",
        directional_bias="",
        entry_timestamp="2020-01-01",
        entry_price=10.0,
        exit_timestamp="2020-01-02",
        exit_price=12.0,
        theoretical_stop_level=None,
        theoretical_target_level=None,
        theoretical_units=1.0,
        adjusted_theoretical_units=1.0,
        theoretical_notional=10.0,
        gross_pnl=2.0,
        fee_cost=0.0,
        slippage_cost=0.0,
        net_pnl=2.0,
        return_pct=0.2,
        holding_bars=1,
        lifecycle_status="simulated_closed",
        entry_reason="",
        exit_reason="",
        result_label="win",
        warnings=[],
    )
    ledger.add(t)
    df = ledger.to_dataframe()
    assert not df.empty

    s = ledger.summarize()
    assert s["win_count"] == 1
