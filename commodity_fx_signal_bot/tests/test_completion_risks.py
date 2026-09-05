import pandas as pd
from local_project_completion.completion_risks import *
from local_project_completion.completion_config import get_default_local_project_completion_profile

def test_completion_risks():
    prof = get_default_local_project_completion_profile()
    df, summary = build_completion_risk_summary(pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), prof)
    assert not df.empty
    assert "yatırım riski değildir" in summary["note"]
