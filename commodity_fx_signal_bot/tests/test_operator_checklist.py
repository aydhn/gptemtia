from local_readiness.readiness_config import get_default_local_readiness_profile
from local_readiness.operator_checklist import build_final_operator_checklist, build_operator_first_run_checklist, build_safe_operator_command_sequence

def test_operator_checklists():
    profile = get_default_local_readiness_profile()
    df1, s1 = build_final_operator_checklist(profile)
    df2, s2 = build_operator_first_run_checklist(profile)
    df3, s3 = build_safe_operator_command_sequence(profile)

    assert not df1.empty
    assert not df2.empty
    assert not df3.empty
