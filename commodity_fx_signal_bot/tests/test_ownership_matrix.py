
from local_closure.ownership_matrix import build_closure_ownership_matrix_rehearsal
from local_closure.closure_config import get_default_local_closure_profile

def test_own():
    p = get_default_local_closure_profile()
    df, summary = build_closure_ownership_matrix_rehearsal(p)
    assert not df.empty
