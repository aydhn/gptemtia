from local_simplification.simplification_report_builder import build_simplification_domain_registry_markdown_report

def test_report_builder():
    res = build_simplification_domain_registry_markdown_report({})
    assert "gercek refactor" in res or "gerçek refactor" in res or "offline/local" in res
