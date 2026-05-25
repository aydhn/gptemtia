import pytest
from command_center.interactive_query_flows import (
    build_symbol_query_flow,
    build_module_query_flow,
    build_warning_query_flow,
    build_project_question_flow,
    build_interactive_query_flow_report
)
from command_center.command_config import get_default_command_center_profile

def test_interactive_query_flows():
    profile = get_default_command_center_profile()

    flow1 = build_symbol_query_flow("GC=F", profile)
    assert flow1["flow_type"] == "symbol_query"
    assert "GC=F" in flow1["target"]

    flow2 = build_module_query_flow("backtest", profile)
    assert flow2["flow_type"] == "module_query"

    flow3 = build_warning_query_flow(profile)
    assert flow3["flow_type"] == "warning_query"

    flow4 = build_project_question_flow("How does this work?", profile)
    assert flow4["flow_type"] == "project_question"

def test_query_flow_report():
    profile = get_default_command_center_profile()
    flow = build_symbol_query_flow("GC=F", profile)
    df, summary = build_interactive_query_flow_report(flow)

    assert not df.empty
    assert summary["target"] == "GC=F"
