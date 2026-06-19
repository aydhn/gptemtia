from local_readiness.readiness_config import get_default_local_readiness_profile
from local_readiness.manual_review_register import build_manual_review_register
from config.paths import PROJECT_ROOT

def test_manual_review_register():
    profile = get_default_local_readiness_profile()
    df, s = build_manual_review_register(PROJECT_ROOT, None, None, profile)
    assert not df.empty
