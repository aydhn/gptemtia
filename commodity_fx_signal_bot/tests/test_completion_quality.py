from local_project_completion.completion_quality import *
from local_project_completion.completion_config import get_default_local_project_completion_profile

def test_completion_quality():
    prof = get_default_local_project_completion_profile()
    q = build_completion_quality_report({})
    assert q["passed"] is True
    
    check = check_for_forbidden_terms_in_completion("gerçek project closure değildir.")
    assert check["passed"] is True
