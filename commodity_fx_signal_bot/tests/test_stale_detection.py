import pandas as pd
from maintenance.stale_detection import detect_stale_artifacts, classify_staleness
from maintenance.maintenance_config import get_default_maintenance_profile

def test_stale_detection():
    profile = get_default_maintenance_profile()

    assert classify_staleness(5, "any", profile) == "fresh"
    assert classify_staleness(20, "any", profile) == "aging"
    assert classify_staleness(40, "any", profile) == "stale"
    assert classify_staleness(100, "any", profile) == "very_stale"

    inv_data = [
        {"artifact_id": "1", "retention_category": "raw", "age_days": 100},
        {"artifact_id": "2", "retention_category": "raw", "age_days": 5},
    ]
    inv_df = pd.DataFrame(inv_data)

    stale = detect_stale_artifacts(inv_df, profile)
    assert len(stale) == 1
    assert stale.iloc[0]["artifact_id"] == "1"
