from local_training.training_config import get_default_local_training_profile
from local_training.onboarding_paths import build_role_based_onboarding_paths, build_operator_onboarding_path, build_analyst_onboarding_path, build_developer_onboarding_path

def test_onboarding_paths():
    prof = get_default_local_training_profile()
    df, sum = build_role_based_onboarding_paths(prof)
    assert not df.empty
    op = build_operator_onboarding_path(prof)
    assert op.role_label == "operator_role"
    an = build_analyst_onboarding_path(prof)
    assert an.role_label == "analyst_role"
    dev = build_developer_onboarding_path(prof)
    assert dev.role_label == "developer_role"
