from pathlib import Path
from local_project_completion.completion_readiness_packet import *
from local_project_completion.completion_config import get_default_local_project_completion_profile

def test_completion_readiness_packet():
    prof = get_default_local_project_completion_profile()
    text, sum1 = build_project_completion_readiness_packet(Path("."), prof)
    assert "not production approval" in sum1["note"]
