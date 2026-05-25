import pytest
import pandas as pd
from command_center.command_report_builder import (
    build_command_catalog_markdown_report,
    build_guided_workflow_markdown_report,
    build_safe_runbook_markdown_report,
    build_project_status_markdown_report,
    build_project_consolidation_markdown_report,
    build_analyst_command_query_markdown_report,
    build_command_center_disclaimer
)

def test_disclaimer_presence():
    df = pd.DataFrame([{"A": 1}])
    summary = {"Total": 1}

    md1 = build_command_catalog_markdown_report(summary, df)
    assert "DISCLAIMER" in md1

    md2 = build_guided_workflow_markdown_report(summary, df)
    assert "DISCLAIMER" in md2

    md3 = build_project_consolidation_markdown_report(summary, df)
    assert "DISCLAIMER" in md3

    md4 = build_analyst_command_query_markdown_report(summary, df)
    assert "DISCLAIMER" in md4

def test_disclaimer_content():
    disc = build_command_center_disclaimer()
    assert "gerçek emir" in disc.lower()
    assert "canlı sinyal" in disc.lower()
