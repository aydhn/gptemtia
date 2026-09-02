import pandas as pd
from local_simplification.simplification_config import get_default_local_simplification_profile
from local_simplification.simplification_gaps import build_simplification_gap_register

def test_gaps():
    p = get_default_local_simplification_profile()
    df, summary = build_simplification_gap_register(pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), p)
    assert not df.empty
