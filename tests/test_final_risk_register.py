from local_project_completion.final_risk_register import *
from local_project_completion.completion_config import get_default_local_project_completion_profile

def test_final_risk_register():
    prof = get_default_local_project_completion_profile()
    df, summary = build_project_completion_final_risk_register(prof)
    assert not df.empty
    assert "not an investment risk" in summary["note"].lower()
