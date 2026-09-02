from local_acceptance.acceptance_report_builder import build_acceptance_domain_registry_markdown_report

def test_build_acceptance_domain_registry_markdown_report():
    md = build_acceptance_domain_registry_markdown_report({})
    assert "Acceptance Domain Registry" in md
