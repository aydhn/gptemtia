import pandas as pd
from local_simplification.simplification_config import get_default_local_simplification_profile
from local_simplification.simplification_scoring import build_maintainability_readiness_score_report

def test_scoring():
    p = get_default_local_simplification_profile()
    df, summary = build_maintainability_readiness_score_report(pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), p)
    assert not df.empty
