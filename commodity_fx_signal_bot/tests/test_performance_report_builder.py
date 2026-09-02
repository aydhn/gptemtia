from local_performance.performance_report_builder import build_performance_domain_registry_markdown_report

def test_performance_report_builder():
    txt = build_performance_domain_registry_markdown_report({})
    assert "benchmark" in txt
