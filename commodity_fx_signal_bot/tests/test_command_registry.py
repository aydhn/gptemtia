import pytest
from command_center.command_registry import (
    build_default_command_registry,
    command_registry_to_dataframe
)
from command_center.command_config import get_default_command_center_profile

def test_default_command_registry():
    profile = get_default_command_center_profile()
    commands = build_default_command_registry(profile)

    assert len(commands) > 0

    c_types = [c.command_type for c in commands]
    assert "status_command" in c_types
    assert "report_command" in c_types
    assert "query_command" in c_types

def test_command_registry_to_dataframe():
    profile = get_default_command_center_profile()
    commands = build_default_command_registry(profile)
    df = command_registry_to_dataframe(commands)

    assert not df.empty
    assert "command_id" in df.columns
    assert "safety_label" in df.columns

def test_safe_registry_no_unsafe_commands():
    profile = get_default_command_center_profile()
    commands = build_default_command_registry(profile)

    for cmd in commands:
        assert cmd.safety_label == "safe_offline_command"
        assert "live" not in cmd.command.lower() or "no live" in cmd.command.lower()
        assert "broker" not in cmd.command.lower()
        assert "deploy" not in cmd.command.lower()
