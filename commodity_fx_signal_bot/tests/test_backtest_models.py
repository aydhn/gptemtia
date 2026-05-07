import pytest
from backtesting.backtest_models import (
    build_backtest_run_id,
    build_trade_id,
    SimulatedTrade,
    simulated_trade_to_dict,
)


def test_build_backtest_run_id_deterministic():
    id1 = build_backtest_run_id("prof", "1d", ["B", "A"])
    id2 = build_backtest_run_id("prof", "1d", ["A", "B"])
    assert id1 == id2


def test_build_trade_id_deterministic():
    id1 = build_trade_id("GC=F", "1d", "lvl1")
    id2 = build_trade_id("GC=F", "1d", "lvl1")
    assert id1 == id2


def test_simulated_trade_to_dict():
    trade = SimulatedTrade(
        symbol="GC=F",
        timeframe="1d",
        trade_id="123",
        source_level_id="",
        source_sizing_id="",
        source_risk_id="",
        strategy_family="",
        directional_bias="",
        entry_timestamp=None,
        entry_price=None,
        exit_timestamp=None,
        exit_price=None,
        theoretical_stop_level=None,
        theoretical_target_level=None,
        theoretical_units=1.0,
        adjusted_theoretical_units=1.0,
        theoretical_notional=None,
        gross_pnl=None,
        fee_cost=0.0,
        slippage_cost=0.0,
        net_pnl=None,
        return_pct=None,
        holding_bars=0,
        lifecycle_status="",
        entry_reason="",
        exit_reason="",
        result_label="",
        warnings=[],
    )
    d = simulated_trade_to_dict(trade)
    assert d["symbol"] == "GC=F"
