from local_performance.datalake_retention import build_datalake_retention_rehearsal_guide
from local_performance.performance_config import get_default_local_performance_profile
from pathlib import Path

def test_datalake_retention():
    p = get_default_local_performance_profile()
    text, s = build_datalake_retention_rehearsal_guide(Path("."), p)
    assert isinstance(text, str)
