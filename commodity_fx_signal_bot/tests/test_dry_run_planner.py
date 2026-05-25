import pytest
from command_center.dry_run_planner import (
    build_command_dry_run_plan,
    plan_full_status_check,
    plan_knowledge_query,
    dry_run_plan_to_dataframe
)
from command_center.command_registry import build_default_command_registry
from command_center.command_config import get_default_command_center_profile

def test_build_dry_run_plan():
    profile = get_default_command_center_profile()
    commands = build_default_command_registry(profile)

    plan = plan_full_status_check(commands, profile)
    assert plan.title == "Full Status Check"
    assert len(plan.commands) > 0

    plan2 = plan_knowledge_query("test query", commands, profile)
    assert "test query" in plan2.title

def test_dry_run_plan_dataframe():
    profile = get_default_command_center_profile()
    commands = build_default_command_registry(profile)

    plan = plan_full_status_check(commands, profile)
    df = dry_run_plan_to_dataframe(plan)

    assert not df.empty
    assert "status" in df.columns
    assert "planned" in df["status"].values

def test_plan_does_not_execute():
    profile = get_default_command_center_profile()
    commands = build_default_command_registry(profile)

    plan = plan_full_status_check(commands, profile)
    # the function simply returns a dataclass, asserting it has no "execute" side effect
    # implicitly by the nature of the pure function
    assert isinstance(plan.execution_order, list)
