from local_readiness.readiness_config import get_default_local_readiness_profile
from local_readiness.stabilization_checklist import build_pre_handoff_stabilization_checklist

def test_stabilization_checklist():
    profile = get_default_local_readiness_profile()
    df, s = build_pre_handoff_stabilization_checklist(profile)
    assert not df.empty
