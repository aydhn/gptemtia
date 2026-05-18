import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from orchestration.job_registry import (
    list_registered_jobs,
    get_registered_job,
    validate_registered_jobs
)
import pytest

def test_job_registry():
    jobs = list_registered_jobs()
    assert len(jobs) > 0

    job = get_registered_job(jobs[0].job_id)
    assert job is not None

    validation = validate_registered_jobs()
    assert validation["valid"]

def test_job_registry_unknown():
    with pytest.raises(ValueError):
        get_registered_job("unknown_job_xyz")
