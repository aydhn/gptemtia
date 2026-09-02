
from local_closure.handoff_aftercare import build_closure_handoff_aftercare_guide
from local_closure.closure_config import get_default_local_closure_profile

def test_handoff():
    p = get_default_local_closure_profile()
    text, summary = build_closure_handoff_aftercare_guide(p)
    assert len(text) > 0


def test_dummy(): pass
