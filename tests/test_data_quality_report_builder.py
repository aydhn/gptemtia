import pytest
import pandas as pd
from unittest.mock import patch
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
    _df_to_markdown,
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


def test_df_to_markdown_exception_fallback():
    df = pd.DataFrame({"A": [1, 2], "B": ["x", "y"]})

    with patch("pandas.DataFrame.to_markdown", side_effect=Exception("Simulated error")):
        result = _df_to_markdown(df)

    expected_lines = [
        "| A | B |",
        "| --- | --- |",
        "| 1 | x |",
        "| 2 | y |"
    ]
    assert result == "\n".join(expected_lines)


def test_df_to_markdown_empty_or_none():
    assert _df_to_markdown(None) == ""
    assert _df_to_markdown(pd.DataFrame()) == ""
