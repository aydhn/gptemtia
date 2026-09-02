from pathlib import Path
from local_simplification.simplification_config import get_default_local_simplification_profile
from local_simplification.script_cli_simplification import build_script_cli_simplification_candidate_registry

def test_build_script_cli_simplification_candidate_registry():
    p = get_default_local_simplification_profile()
    df, summary = build_script_cli_simplification_candidate_registry(Path("."), p)
    assert df is not None
    assert len(summary["warnings"]) > 0
