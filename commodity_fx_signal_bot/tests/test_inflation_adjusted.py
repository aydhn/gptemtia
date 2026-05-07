import pytest
import pandas as pd
from backtesting.inflation_adjusted import (
    align_equity_with_inflation,
    calculate_real_equity_curve,
    calculate_real_return_metrics,
    calculate_inflation_outperformance,
    build_inflation_adjusted_performance,
)


def test_align():
    idx = pd.date_range("2024-01-01", periods=5)
    eq = pd.DataFrame({"equity": [100, 110, 120, 130, 140]}, index=idx)
    macro = pd.DataFrame({"tr_cpi_index": [100, 102, 104, 106, 108]}, index=idx)

    aligned = align_equity_with_inflation(eq, macro)
    assert "tr_cpi_index" in aligned.columns


def test_real_curve():
    idx = pd.date_range("2024-01-01", periods=5)
    eq = pd.DataFrame({"equity": [100, 110, 120, 130, 140]}, index=idx)
    infl = pd.Series([100, 102, 104, 106, 108], index=idx)

    real_df = calculate_real_equity_curve(eq, infl)
    assert "real_equity" in real_df.columns


def test_real_metrics():
    idx = pd.date_range("2024-01-01", periods=5)
    real_df = pd.DataFrame({"real_equity": [100, 105, 110, 115, 120]}, index=idx)
    mets = calculate_real_return_metrics(real_df)
    assert "real_total_return" in mets


def test_build():
    idx = pd.date_range("2024-01-01", periods=5)
    eq = pd.DataFrame({"equity": [100, 110, 120, 130, 140]}, index=idx)
    macro = pd.DataFrame({"tr_cpi_index": [100, 102, 104, 106, 108]}, index=idx)

    df, summary = build_inflation_adjusted_performance(eq, macro)
    assert "nominal_total_return" in summary
    assert "real_total_return_tr_cpi" in summary
