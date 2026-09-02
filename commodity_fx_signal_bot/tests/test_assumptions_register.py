
from local_closure.assumptions_register import build_closure_assumptions_register
from local_closure.closure_config import get_default_local_closure_profile

def test_assump():
    p = get_default_local_closure_profile()
    df, summary = build_closure_assumptions_register(p)
    assert not df.empty
