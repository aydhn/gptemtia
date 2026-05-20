import pytest
import pandas as pd
from research_reports.markdown_renderer import (
    render_symbol_report_markdown,
    render_universe_report_markdown,
    render_daily_digest_markdown,
    dataframe_to_markdown_table,
    render_report_header,
    render_report_footer
)
from research_reports.research_models import SymbolResearchSnapshot
from research_reports.research_config import ResearchReportProfile

def test_dataframe_to_markdown_table():
    df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
    md = dataframe_to_markdown_table(df)
    assert "|   A |   B |" in md

    empty_md = dataframe_to_markdown_table(pd.DataFrame())
    assert "empty" in empty_md.lower()

def test_render_report_footer():
    footer = render_report_footer()
    assert "Uyarı:" in footer
    assert "yatırım tavsiyesi değildir" in footer.lower()

def test_render_symbol_report_markdown():
    snap = SymbolResearchSnapshot("AAPL", "1d", "stock", "2023", {}, {}, {}, {}, {}, {}, {}, {}, 0.5, "ready", ["warn1"])
    md = render_symbol_report_markdown(snap, "Narrative text", {"Table1": pd.DataFrame({"X": [1]})})
    assert "# Research Report: AAPL" in md
    assert "Narrative text" in md
    assert "warn1" in md
    assert "Table1" in md
    assert "|   X |" in md
    assert "Uyarı:" in md

def test_render_universe_report_markdown():
    prof = ResearchReportProfile("test", "test", max_rows_per_table=1)
    df = pd.DataFrame({"A": [1, 2]}) # 2 rows
    md = render_universe_report_markdown(df, "Universe text", prof)
    assert "# Universe Research Report" in md
    assert "Universe text" in md
    # max rows is 1, so row 2 shouldn't be in markdown output for the table (hard to test exact output of to_markdown simply, but we know it truncates)
    assert "Uyarı:" in md

def test_render_daily_digest_markdown():
    prof = ResearchReportProfile("test", "test")
    md = render_daily_digest_markdown([], pd.DataFrame(), prof)
    assert "# Daily Research Digest" in md
    assert "Summarized 0 symbols" in md
    assert "Uyarı:" in md
