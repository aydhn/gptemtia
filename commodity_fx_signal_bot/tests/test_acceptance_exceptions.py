import pandas as pd
from local_acceptance.acceptance_exceptions import build_acceptance_exception_register
from local_acceptance.acceptance_config import get_default_local_acceptance_profile

def test_build_acceptance_exception_register():
    p = get_default_local_acceptance_profile()
    df, s = build_acceptance_exception_register(pd.DataFrame(), pd.DataFrame(), p)
    assert df.empty
