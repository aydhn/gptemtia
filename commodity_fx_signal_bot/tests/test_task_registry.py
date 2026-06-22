import pytest
from local_maintenance.maintenance_config import get_default_local_maintenance_profile
from local_maintenance.domain_registry import build_maintenance_domain_registry
from local_maintenance.task_registry import build_maintenance_task_registry, evaluate_maintenance_task_status

def test_maintenance_task_registry():
    profile = get_default_local_maintenance_profile()
    domain_df, _ = build_maintenance_domain_registry(profile)
    df, summary = build_maintenance_task_registry(domain_df, profile)

    assert not df.empty
    assert "task_id" in df.columns
    assert summary["total_tasks"] > 0

def test_evaluate_maintenance_task_status():
    profile = get_default_local_maintenance_profile()
    domain_df, _ = build_maintenance_domain_registry(profile)
    task_df, _ = build_maintenance_task_registry(domain_df, profile)

    eval_df, eval_sum = evaluate_maintenance_task_status(task_df, None, profile)
    assert not eval_df.empty
    assert "maintenance_due_soon" in eval_df["status"].values
