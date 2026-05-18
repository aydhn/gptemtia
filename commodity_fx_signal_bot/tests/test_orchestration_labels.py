import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from orchestration.orchestration_labels import (
    list_job_status_labels,
    list_workflow_status_labels,
    list_dependency_status_labels,
    list_job_type_labels,
    validate_job_status,
    is_terminal_job_status,
    is_failed_job_status
)
import pytest

def test_label_lists_not_empty():
    assert len(list_job_status_labels()) > 0
    assert len(list_workflow_status_labels()) > 0
    assert len(list_dependency_status_labels()) > 0
    assert len(list_job_type_labels()) > 0

def test_validate_job_status():
    validate_job_status("job_success")
    with pytest.raises(ValueError):
        validate_job_status("invalid_status")

def test_is_terminal_job_status():
    assert is_terminal_job_status("job_success") is True
    assert is_terminal_job_status("job_running") is False

def test_is_failed_job_status():
    assert is_failed_job_status("job_failed") is True
    assert is_failed_job_status("job_blocked") is True
    assert is_failed_job_status("job_success") is False
