from local_project_completion.final_handoff_checklists import *
from local_project_completion.completion_config import get_default_local_project_completion_profile

def test_final_handoff_checklists():
    prof = get_default_local_project_completion_profile()
    df1, sum1 = build_final_operator_handoff_checklist(prof)
    assert not df1.empty
    assert "not real sign-off" in sum1["note"]
