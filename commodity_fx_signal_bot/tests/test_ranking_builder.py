import pytest
import pandas as pd
from research_reports.ranking_builder import (
    build_symbol_ranking_table,
    build_asset_class_ranking_tables,
    build_ranking_summary
)
from research_reports.research_models import SymbolResearchSnapshot
from research_reports.research_config import ResearchReportProfile

def get_dummy_snapshots():
    s1 = SymbolResearchSnapshot("AAPL", "1d", "stock", "2023", {}, {}, {}, {}, {}, {}, {}, {"missing_sources_count": 0}, 0.8, "ready", [])
    s2 = SymbolResearchSnapshot("MSFT", "1d", "stock", "2023", {}, {}, {}, {}, {}, {}, {}, {"missing_sources_count": 1}, 0.6, "warning", ["w1"])
    s3 = SymbolResearchSnapshot("GC=F", "1d", "metal", "2023", {}, {}, {}, {}, {}, {}, {}, {"missing_sources_count": 0}, 0.9, "ready", [])
    return [s1, s2, s3]

def test_build_symbol_ranking_table():
    prof = ResearchReportProfile("test", "test")
    snapshots = get_dummy_snapshots()
    df = build_symbol_ranking_table(snapshots, prof)

    assert not df.empty
    assert "rank" in df.columns
    assert "symbol" in df.columns

    # Top rank should be GC=F (0.9)
    assert df.iloc[0]["symbol"] == "GC=F"
    assert df.iloc[0]["rank"] == 1

    # Check warning count mapping
    msft_row = df[df["symbol"] == "MSFT"].iloc[0]
    assert msft_row["warning_count"] == 1
    assert msft_row["missing_sources_count"] == 1

def test_empty_ranking_table():
    prof = ResearchReportProfile("test", "test")
    df = build_symbol_ranking_table([], prof)
    assert df.empty

def test_build_asset_class_ranking_tables():
    prof = ResearchReportProfile("test", "test")
    df = build_symbol_ranking_table(get_dummy_snapshots(), prof)
    tables = build_asset_class_ranking_tables(df)

    assert "stock" in tables
    assert "metal" in tables
    assert len(tables["stock"]) == 2
    assert len(tables["metal"]) == 1

def test_build_ranking_summary():
    prof = ResearchReportProfile("test", "test")
    df = build_symbol_ranking_table(get_dummy_snapshots(), prof)
    summary = build_ranking_summary(df)

    assert summary["total_symbols_ranked"] == 3
    assert summary["top_symbol"] == "GC=F"
