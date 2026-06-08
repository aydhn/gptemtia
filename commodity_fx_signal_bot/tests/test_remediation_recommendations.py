
import pytest
import pandas as pd
from secrets_hygiene.remediation_recommendations import (
    map_finding_to_safe_recommendation,
    build_secret_remediation_recommendations,
    recommendations_to_dataframe
)
from secrets_hygiene.secrets_config import get_default_secrets_hygiene_profile

def test_map_finding_to_safe_recommendation():
    row = pd.Series({"finding_type": "api_key_finding", "severity": "high_secret_risk", "relative_path": "test.py"})
    rec = map_finding_to_safe_recommendation(row)
    assert not rec.destructive
    assert "rotate" in rec.safe_action.lower()

def test_build_secret_remediation_recommendations():
    df = pd.DataFrame([{"finding_type": "api_key_finding", "severity": "high_secret_risk", "relative_path": "test.py"}])
    profile = get_default_secrets_hygiene_profile()
    recs = build_secret_remediation_recommendations(df, None, profile)
    assert len(recs) == 1

def test_recommendations_dataframe():
    df = pd.DataFrame([{"finding_type": "api_key_finding", "severity": "high_secret_risk", "relative_path": "test.py"}])
    profile = get_default_secrets_hygiene_profile()
    recs = build_secret_remediation_recommendations(df, None, profile)
    df_recs = recommendations_to_dataframe(recs)
    assert not df_recs.empty
    assert "safe_action" in df_recs.columns
