import pytest
from pathlib import Path
from final_review.safety_audit import build_safety_audit_report, _FALSE_POSITIVES
from final_review.final_review_config import get_default_final_review_profile

@pytest.fixture
def project_root():
    return Path(__file__).resolve().parent.parent

def test_build_safety_audit_report(project_root):
    profile = get_default_final_review_profile()
    df, summary = build_safety_audit_report(project_root, profile)
    assert "passed" in summary
    assert "critical_issues" in summary

def test_false_positives():
    assert "yatırım tavsiyesi değildir" in _FALSE_POSITIVES
