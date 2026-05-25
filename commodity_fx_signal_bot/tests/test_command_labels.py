import pytest
from command_center.command_labels import (
    list_command_type_labels,
    list_command_safety_labels,
    list_workflow_type_labels,
    list_runbook_type_labels,
    validate_command_type,
    validate_command_safety
)
from core.exceptions import ConfigError

def test_label_lists_not_empty():
    assert len(list_command_type_labels()) > 0
    assert len(list_command_safety_labels()) > 0
    assert len(list_workflow_type_labels()) > 0
    assert len(list_runbook_type_labels()) > 0

def test_validate_command_type():
    validate_command_type("status_command")
    with pytest.raises(ConfigError):
        validate_command_type("invalid_command_type")

def test_validate_command_safety():
    validate_command_safety("safe_offline_command")
    with pytest.raises(ConfigError):
        validate_command_safety("invalid_safety_label")

def test_safe_offline_command_name():
    # safe_offline_command canlı emir güvenliği olarak adlandırılmaz
    assert "safe_offline_command" in list_command_safety_labels()
    assert "live_safe" not in list_command_safety_labels()
