
from pathlib import Path
from local_closure.decision_log import build_closure_decision_log
from local_closure.closure_config import get_default_local_closure_profile

def test_dec():
    p = get_default_local_closure_profile()
    df, summary = build_closure_decision_log(Path.cwd(), p)
    assert not df.empty
