from local_performance.report_rotation import build_report_rotation_rehearsal_guide
from local_performance.performance_config import get_default_local_performance_profile
from pathlib import Path

def test_report_rotation():
    p = get_default_local_performance_profile()
    text, s = build_report_rotation_rehearsal_guide(Path("."), p)
    assert isinstance(text, str)
