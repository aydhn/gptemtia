from local_readiness.readiness_config import get_default_local_readiness_profile
from local_readiness.readiness_validation import build_readiness_validation_report

def test_readiness_validation():
    profile = get_default_local_readiness_profile()
    df, s = build_readiness_validation_report({}, profile)
    assert not df.empty
