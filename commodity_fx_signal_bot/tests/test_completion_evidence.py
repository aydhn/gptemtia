from pathlib import Path
from local_project_completion.completion_evidence import *
from local_project_completion.completion_config import get_default_local_project_completion_profile

def test_completion_evidence():
    prof = get_default_local_project_completion_profile()
    df, summary = build_project_completion_evidence_map(Path("."), prof)
    assert not df.empty
    assert "not proof" in summary["note"]
