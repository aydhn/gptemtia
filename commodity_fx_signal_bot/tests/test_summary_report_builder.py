import pandas as pd
from report_summarization.summary_report_builder import build_report_summary_registry_markdown_report, build_executive_summary_markdown_report

def test_build_report_summary_registry_markdown_report():
    summary = {"total_reports": 5}
    md = build_report_summary_registry_markdown_report(summary)
    assert "REPORT SUMMARY REGISTRY" in md
    assert "Canlı emir" in md # Disclaimer
    assert "Total Reports: 5" in md

def test_build_executive_summary_markdown_report():
    md = build_executive_summary_markdown_report({}, "EXECUTIVE TEST")
    assert "EXECUTIVE TEST" in md
    assert "Canlı emir" in md
