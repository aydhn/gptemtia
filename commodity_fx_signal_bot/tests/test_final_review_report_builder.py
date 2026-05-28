import pytest
import pandas as pd
from final_review.final_review_report_builder import (
    build_final_system_review_markdown_report, build_architecture_audit_markdown_report,
    build_safety_audit_markdown_report, build_offline_acceptance_markdown_report,
    build_release_readiness_dry_run_markdown_report, build_final_consolidation_markdown_report
)

def test_markdown_reports():
    assert "DISCLAIMER" in build_final_system_review_markdown_report({})
    assert "DISCLAIMER" in build_architecture_audit_markdown_report({})
    assert "DISCLAIMER" in build_safety_audit_markdown_report({})
    assert "DISCLAIMER" in build_offline_acceptance_markdown_report({})
    assert "DISCLAIMER" in build_release_readiness_dry_run_markdown_report({})
    assert "DISCLAIMER" in build_final_consolidation_markdown_report({})
