import pytest
from pathlib import Path
from final_review.consolidation_audit import build_phase_1_55_consolidation_audit
from final_review.final_review_config import get_default_final_review_profile

@pytest.fixture
def project_root():
    return Path(__file__).resolve().parent.parent

def test_build_phase_1_55_consolidation_audit(project_root):
    profile = get_default_final_review_profile()
    dfs, summary = build_phase_1_55_consolidation_audit(project_root, profile)
    assert "matrix" in dfs
    assert "passed" in summary
