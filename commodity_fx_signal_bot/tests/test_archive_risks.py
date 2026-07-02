import pytest
import pandas as pd
from local_archive.archive_config import get_default_local_archive_profile
from local_archive.archive_risks import build_archive_risk_summary

def test_archive_risks():
    profile = get_default_local_archive_profile()
    gap_df = pd.DataFrame([{"gap_type": "missing_domain", "description": "test"}])
    bound_df = pd.DataFrame()
    ver_df = pd.DataFrame([{"relative_path": ".env"}])

    df, summary = build_archive_risk_summary(gap_df, bound_df, ver_df, profile)

    assert not df.empty
    risks = df["risk_type"].tolist()
    assert "secret_mismatch" in risks
    assert "missing_domain" in risks

    levels = df["risk_level"].tolist()
    assert "archive_critical_risk" in levels
    assert "archive_medium_risk" in levels
