"""Test report builder."""
from commodity_fx_signal_bot.local_reproducibility_governance.reproducibility_report_builder import build_reproducibility_domain_registry_markdown_report
def test_report_builder():
    text = build_reproducibility_domain_registry_markdown_report({})
    assert "build_free" not in text
