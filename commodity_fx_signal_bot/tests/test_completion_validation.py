import pandas as pd
from local_project_completion.completion_validation import *
from local_project_completion.completion_config import get_default_local_project_completion_profile

def test_completion_validation():
    prof = get_default_local_project_completion_profile()
    df, sum1 = build_completion_validation_report({}, prof)
    assert not df.empty
