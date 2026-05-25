import pytest
from command_center.command_models import (
    SafeCommand,
    GuidedWorkflow,
    SafeRunbook,
    CommandDryRunPlan,
    build_safe_command_id,
    build_workflow_id,
    build_runbook_id,
    safe_command_to_dict,
    sanitize_command_text
)

def test_build_safe_command_id():
    cid1 = build_safe_command_id("Test Command", "module_a")
    cid2 = build_safe_command_id("test_command", "module_a")
    assert cid1 == "cmd_module_a_test_command"
    assert cid2 == "cmd_module_a_test_command"

def test_build_workflow_id():
    wid = build_workflow_id("Test Workflow", "workflow_type")
    assert wid == "wf_workflow_type_test_workflow"

def test_build_runbook_id():
    rid = build_runbook_id("Test Runbook", "runbook_type")
    assert rid == "rb_runbook_type_test_runbook"

def test_safe_command_to_dict():
    cmd = SafeCommand(
        command_id="test_id",
        command_name="test",
        command_type="status_command",
        safety_label="safe_offline_command",
        command="echo 1",
        description="A test",
        module_name="test_mod",
        dry_run_supported=True,
        requires_arguments=False,
        example_arguments={},
        output_paths=[],
        warnings=[]
    )
    d = safe_command_to_dict(cmd)
    assert d["command_id"] == "test_id"
    assert "command_name" in d

def test_sanitize_command_text():
    raw = "python  script.py\n--arg val"
    sanitized = sanitize_command_text(raw)
    assert "\n" not in sanitized
