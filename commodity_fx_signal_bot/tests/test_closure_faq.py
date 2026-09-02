
from local_closure.closure_faq import build_closure_faq
from local_closure.closure_config import get_default_local_closure_profile

def test_faq():
    p = get_default_local_closure_profile()
    df, summary = build_closure_faq(p)
    assert not df.empty
