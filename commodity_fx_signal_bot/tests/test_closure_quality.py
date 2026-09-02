
import pandas as pd
from local_closure.closure_quality import build_closure_quality_report, check_for_forbidden_terms_in_closure
from local_closure.closure_config import get_default_local_closure_profile

def test_qual():
    p = get_default_local_closure_profile()
    report = build_closure_quality_report({}, None, None, None)
    assert report["passed"]
    
    check = check_for_forbidden_terms_in_closure("live trading approved")
    assert not check["valid"]
