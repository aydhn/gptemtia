
from pathlib import Path
from local_closure.governance_rehearsal import build_post_project_governance_rehearsal_guide, build_governance_rehearsal_sections
from local_closure.closure_config import get_default_local_closure_profile

def test_governance():
    p = get_default_local_closure_profile()
    text, summary = build_post_project_governance_rehearsal_guide(Path.cwd(), p)
    assert isinstance(text, str)
    assert "UYARI" in text
    assert len(build_governance_rehearsal_sections(p)) > 0
