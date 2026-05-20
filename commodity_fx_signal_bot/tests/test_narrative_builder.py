import pytest
from research_reports.narrative_builder import (
    build_symbol_narrative,
    build_technical_narrative,
    build_risk_level_narrative,
    build_backtest_narrative,
    build_performance_narrative,
    build_validation_narrative,
    build_ml_narrative,
    build_paper_narrative,
    build_quality_narrative,
    build_universe_narrative,
    build_disclaimer_text
)
from research_reports.research_models import SymbolResearchSnapshot
from research_reports.research_config import ResearchReportProfile

def test_build_disclaimer_text():
    text = build_disclaimer_text()
    assert "offline" in text.lower()
    assert "yatırım tavsiyesi" in text.lower()
    assert "canlı sinyal" in text.lower()
    assert "gerçek emir" in text.lower()

def test_section_narratives():
    assert "Teknik özet bulunmamaktadır" in build_technical_narrative({})
    assert "Risk seviye özeti bulunmamaktadır" in build_risk_level_narrative({})
    assert "Backtest özeti bulunmamaktadır" in build_backtest_narrative({})
    assert "Performans özeti bulunmamaktadır" in build_performance_narrative({})
    assert "Doğrulama özeti bulunmamaktadır" in build_validation_narrative({})
    assert "ML özeti bulunmamaktadır" in build_ml_narrative({})
    assert "Paper özeti bulunmamaktadır" in build_paper_narrative({})
    assert "Kalite özeti bulunmamaktadır" in build_quality_narrative({})

    # Test valid
    assert "supportive_context" in build_technical_narrative({"strongest_signal_context": "supportive_context"})
    assert "10 risk adayı" in build_risk_level_narrative({"risk_candidate_count": 10})

def test_build_symbol_narrative():
    prof = ResearchReportProfile("test", "test", include_technical_summary=True, include_paper_summary=False)
    snap = SymbolResearchSnapshot("AAPL", "1d", "stock", "2023", {"strongest_signal_context": "supportive_context"}, {}, {}, {}, {}, {}, {}, {}, 0.5, "ready", [])
    text = build_symbol_narrative(snap, prof)
    assert "AAPL için Araştırma Özeti" in text
    assert "supportive_context" in text
    assert "Paper özeti" not in text

def test_build_universe_narrative():
    text = build_universe_narrative({"total_symbols_ranked": 10, "top_symbol": "AAPL"})
    assert "10 sembol" in text
    assert "AAPL" in text

def test_no_forbidden_terms_generated():
    text = build_symbol_narrative(SymbolResearchSnapshot("AAPL", "1d", "stock", "2023", {}, {}, {}, {}, {}, {}, {}, {}, 0.5, "ready", []), ResearchReportProfile("test", "test"))
    text_upper = text.upper()
    assert " SAT " not in f" {text_upper} "
    assert " BUY " not in f" {text_upper} "
