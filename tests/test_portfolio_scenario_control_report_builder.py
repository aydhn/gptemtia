# -*- coding: utf-8 -*-
from advanced_portfolio_scenario_control.portfolio_scenario_control_report_builder import (
    build_portfolio_scenario_control_markdown_report, SCENARIO_CONTROL_DISCLAIMER
)

def test_report_builder():
    summary = {"profile_name": "test_prof", "overall_score": 1.0}
    md = build_portfolio_scenario_control_markdown_report(summary)
    assert "Phase 156" in md
    assert SCENARIO_CONTROL_DISCLAIMER in md
