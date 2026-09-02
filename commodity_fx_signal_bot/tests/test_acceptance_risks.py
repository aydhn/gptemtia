import pandas as pd
from local_acceptance.acceptance_risks import build_acceptance_risk_summary
from local_acceptance.acceptance_config import get_default_local_acceptance_profile

def test_build_acceptance_risk_summary():
    p = get_default_local_acceptance_profile()
    df = pd.DataFrame()
    res, _ = build_acceptance_risk_summary(df, df, df, p)
    assert res.empty
