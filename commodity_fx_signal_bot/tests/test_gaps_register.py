from local_readiness.readiness_config import get_default_local_readiness_profile
from local_readiness.gaps_register import build_known_gaps_register
from config.paths import PROJECT_ROOT

def test_gaps_register():
    profile = get_default_local_readiness_profile()
    df, s = build_known_gaps_register(PROJECT_ROOT, profile)
    assert not df.empty
