
from local_closure.limitations_register import build_closure_known_limitations_register
from local_closure.closure_config import get_default_local_closure_profile

def test_lim():
    p = get_default_local_closure_profile()
    df, summary = build_closure_known_limitations_register(p)
    assert not df.empty
