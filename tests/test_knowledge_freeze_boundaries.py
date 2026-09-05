from local_project_completion.knowledge_freeze_boundaries import *
from local_project_completion.completion_config import get_default_local_project_completion_profile

def test_knowledge_freeze_boundaries():
    prof = get_default_local_project_completion_profile()
    df, sum1 = build_knowledge_freeze_boundary_registry(prof)
    assert not df.empty
    assert sum1["boundaries"] > 0
