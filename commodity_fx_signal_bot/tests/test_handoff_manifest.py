from local_readiness.readiness_config import get_default_local_readiness_profile
from local_readiness.handoff_manifest import build_handoff_package_manifest
from config.paths import PROJECT_ROOT

def test_handoff_manifest():
    profile = get_default_local_readiness_profile()
    m, s = build_handoff_package_manifest(PROJECT_ROOT, 1.0, {}, profile)
    assert m["readiness_score"] == 1.0
    assert m["local_only"] is True
