from pathlib import Path
from local_simplification.simplification_config import get_default_local_simplification_profile
from local_simplification.config_simplification import build_config_simplification_candidate_registry

def test_build_config_simplification_candidate_registry():
    p = get_default_local_simplification_profile()
    df, summary = build_config_simplification_candidate_registry(Path("."), p)
    assert df is not None
    assert len(summary["warnings"]) > 0
