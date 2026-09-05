from local_project_completion.completion_unresolved import *
from local_project_completion.completion_config import get_default_local_project_completion_profile

def test_completion_unresolved():
    prof = get_default_local_project_completion_profile()
    df, summary = build_project_completion_unresolved_register(prof)
    assert not df.empty
