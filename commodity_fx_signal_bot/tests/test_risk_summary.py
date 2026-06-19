from local_readiness.readiness_config import get_default_local_readiness_profile
from local_readiness.risk_summary import build_pre_handoff_risk_summary
import pandas as pd

def test_risk_summary():
    profile = get_default_local_readiness_profile()
    df, s = build_pre_handoff_risk_summary(pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), profile)
    assert not df.empty
