from local_project_completion.completion_no_go_safe_go import *
from local_project_completion.completion_config import get_default_local_project_completion_profile

def test_completion_no_go_safe_go():
    prof = get_default_local_project_completion_profile()
    df, summary = build_completion_no_go_safe_go_summary(prof)
    assert not df.empty
