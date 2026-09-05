"""Test report builder."""
from commodity_fx_signal_bot.local_documentation_export.documentation_export_report_builder import build_documentation_export_domain_registry_markdown_report

def test_report_builder():
    txt = build_documentation_export_domain_registry_markdown_report({})
    assert "Gerçek static site deployment" in txt
