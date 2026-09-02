
import pandas as pd
from local_closure.closure_risks import build_closure_risk_summary
from local_closure.closure_config import get_default_local_closure_profile

def test_risks():
    p = get_default_local_closure_profile()
    df, summary = build_closure_risk_summary(pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), p)
    assert not df.empty
