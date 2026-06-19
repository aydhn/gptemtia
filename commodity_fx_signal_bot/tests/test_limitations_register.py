from local_readiness.readiness_config import get_default_local_readiness_profile
from local_readiness.limitations_register import build_known_limitations_register
from config.paths import PROJECT_ROOT

def test_limitations_register():
    profile = get_default_local_readiness_profile()
    df, s = build_known_limitations_register(PROJECT_ROOT, profile)
    assert not df.empty
