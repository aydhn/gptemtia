
import pandas as pd
from local_review_governance.review_scoring import build_review_readiness_score_report
from local_review_governance.review_config import get_default_local_review_governance_profile

def test_scoring():
    p = get_default_local_review_governance_profile()
    df, s = build_review_readiness_score_report(pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), p)
    assert not df.empty
