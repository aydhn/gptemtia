import pandas as pd
from local_acceptance.acceptance_gaps import build_acceptance_gap_register
from local_acceptance.acceptance_config import get_default_local_acceptance_profile

def test_build_acceptance_gap_register():
    p = get_default_local_acceptance_profile()
    df = pd.DataFrame()
    res, _ = build_acceptance_gap_register(df, df, df, df, p)
    assert res.empty
