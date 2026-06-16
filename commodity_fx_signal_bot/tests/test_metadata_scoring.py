import pandas as pd
import pytest
from artifact_metadata.metadata_scoring import calculate_metadata_completeness_score, calculate_metadata_freshness_score, classify_metadata_status
from artifact_metadata.metadata_config import get_default_artifact_metadata_profile
from datetime import datetime, timezone, timedelta

def test_calculate_metadata_completeness_score():
    df = pd.DataFrame([
        {"intended_use": "use", "non_use_policy": "pol", "limitations": ["l"]},
        {"intended_use": "", "non_use_policy": "pol", "limitations": ["l"]},
    ])
    score = calculate_metadata_completeness_score(df)
    assert score == 0.5

def test_calculate_metadata_freshness_score():
    now = datetime.now(timezone.utc)
    old = now - timedelta(days=100)
    recent = now - timedelta(days=10)

    df = pd.DataFrame([
        {"created_or_modified_at_utc": old.isoformat()},
        {"created_or_modified_at_utc": recent.isoformat()},
        {"created_or_modified_at_utc": None}
    ])

    profile = get_default_artifact_metadata_profile() # default warning is 45 days
    score = calculate_metadata_freshness_score(df, profile)
    # 1 out of 3 is fresh
    assert abs(score - 1/3) < 0.001

def test_classify_metadata_status():
    s1 = pd.Series({"intended_use": "a", "non_use_policy": "b"})
    assert classify_metadata_status(s1) == "metadata_complete"

    s2 = pd.Series({"intended_use": None, "non_use_policy": "b"})
    assert classify_metadata_status(s2) == "metadata_missing"
