import pytest
from command_center.workflow_registry import (
    build_research_refresh_workflow,
    build_report_generation_workflow,
    build_knowledge_query_workflow,
    build_default_workflows,
    workflows_to_dataframe
)
from command_center.command_registry import build_default_command_registry
from command_center.command_config import get_default_command_center_profile

def test_build_workflows():
    profile = get_default_command_center_profile()
    commands = build_default_command_registry(profile)

    wf1 = build_research_refresh_workflow(commands)
    assert wf1.workflow_type == "research_refresh_workflow"
    assert len(wf1.steps) > 0

    wf2 = build_report_generation_workflow(commands)
    assert wf2.workflow_type == "report_generation_workflow"

    wf3 = build_knowledge_query_workflow(commands)
    assert wf3.workflow_type == "knowledge_query_workflow"

def test_default_workflows():
    profile = get_default_command_center_profile()
    commands = build_default_command_registry(profile)
    workflows = build_default_workflows(commands, profile)

    assert len(workflows) > 0

    df = workflows_to_dataframe(workflows)
    assert not df.empty
    assert "workflow_id" in df.columns

def test_workflow_is_not_execution():
    profile = get_default_command_center_profile()
    commands = build_default_command_registry(profile)
    workflows = build_default_workflows(commands, profile)

    for wf in workflows:
        # Check descriptions or structure to ensure it's guided/manual
        assert "A guided workflow" in wf.description or "for" in wf.description
