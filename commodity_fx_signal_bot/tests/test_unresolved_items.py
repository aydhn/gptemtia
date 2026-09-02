
from pathlib import Path
from local_closure.unresolved_items import build_closure_unresolved_items_register
from local_closure.closure_config import get_default_local_closure_profile

def test_unresolved():
    p = get_default_local_closure_profile()
    df, summary = build_closure_unresolved_items_register(Path.cwd(), p)
    assert not df.empty
    assert summary["total"] > 0
