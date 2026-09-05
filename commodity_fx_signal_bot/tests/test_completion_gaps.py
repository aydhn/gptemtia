import pandas as pd
from local_project_completion.completion_gaps import *
from local_project_completion.completion_config import get_default_local_project_completion_profile

def test_completion_gaps():
    prof = get_default_local_project_completion_profile()
    df, summary = build_completion_gap_register(pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), prof)
    assert not df.empty
