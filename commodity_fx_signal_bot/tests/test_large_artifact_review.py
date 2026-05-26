import pandas as pd
from maintenance.large_artifact_review import identify_large_artifacts, classify_large_artifact_action
from maintenance.maintenance_config import get_default_maintenance_profile

def test_large_artifact_review():
    profile = get_default_maintenance_profile()

    inv_data = [
        {"artifact_id": "1", "size_bytes": 200 * 1024 * 1024, "protected": True, "lifecycle_label": "active"},
        {"artifact_id": "2", "size_bytes": 200 * 1024 * 1024, "protected": False, "lifecycle_label": "cleanup_candidate"},
        {"artifact_id": "3", "size_bytes": 50 * 1024 * 1024, "protected": False, "lifecycle_label": "active"},
    ]
    inv_df = pd.DataFrame(inv_data)

    large = identify_large_artifacts(inv_df, 100)
    assert len(large) == 2

    assert classify_large_artifact_action(large.iloc[0], profile) == "review_required_action"
    assert classify_large_artifact_action(large.iloc[1], profile) == "cleanup_dry_run_action"
