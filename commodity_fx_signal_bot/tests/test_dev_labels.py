import pytest
from devtools.dev_labels import (
    list_dx_status_labels, list_dx_category_labels, list_cli_command_group_labels,
    validate_dx_status, validate_dx_category, validate_cli_command_group,
    is_failed_dx_status
)

def test_lists_not_empty():
    assert len(list_dx_status_labels()) > 0
    assert len(list_dx_category_labels()) > 0
    assert len(list_cli_command_group_labels()) > 0

def test_validate_dx_status():
    validate_dx_status("dx_passed")
    with pytest.raises(ValueError):
        validate_dx_status("invalid")

def test_validate_cli_command_group():
    validate_cli_command_group("data")
    with pytest.raises(ValueError):
        validate_cli_command_group("invalid")

def test_is_failed_dx_status():
    assert is_failed_dx_status("dx_failed") is True
    assert is_failed_dx_status("dx_passed") is False
