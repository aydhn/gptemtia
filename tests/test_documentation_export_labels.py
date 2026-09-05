"""Test labels."""
from commodity_fx_signal_bot.local_documentation_export.export_labels import list_documentation_export_domain_labels, validate_documentation_export_domain_label

def test_labels():
    labels = list_documentation_export_domain_labels()
    assert "static_site_export_domain" in labels
    validate_documentation_export_domain_label("static_site_export_domain")
