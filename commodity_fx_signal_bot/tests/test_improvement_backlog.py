
import pandas as pd
from local_closure.improvement_backlog import build_closure_future_improvement_backlog
from local_closure.closure_config import get_default_local_closure_profile

def test_improv():
    p = get_default_local_closure_profile()
    df, summary = build_closure_future_improvement_backlog(pd.DataFrame(), pd.DataFrame(), p)
    assert not df.empty
