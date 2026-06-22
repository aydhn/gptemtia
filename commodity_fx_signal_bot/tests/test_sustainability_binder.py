import pytest
import pandas as pd
from local_maintenance.maintenance_config import get_default_local_maintenance_profile
from local_maintenance.sustainability_binder import build_long_term_sustainability_binder

def test_sustainability_binder():
    profile = get_default_local_maintenance_profile()
    score_df = pd.DataFrame([{"value": 0.8, "classification": "Good"}])

    text, summary = build_long_term_sustainability_binder(None, None, None, score_df, None, profile)

    assert "Long-Term Sustainability Binder" in text
    assert "0.8" in text
    assert "sla" in text.lower()
