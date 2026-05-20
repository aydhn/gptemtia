import pytest
import pandas as pd
from research_reports.symbol_summary import (
    build_latest_price_summary,
    build_symbol_identity_summary,
    calculate_symbol_research_score,
    build_symbol_research_snapshot
)
from config.symbols import SymbolSpec
from research_reports.research_config import ResearchReportProfile

def test_build_latest_price_summary():
    df = pd.DataFrame({"close": [10.0, 11.0], "volume": [100, 200]}, index=pd.date_range("2023-01-01", periods=2))
    summary = build_latest_price_summary({"ohlcv": df})
    assert summary["latest_close"] == 11.0
    assert summary["volume_available"] is True

    empty_summary = build_latest_price_summary({"ohlcv": pd.DataFrame()})
    assert empty_summary["latest_close"] is None

def test_build_symbol_identity_summary():
    spec = SymbolSpec("AAPL", "Apple", "equities", "stock", "USD")
    summary = build_symbol_identity_summary(spec, {})
    assert summary["symbol"] == "AAPL"
    assert summary["asset_class"] == "equities"

def test_calculate_symbol_research_score():
    score = calculate_symbol_research_score({"technical_summary": {"strongest_signal_context": "supportive_context"}})
    assert 0.0 <= score <= 1.0

def test_insufficient_data_status():
    spec = SymbolSpec("AAPL", "Apple", "equities", "stock", "USD")
    prof = ResearchReportProfile("test", "desc")
    snap = build_symbol_research_snapshot(spec, "1d", {}, {"data_available": False}, prof)
    assert snap.research_status == "research_report_insufficient_data"
