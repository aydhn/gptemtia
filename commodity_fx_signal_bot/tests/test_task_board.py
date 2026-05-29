import pytest
from pathlib import Path
from analyst_ux.ux_config import get_default_analyst_ux_profile
from analyst_ux.task_board import (
    build_default_analyst_tasks, build_tasks_from_quality_reports,
    analyst_tasks_to_dataframe
)

def test_task_board():
    profile = get_default_analyst_ux_profile()
    tasks = build_default_analyst_tasks(profile)

    assert len(tasks) > 0
    df = analyst_tasks_to_dataframe(tasks)
    assert not df.empty

    root = Path(__file__).parent.parent
    q_tasks = build_tasks_from_quality_reports(root, profile)
    assert len(q_tasks) == 0 # mock returns empty

    # Check warning
    for task in tasks:
        assert "gerçek trading task board değildir" in task.warnings[0]
