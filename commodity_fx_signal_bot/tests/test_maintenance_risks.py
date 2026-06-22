import pytest
import pandas as pd
from local_maintenance.maintenance_config import get_default_local_maintenance_profile
from local_maintenance.maintenance_risks import build_maintenance_risk_summary, build_maintenance_risk_digest

def test_maintenance_risk_summary():
    profile = get_default_local_maintenance_profile()
    gap_df = pd.DataFrame([{"gap_type": "missing_operator_review_items", "description": "No operator tasks"}])

    df, summary = build_maintenance_risk_summary(gap_df, None, None, profile)

    assert not df.empty
    assert "sustainability_high_risk" in df["risk_level"].values
    assert "investment risk" in summary["disclaimer"].lower()

def test_maintenance_risk_digest():
    profile = get_default_local_maintenance_profile()
    gap_df = pd.DataFrame([{"gap_type": "missing_operator_review_items", "description": "No operator tasks"}])
    df, _ = build_maintenance_risk_summary(gap_df, None, None, profile)

    digest, summary = build_maintenance_risk_digest(df, profile)
    assert "Maintenance Risk Digest" in digest
    assert "investment risk" in digest.lower()
