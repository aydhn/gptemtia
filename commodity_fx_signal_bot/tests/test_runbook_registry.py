import pytest
from command_center.runbook_registry import (
    build_safe_start_runbook,
    build_daily_research_runbook,
    build_troubleshooting_runbook,
    build_default_runbooks,
    runbooks_to_dataframe
)
from command_center.command_registry import build_default_command_registry
from command_center.workflow_registry import build_default_workflows
from command_center.command_config import get_default_command_center_profile

def test_build_runbooks():
    profile = get_default_command_center_profile()
    commands = build_default_command_registry(profile)
    workflows = build_default_workflows(commands, profile)

    rb1 = build_safe_start_runbook(commands, workflows)
    assert rb1.runbook_type == "safe_start_runbook"
    assert "Safety Limits" in [s["title"] for s in rb1.sections]

    rb2 = build_daily_research_runbook(commands, workflows)
    assert rb2.runbook_type == "daily_research_runbook"

    rb3 = build_troubleshooting_runbook(commands, workflows)
    assert rb3.runbook_type == "troubleshooting_runbook"

def test_default_runbooks():
    profile = get_default_command_center_profile()
    commands = build_default_command_registry(profile)
    workflows = build_default_workflows(commands, profile)
    runbooks = build_default_runbooks(commands, workflows, profile)

    assert len(runbooks) > 0
    df = runbooks_to_dataframe(runbooks)
    assert not df.empty

def test_runbook_no_investment_advice():
    profile = get_default_command_center_profile()
    commands = build_default_command_registry(profile)
    workflows = build_default_workflows(commands, profile)
    runbooks = build_default_runbooks(commands, workflows, profile)

    for rb in runbooks:
        # Validate that safety notes or descriptions don't imply trading
        assert "trade" not in rb.description.lower() or "offline" in rb.description.lower()
        for note in rb.safety_notes:
            assert "live" not in note.lower()
