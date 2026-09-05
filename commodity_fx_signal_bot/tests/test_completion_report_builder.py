from local_project_completion.completion_report_builder import *

def test_report_builder():
    text = build_completion_domain_registry_markdown_report({})
    assert "Gerçek project closure" in text or "gerçek project closure" in text.lower()
