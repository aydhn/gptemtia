
from pathlib import Path
from local_closure.meta_review import build_final_project_meta_review_report, build_meta_review_sections
from local_closure.closure_config import get_default_local_closure_profile

def test_meta_review():
    p = get_default_local_closure_profile()
    text, summary = build_final_project_meta_review_report(Path.cwd(), p)
    assert isinstance(text, str)
    assert len(text) > 0
    assert "UYARI" in text
    
    sections = build_meta_review_sections(Path.cwd(), p)
    assert len(sections) > 0
