from local_training.training_config import get_default_local_training_profile
from local_training.training_quality import build_training_quality_report, check_for_forbidden_terms_in_training

def test_quality():
    prof = get_default_local_training_profile()
    q = build_training_quality_report({})
    assert q["passed"]
    f = check_for_forbidden_terms_in_training("live order")
    assert not f["is_safe"]
