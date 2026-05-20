import pytest
import pandas as pd
from research_reports.report_quality import (
    check_research_snapshot_quality,
    check_research_report_markdown,
    check_ranking_table_quality,
    check_for_forbidden_trade_terms_in_research,
    build_research_quality_report,
    _check_text_for_forbidden_terms
)
from research_reports.research_models import SymbolResearchSnapshot, ResearchReport

def test_check_text_for_forbidden_terms():
    assert "AL" in _check_text_for_forbidden_terms("Bu bir AL sinyalidir.")
    assert "BUY" in _check_text_for_forbidden_terms("Strong BUY setup.")
    assert not _check_text_for_forbidden_terms("Alışılagelmiş bir durum.") # Boundary test, although simplistic string match might fail if ' AL ' is matched against ' ALIŞ '. Our implementation uses " AL ", so " Alış " wouldn't match.

def test_check_research_snapshot_quality():
    snap = SymbolResearchSnapshot("AAPL", "1d", "stock", "2023", {}, {}, {}, {}, {}, {}, {}, {}, 0.05, "ready", [])
    q = check_research_snapshot_quality(snap)
    assert q["passed"] is False
    assert len(q["warnings"]) > 0

def test_check_research_report_markdown():
    q = check_research_report_markdown("")
    assert q["passed"] is False
    assert not q["markdown_not_empty"]

    q2 = check_research_report_markdown("Test report. Bu rapor offline araştırma/simülasyon çıktısıdır; gerçek emir, canlı sinyal veya yatırım tavsiyesi değildir.")
    assert q2["passed"] is True

    q3 = check_research_report_markdown("Bu bir AL sinyalidir. offline araştırma")
    assert q3["passed"] is False
    assert q3["forbidden_trade_terms_found"] is True

def test_check_ranking_table_quality():
    q = check_ranking_table_quality(pd.DataFrame())
    assert q["passed"] is False

    q2 = check_ranking_table_quality(pd.DataFrame({"A": [1]}))
    assert q2["passed"] is True

def test_build_research_quality_report():
    rep = ResearchReport("id", "type", "title", "prof", "1d", [], "date", "Valid report. offline araştırma/simülasyon", {}, {}, [])
    q = build_research_quality_report(rep, [], pd.DataFrame({"A": [1]}))
    assert q["passed"] is True

    rep_bad = ResearchReport("id", "type", "title", "prof", "1d", [], "date", "AL sinyali.", {}, {}, [])
    q_bad = build_research_quality_report(rep_bad, [], pd.DataFrame())
    assert q_bad["passed"] is False
