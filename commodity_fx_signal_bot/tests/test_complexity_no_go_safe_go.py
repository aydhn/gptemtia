from local_simplification.simplification_config import get_default_local_simplification_profile
from local_simplification.complexity_no_go_safe_go import build_complexity_no_go_safe_go_summary

def test_no_go_safe_go():
    p = get_default_local_simplification_profile()
    df, summary = build_complexity_no_go_safe_go_summary(p)
    assert not df.empty
