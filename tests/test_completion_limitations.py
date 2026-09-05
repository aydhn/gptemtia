from local_project_completion.completion_limitations import *
from local_project_completion.completion_config import get_default_local_project_completion_profile

def test_completion_limitations():
    prof = get_default_local_project_completion_profile()
    df, summary = build_project_completion_known_limitations_register(prof)
    assert not df.empty
