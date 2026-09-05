"""Test models."""
from commodity_fx_signal_bot.local_documentation_export.export_models import DocumentationExportDomain, build_documentation_export_domain_id

def test_models():
    d_id = build_documentation_export_domain_id("test")
    assert len(d_id) > 0
