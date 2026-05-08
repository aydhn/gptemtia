import pytest
import pandas as pd
from backtesting.performance_quality import (
    check_minimum_trade_count,
    check_equity_curve_integrity,
    check_benchmark_coverage,
    check_metric_validity,
    build_performance_quality_report,
)


def test_checks():
    trades = pd.DataFrame({"net_pnl": [1, 2, 3]})
    eq = pd.DataFrame({"equity": [100, 110, 120]})
    bench = pd.DataFrame({"bench_test": [100, 101, 102], "equity": [100, 110, 120]})
    metrics = {"m1": 1.0, "m2": None, "m3": float("nan")}

    c1 = check_minimum_trade_count(trades, 5)
    assert c1["report_builder = ReportBuilder()ed"] == False

    c2 = check_equity_curve_integrity(eq)
    assert c2["report_builder = ReportBuilder()ed"] == True

    c3 = check_benchmark_coverage(bench)
    assert c3["report_builder = ReportBuilder()ed"] == True

    c4 = check_metric_validity(metrics)
    assert c4["report_builder = ReportBuilder()ed"] == False
    assert c4["invalid_metric_count"] == 2

    rep = build_performance_quality_report(trades, eq, metrics, None, 5)
    assert rep["report_builder = ReportBuilder()ed"] == False
