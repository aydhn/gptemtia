from pathlib import Path
from local_simplification.simplification_config import get_default_local_simplification_profile
from local_simplification.repo_ergonomics import build_repo_ergonomics_rehearsal_guide

def test_build_repo_ergonomics():
    p = get_default_local_simplification_profile()
    text, summary = build_repo_ergonomics_rehearsal_guide(Path("."), p)
    assert len(text) > 0
    assert len(summary["warnings"]) > 0
