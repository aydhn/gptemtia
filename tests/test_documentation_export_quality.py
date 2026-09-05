"""Test quality."""
from commodity_fx_signal_bot.local_documentation_export.documentation_export_quality import build_documentation_export_quality_report

def test_quality():
    rep = build_documentation_export_quality_report({})
    assert rep["passed"]
