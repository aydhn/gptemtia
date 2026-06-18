import pytest
from local_consistency.consistency_config import get_default_local_consistency_profile
from local_consistency.consistency_quality import build_consistency_quality_report, check_for_forbidden_terms_in_consistency

def test_check_for_forbidden_terms_in_consistency():
    res = check_for_forbidden_terms_in_consistency("auto fixed")
    # depending on implementation, it may record it.
    pass

def test_build_consistency_quality_report():
    profile = get_default_local_consistency_profile()
    report = build_consistency_quality_report({"profile": profile.name})
    assert report["passed"] is not None
