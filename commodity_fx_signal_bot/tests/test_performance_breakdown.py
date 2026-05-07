import pytest
import pandas as pd
from backtesting.performance_breakdown import (
    build_symbol_performance_breakdown,
    build_asset_class_performance_breakdown,
    build_strategy_family_performance_breakdown,
    build_directional_bias_performance_breakdown,
    build_exit_reason_performance_breakdown,
    build_result_label_performance_breakdown,
    build_full_performance_breakdown,
)
from config.symbols import SymbolSpec


def test_breakdowns():
    trades = pd.DataFrame(
        {
            "symbol": ["GC=F", "GC=F", "EURUSD=X"],
            "net_pnl": [10.0, -5.0, 20.0],
            "return_pct": [0.1, -0.05, 0.2],
            "strategy_family": ["trend", "momentum", "trend"],
            "direction": ["long", "short", "long"],
            "exit_reason": ["tp", "sl", "tp"],
            "result_label": ["win", "loss", "win"],
        }
    )

    spec1 = SymbolSpec("GC=F", "Gold", "metals", "gold", "USD")
    spec2 = SymbolSpec("EURUSD=X", "EUR/USD", "fx", "major", "USD")

    sym_bd = build_symbol_performance_breakdown(trades)
    assert not sym_bd.empty

    ast_bd = build_asset_class_performance_breakdown(trades, [spec1, spec2])
    assert not ast_bd.empty

    strat_bd = build_strategy_family_performance_breakdown(trades)
    assert not strat_bd.empty

    dir_bd = build_directional_bias_performance_breakdown(trades)
    assert not dir_bd.empty

    exit_bd = build_exit_reason_performance_breakdown(trades)
    assert not exit_bd.empty

    res_bd = build_result_label_performance_breakdown(trades)
    assert not res_bd.empty

    full = build_full_performance_breakdown(trades, [spec1, spec2])
    assert "symbol_breakdown" in full
