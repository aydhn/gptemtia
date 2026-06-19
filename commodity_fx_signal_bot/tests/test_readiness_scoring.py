from local_readiness.readiness_config import get_default_local_readiness_profile
from local_readiness.readiness_scoring import build_readiness_score_report
import pandas as pd

def test_readiness_scoring():
    profile = get_default_local_readiness_profile()
    df, s = build_readiness_score_report(pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), profile)
    assert not df.empty
    assert df.iloc[0]["score"] == 1.0
