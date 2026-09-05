from local_project_completion.final_recaps import *
from local_project_completion.completion_config import get_default_local_project_completion_profile

def test_final_recaps():
    prof = get_default_local_project_completion_profile()
    t1, s1 = build_final_safe_usage_recap(prof)
    assert "not official" in s1["note"]
