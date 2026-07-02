import pytest
import pandas as pd
from local_archive.archive_config import get_default_local_archive_profile
from local_archive.retention_policy import build_retention_policy_registry

def test_retention_policy_registry():
    profile = get_default_local_archive_profile()
    domain_df = pd.DataFrame([
        {"domain_id": "1", "domain_label": "documentation_archive"},
        {"domain_id": "2", "domain_label": "test_archive"}
    ])

    df, summary = build_retention_policy_registry(domain_df, profile)

    assert not df.empty
    assert "policy_id" in df.columns

    # Check assignment
    doc_pol = df[df["domain_label"] == "documentation_archive"]
    assert doc_pol.iloc[0]["retention_label"] == "retain_long_term_manual"

    test_pol = df[df["domain_label"] == "test_archive"]
    assert test_pol.iloc[0]["retention_label"] == "retain_short_term_manual"
