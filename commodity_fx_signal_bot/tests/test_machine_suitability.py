from local_performance.machine_suitability import build_local_machine_suitability_checklist
from local_performance.performance_config import get_default_local_performance_profile
from pathlib import Path

def test_machine_suitability():
    p = get_default_local_performance_profile()
    df, s = build_local_machine_suitability_checklist(Path("."), p)
    assert not df.empty
