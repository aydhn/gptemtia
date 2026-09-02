from pathlib import Path
from local_simplification.simplification_config import get_default_local_simplification_profile
from local_simplification.test_suite_simplification import build_test_suite_simplification_candidate_registry

def test_build_test_suite_simplification_candidate_registry():
    p = get_default_local_simplification_profile()
    df, summary = build_test_suite_simplification_candidate_registry(Path("."), p)
    assert df is not None
    assert len(summary["warnings"]) > 0
