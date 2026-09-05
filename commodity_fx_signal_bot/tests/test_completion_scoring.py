import pandas as pd
from local_project_completion.completion_scoring import *
from local_project_completion.completion_config import get_default_local_project_completion_profile

def test_completion_scoring():
    prof = get_default_local_project_completion_profile()
    df, summary = build_completion_readiness_score_report(pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), prof)
    assert not df.empty
    assert 0 <= summary["score"] <= 1
