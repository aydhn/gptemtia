import pandas as pd
from maintenance.archive_strategy import identify_archive_candidates, build_archive_manifest, build_archive_plan
from maintenance.maintenance_config import get_default_maintenance_profile

def test_archive_strategy():
    profile = get_default_maintenance_profile()

    inv_data = [{
        "artifact_id": "1", "path": "a", "lifecycle_label": "archive_candidate",
        "protected": False, "size_bytes": 100, "age_days": 100
    }, {
        "artifact_id": "2", "path": "b", "lifecycle_label": "archive_candidate",
        "protected": True, "size_bytes": 100, "age_days": 100
    }]
    inv_df = pd.DataFrame(inv_data)

    candidates = identify_archive_candidates(inv_df, pd.DataFrame(), profile)
    assert len(candidates) == 1
    assert candidates.iloc[0]["artifact_id"] == "1"

    manifest = build_archive_manifest(candidates, profile)
    assert manifest.candidate_count == 1
    assert manifest.dry_run is True

    plan_df, summary = build_archive_plan(candidates, profile)
    assert summary["candidate_count"] == 1
