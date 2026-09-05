from local_project_completion.terminal_maps import *
from local_project_completion.completion_config import get_default_local_project_completion_profile

def test_terminal_maps():
    prof = get_default_local_project_completion_profile()
    t1, s1 = build_terminal_readme_map(prof)
    assert "Manual review" in s1["note"]
