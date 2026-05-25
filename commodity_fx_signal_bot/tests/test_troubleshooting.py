import pytest
from command_center.troubleshooting import (
    build_common_issue_registry,
    map_issue_to_safe_commands,
    build_troubleshooting_plan,
    summarize_troubleshooting_plan
)
from command_center.command_registry import build_default_command_registry
from command_center.command_config import get_default_command_center_profile

def test_build_common_issue_registry():
    df = build_common_issue_registry()
    assert not df.empty
    assert "pytest failure" in df["issue"].values

def test_map_issue_to_safe_commands():
    profile = get_default_command_center_profile()
    commands = build_default_command_registry(profile)

    df = map_issue_to_safe_commands("status", commands)
    assert not df.empty

    # Check fallback to project_status_report
    df2 = map_issue_to_safe_commands("completely_unknown_issue_xyz", commands)
    assert not df2.empty
    assert "project_status_report" in df2["command_name"].values

def test_build_troubleshooting_plan():
    profile = get_default_command_center_profile()
    commands = build_default_command_registry(profile)

    plan_df, summary = build_troubleshooting_plan("missing report", commands, profile)
    assert not plan_df.empty
    assert summary["suggested_commands"] > 0

    # We should ensure no deploy/broker solutions are offered
    for cmd in plan_df["command"]:
        assert "deploy" not in cmd
        assert "broker" not in cmd
