from pathlib import Path
from local_simplification.simplification_config import get_default_local_simplification_profile
from local_simplification.duplicate_pattern_candidates import build_duplicate_pattern_consolidation_candidate_registry

def test_build_duplicate_pattern_consolidation_candidate_registry():
    p = get_default_local_simplification_profile()
    df, summary = build_duplicate_pattern_consolidation_candidate_registry(Path("."), p)
    assert df is not None
    assert len(summary["warnings"]) > 0
