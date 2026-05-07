import pandas as pd
import numpy as np


def check_minimum_trade_count(trades_df: pd.DataFrame, min_trades: int = 5) -> dict:
    trade_count = len(trades_df) if not trades_df.empty else 0
    passed = trade_count >= min_trades
    return {
        "passed": passed,
        "trade_count": trade_count,
        "min_required": min_trades,
        "warning": (
            f"Insufficient trades: {trade_count} < {min_trades}" if not passed else None
        ),
    }


def check_equity_curve_integrity(equity_curve: pd.DataFrame) -> dict:
    if equity_curve.empty or "equity" not in equity_curve.columns:
        return {"passed": False, "warning": "Empty equity curve."}

    eq = equity_curve["equity"]
    if eq.isnull().any():
        return {"passed": False, "warning": "Equity curve contains NaN values."}

    if (eq <= 0).any():
        return {"passed": False, "warning": "Equity curve dropped to zero or below."}

    return {"passed": True, "warning": None}


def check_benchmark_coverage(aligned_benchmark_df: pd.DataFrame | None) -> dict:
    if aligned_benchmark_df is None or aligned_benchmark_df.empty:
        return {
            "passed": False,
            "benchmark_coverage_ratio": 0.0,
            "warning": "No benchmark data provided or aligned.",
        }

    if "equity" not in aligned_benchmark_df.columns:
        return {
            "passed": False,
            "benchmark_coverage_ratio": 0.0,
            "warning": "No equity column in aligned dataframe.",
        }

    total_len = len(aligned_benchmark_df)

    bench_cols = [c for c in aligned_benchmark_df.columns if c.startswith("bench_")]
    if not bench_cols:
        return {
            "passed": False,
            "benchmark_coverage_ratio": 0.0,
            "warning": "No valid benchmark columns found.",
        }

    valid_len = len(aligned_benchmark_df[bench_cols[0]].dropna())
    coverage = float(valid_len / total_len) if total_len > 0 else 0.0

    passed = coverage >= 0.9
    return {
        "passed": passed,
        "benchmark_coverage_ratio": coverage,
        "warning": f"Low benchmark coverage: {coverage:.2f}" if not passed else None,
    }


def check_metric_validity(metrics: dict) -> dict:
    invalid_count = 0
    warnings = []

    for k, v in metrics.items():
        if v is None:
            invalid_count += 1
            warnings.append(f"Metric {k} is None.")
        elif isinstance(v, float) and (np.isnan(v) or np.isinf(v)):
            invalid_count += 1
            warnings.append(f"Metric {k} is NaN or Inf.")

    return {
        "passed": invalid_count == 0,
        "invalid_metric_count": invalid_count,
        "warnings": warnings,
    }


def check_performance_report_warnings(summary: dict) -> dict:
    warnings = summary.get("warnings", [])
    return {"passed": len(warnings) == 0, "warning_count": len(warnings)}


def build_performance_quality_report(
    trades_df: pd.DataFrame,
    equity_curve: pd.DataFrame,
    metrics: dict,
    benchmark_summary: dict | None = None,
    min_trades: int = 5,
) -> dict:

    trade_check = check_minimum_trade_count(trades_df, min_trades)
    eq_check = check_equity_curve_integrity(equity_curve)
    metric_check = check_metric_validity(metrics)

    warnings = []
    if not trade_check["passed"]:
        warnings.append(trade_check["warning"])
    if not eq_check["passed"]:
        warnings.append(eq_check["warning"])
    if not metric_check["passed"]:
        warnings.extend(metric_check["warnings"])

    passed = trade_check["passed"] and eq_check["passed"] and metric_check["passed"]

    return {
        "passed": passed,
        "minimum_trade_count_passed": trade_check["passed"],
        "equity_curve_valid": eq_check["passed"],
        "invalid_metric_count": metric_check["invalid_metric_count"],
        "warning_count": len(warnings),
        "warnings": warnings,
    }
