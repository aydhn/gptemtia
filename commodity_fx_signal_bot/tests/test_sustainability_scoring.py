import pytest
import pandas as pd
from local_maintenance.maintenance_config import get_default_local_maintenance_profile
from local_maintenance.sustainability_scoring import build_sustainability_score_report

def test_sustainability_score():
    profile = get_default_local_maintenance_profile()
    gap_df = pd.DataFrame([{"gap_type": "missing_operator_review_items"}])
    risk_df = pd.DataFrame([{"risk_level": "sustainability_high_risk"}])

    df, summary = build_sustainability_score_report(None, gap_df, risk_df, profile)

    assert not df.empty
    val = df.iloc[0]["value"]
    assert 0.0 <= val <= 1.0
    assert "SLA" in summary["disclaimer"]
