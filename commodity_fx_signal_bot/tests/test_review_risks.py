
import pandas as pd
from local_review_governance.review_risks import build_review_risk_summary
from local_review_governance.review_config import get_default_local_review_governance_profile

def test_risks():
    p = get_default_local_review_governance_profile()
    df, s = build_review_risk_summary(pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), p)
    assert not df.empty
