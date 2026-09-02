
from pathlib import Path
from local_closure.closure_recaps import build_closure_executive_recap, summarize_closure_recaps
from local_closure.closure_config import get_default_local_closure_profile

def test_recaps():
    p = get_default_local_closure_profile()
    text, summary = build_closure_executive_recap(Path.cwd(), p)
    assert len(text) > 0
    assert summarize_closure_recaps({"ex": text})["ex"] == len(text)
