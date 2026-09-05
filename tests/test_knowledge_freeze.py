from pathlib import Path
from local_project_completion.knowledge_freeze import *
from local_project_completion.completion_config import get_default_local_project_completion_profile

def test_knowledge_freeze():
    prof = get_default_local_project_completion_profile()
    df1, sum1 = build_knowledge_freeze_rehearsal_registry(Path("."), prof)
    df2, sum2 = build_knowledge_freeze_inventory(Path("."), prof)
    assert not df1.empty
    assert not df2.empty
    assert "not a git tag" in sum1["note"].lower()
