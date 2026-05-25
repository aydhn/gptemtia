import pytest
from command_center.command_safety import (
    detect_forbidden_command_terms,
    classify_command_safety,
    validate_safe_command,
    filter_safe_commands
)
from command_center.command_models import SafeCommand

def test_detect_forbidden_command_terms():
    res1 = detect_forbidden_command_terms("python -m scripts.run_live_trading")
    assert res1["forbidden_terms_found"] is True
    assert "live" in res1["found_terms"]

    res2 = detect_forbidden_command_terms("python -m scripts.run_project_status_report")
    assert res2["forbidden_terms_found"] is False

def test_classify_command_safety():
    assert classify_command_safety("python -m status") == "safe_offline_command"
    assert classify_command_safety("python deploy.py") == "blocked_deploy_command"
    assert classify_command_safety("python live_broker.py") == "blocked_live_command"

def test_validate_safe_command():
    safe_cmd = SafeCommand("id1", "status", "status_command", "safe_offline_command", "echo 1", "", "", True, False, {}, [], [])
    res = validate_safe_command(safe_cmd)
    assert res["valid"] is True

    unsafe_cmd = SafeCommand("id2", "live", "status_command", "safe_offline_command", "live order", "", "", True, False, {}, [], [])
    res2 = validate_safe_command(unsafe_cmd)
    assert res2["valid"] is False

def test_filter_safe_commands():
    cmd1 = SafeCommand("id1", "status", "status_command", "safe_offline_command", "echo 1", "", "", True, False, {}, [], [])
    cmd2 = SafeCommand("id2", "live", "status_command", "safe_offline_command", "live order", "", "", True, False, {}, [], [])

    safe, blocked = filter_safe_commands([cmd1, cmd2])
    assert len(safe) == 1
    assert len(blocked) == 1
    assert safe[0].command_id == "id1"
