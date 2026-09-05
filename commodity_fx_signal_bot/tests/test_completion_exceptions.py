import pandas as pd
from local_project_completion.completion_exceptions import *
from local_project_completion.completion_config import get_default_local_project_completion_profile

def test_completion_exceptions():
    prof = get_default_local_project_completion_profile()
    df, summary = build_completion_exception_register(pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), prof)
    assert not df.empty
    assert "auto-fix yapmaz" in summary["note"]
