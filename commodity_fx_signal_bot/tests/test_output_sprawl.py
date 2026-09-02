from pathlib import Path
from local_simplification.simplification_config import get_default_local_simplification_profile
from local_simplification.output_sprawl import build_report_output_sprawl_report

def test_build_report_output_sprawl_report():
    p = get_default_local_simplification_profile()
    df, summary = build_report_output_sprawl_report(Path("."), p)
    assert df is not None
    assert len(summary["warnings"]) > 0
