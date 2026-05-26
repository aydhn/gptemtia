import pandas as pd
from maintenance.cleanup_planner import identify_cleanup_candidates, build_cleanup_dry_run_plan
from maintenance.maintenance_config import get_default_maintenance_profile

def test_cleanup_planner():
    profile = get_default_maintenance_profile()

    inv_data = [{
        "artifact_id": "1", "path": "a", "lifecycle_label": "cleanup_candidate",
        "protected": False, "size_bytes": 100, "age_days": 100
    }, {
        "artifact_id": "2", "path": "b", "lifecycle_label": "cleanup_candidate",
        "protected": True, "size_bytes": 100, "age_days": 100
    }]
    inv_df = pd.DataFrame(inv_data)

    candidates = identify_cleanup_candidates(inv_df, pd.DataFrame(), profile)
    assert len(candidates) == 1
    assert candidates.iloc[0]["artifact_id"] == "1"

    plan_df, summary = build_cleanup_dry_run_plan(candidates, profile)
    assert summary["candidate_count"] == 1
    assert summary["reclaimable_bytes"] == 100
    assert plan_df.iloc[0]["action_label"] == "cleanup_dry_run_action"
