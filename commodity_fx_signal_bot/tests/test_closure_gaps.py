
import pandas as pd
from local_closure.closure_gaps import build_closure_gap_register
from local_closure.closure_config import get_default_local_closure_profile

def test_gaps():
    p = get_default_local_closure_profile()
    df, summary = build_closure_gap_register(pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), p)
    assert not df.empty
