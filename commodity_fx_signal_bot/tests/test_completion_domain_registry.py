from local_project_completion.completion_domain_registry import *
from local_project_completion.completion_config import get_default_local_project_completion_profile

def test_domain_registry():
    prof = get_default_local_project_completion_profile()
    df, summary = build_completion_domain_registry(prof)
    assert not df.empty
    assert "note" in summary
