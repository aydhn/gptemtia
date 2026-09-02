
import pandas as pd
from local_closure.closure_scoring import build_closure_readiness_score_report
from local_closure.closure_config import get_default_local_closure_profile

def test_scoring():
    p = get_default_local_closure_profile()
    df, summary = build_closure_readiness_score_report(pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), p)
    assert not df.empty
    assert 0 <= summary["score"] <= 1
