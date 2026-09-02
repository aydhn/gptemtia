from pathlib import Path
from local_simplification.simplification_config import get_default_local_simplification_profile
from local_simplification.file_count_complexity import build_file_count_complexity_report

def test_build_file_count_complexity_report():
    p = get_default_local_simplification_profile()
    df, summary = build_file_count_complexity_report(Path("."), p)
    assert df is not None
    assert len(summary["warnings"]) > 0
