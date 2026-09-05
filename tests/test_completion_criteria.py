from local_project_completion.completion_criteria import *
from local_project_completion.completion_config import get_default_local_project_completion_profile

def test_completion_criteria():
    prof = get_default_local_project_completion_profile()
    df, summary = build_project_completion_criteria_matrix(prof)
    assert not df.empty
