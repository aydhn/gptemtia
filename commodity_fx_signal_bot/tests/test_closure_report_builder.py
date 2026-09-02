
from local_closure.closure_report_builder import build_closure_domain_registry_markdown_report

def test_report_builder():
    md = build_closure_domain_registry_markdown_report({}, None)
    assert "UYARI" in md
