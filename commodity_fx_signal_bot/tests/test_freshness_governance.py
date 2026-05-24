from datetime import datetime, timezone

import pandas as pd

from governance.freshness_governance import (
    build_freshness_governance_table,
    calculate_artifact_age_hours,
    classify_artifact_freshness,
)


def test_freshness():
    now = datetime.now(timezone.utc).isoformat()
    age = calculate_artifact_age_hours(now)
    assert age is not None and age < 1

    label = classify_artifact_freshness(age, "type")
    assert label == "fresh"

def test_build_table():
    now = datetime.now(timezone.utc).isoformat()
    inv_df = pd.DataFrame([{"artifact_id": "a1", "artifact_type": "type", "relative_path": "path", "modified_at_utc": now}])
    df = build_freshness_governance_table(inv_df)
    assert not df.empty
    assert df.iloc[0]["freshness"] == "fresh"
