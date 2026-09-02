import pandas as pd
from local_acceptance.acceptance_scoring import build_acceptance_readiness_score_report
from local_acceptance.acceptance_config import get_default_local_acceptance_profile

def test_build_acceptance_readiness_score_report():
    p = get_default_local_acceptance_profile()
    df = pd.DataFrame()
    res, s = build_acceptance_readiness_score_report(df, df, df, p)
    assert not res.empty
    assert s["score"] > 0
