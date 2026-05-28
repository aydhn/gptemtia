import pytest
from pathlib import Path
from final_review.readiness_audit import build_readiness_audit_report
from final_review.final_review_config import get_default_final_review_profile

@pytest.fixture
def project_root():
    return Path(__file__).resolve().parent.parent

def test_build_readiness_audit_report(project_root):
    profile = get_default_final_review_profile()
    df, summary = build_readiness_audit_report(project_root, profile)
    assert not df.empty
    assert "passed" in summary
