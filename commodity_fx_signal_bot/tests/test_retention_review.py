import pytest
import pandas as pd
from local_archive.archive_config import get_default_local_archive_profile
from local_archive.retention_review import build_retention_review_checklist

def test_retention_review_checklist():
    profile = get_default_local_archive_profile()
    item_df = pd.DataFrame([
        {"item_id": "1", "item_status": "archive_candidate", "domain_label": "documentation_archive"}
    ])
    policy_df = pd.DataFrame([
        {"domain_label": "documentation_archive", "review_interval_days": 180, "retention_label": "retain_long_term_manual"}
    ])

    df, summary = build_retention_review_checklist(policy_df, item_df, profile)

    assert not df.empty
    assert "task" in df.columns
    assert "status" in df.columns
