
from local_closure.open_questions import build_closure_open_questions_register
from local_closure.closure_config import get_default_local_closure_profile

def test_open_q():
    p = get_default_local_closure_profile()
    df, summary = build_closure_open_questions_register(p)
    assert not df.empty
