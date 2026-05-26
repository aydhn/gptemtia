import pandas as pd
from maintenance.rotation_planner import build_report_rotation_plan, summarize_rotation_plans
from maintenance.maintenance_config import get_default_maintenance_profile

def test_rotation_planner():
    profile = get_default_maintenance_profile()
    profile = profile.__class__(**{**profile.__dict__, "keep_latest_n_reports": 2})

    inv_data = [
        {"artifact_id": "1", "path": "a", "retention_category": "report_retention", "age_days": 1},
        {"artifact_id": "2", "path": "b", "retention_category": "report_retention", "age_days": 2},
        {"artifact_id": "3", "path": "c", "retention_category": "report_retention", "age_days": 3},
    ]
    inv_df = pd.DataFrame(inv_data)

    plan_df, summary = build_report_rotation_plan(inv_df, profile)
    assert len(plan_df) == 3
    # First 2 should be keep_action, 3rd should be rotate
    assert len(plan_df[plan_df["action"] == "keep_action"]) == 2
    assert len(plan_df[plan_df["action"] == "rotate_dry_run_action"]) == 1

    sums = summarize_rotation_plans({"reports": plan_df})
    assert sums["reports"] == 3
