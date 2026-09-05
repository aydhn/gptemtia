
import pandas as pd
from local_review_governance.review_gaps import build_review_gap_register
from local_review_governance.review_config import get_default_local_review_governance_profile

def test_gaps():
    p = get_default_local_review_governance_profile()
    df, s = build_review_gap_register(pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), p)
    assert not df.empty
