
import pandas as pd
from local_review_governance.review_exceptions import build_review_exception_register
from local_review_governance.review_config import get_default_local_review_governance_profile

def test_exceptions():
    p = get_default_local_review_governance_profile()
    df, s = build_review_exception_register(pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), p)
    assert not df.empty
