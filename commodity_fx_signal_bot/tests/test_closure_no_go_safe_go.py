
from pathlib import Path
from local_closure.closure_no_go_safe_go import build_closure_no_go_safe_go_summary
from local_closure.closure_config import get_default_local_closure_profile

def test_nogo():
    p = get_default_local_closure_profile()
    df, summary = build_closure_no_go_safe_go_summary(Path.cwd(), p)
    assert not df.empty
