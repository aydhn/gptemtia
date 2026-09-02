import pandas as pd
from local_simplification.simplification_config import get_default_local_simplification_profile
from local_simplification.simplification_risks import build_simplification_risk_summary

def test_risks():
    p = get_default_local_simplification_profile()
    df, summary = build_simplification_risk_summary(pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), p)
    assert not df.empty
