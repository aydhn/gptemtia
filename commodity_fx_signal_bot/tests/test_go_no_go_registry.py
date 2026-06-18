from local_readiness.readiness_config import get_default_local_readiness_profile
from local_readiness.go_no_go_registry import build_no_go_condition_registry, build_safe_go_condition_registry

def test_go_no_go():
    profile = get_default_local_readiness_profile()
    no_go_df, s1 = build_no_go_condition_registry(profile)
    safe_go_df, s2 = build_safe_go_condition_registry(profile)
    assert not no_go_df.empty
    assert not safe_go_df.empty
