import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from orchestration.workflow_templates import list_workflow_templates, get_workflow_template, validate_workflow_templates
from orchestration.job_registry import list_registered_jobs
import pytest

def test_workflow_templates():
    templates = list_workflow_templates()
    assert len(templates) > 0

    template = get_workflow_template("healthcheck_workflow")
    assert template is not None

    with pytest.raises(ValueError):
        get_workflow_template("unknown_workflow")

    jobs = list_registered_jobs()
    val = validate_workflow_templates(jobs)
    assert val["valid"]
