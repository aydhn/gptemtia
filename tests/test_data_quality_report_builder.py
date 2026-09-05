import pytest
import pandas as pd
from advanced_data_quality.data_quality_report_builder import (
    build_data_quality_disclaimer,
    build_data_quality_profile_markdown_report,
    build_quality_rule_registry_markdown_report,
    build_quality_findings_markdown_report,
    build_manual_review_queue_markdown_report,
    build_provider_quality_score_markdown_report,
    build_dataset_quality_score_markdown_report,
    build_data_quality_health_markdown_report,
    build_data_quality_validation_markdown_report,
    build_data_quality_safety_markdown_report,
    build_phase_113_handoff_markdown_report,
)


def test_data_quality_report_builder():
    disc = build_data_quality_disclaimer()
    assert "Phase 112" in disc
    assert "Canlı emir" in disc
    assert "destructive auto-cleaning" in disc

    rep_prof = build_data_quality_profile_markdown_report({})
    assert "# Data Quality Profile Registry Report" in rep_prof

    rep_rules = build_quality_rule_registry_markdown_report({})
    assert "# Quality Rule Registry Report" in rep_rules

    rep_find = build_quality_findings_markdown_report({})
    assert "# Quality Findings Registry Report" in rep_find

    rep_handoff = build_phase_113_handoff_markdown_report({})
    assert "# Phase 113 Normalization Handoff Report" in rep_handoff
