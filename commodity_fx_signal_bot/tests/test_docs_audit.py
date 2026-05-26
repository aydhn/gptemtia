import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from devtools.docs_audit import check_required_docs, check_docs_nonempty, check_readme_sections, check_docs_for_forbidden_trade_language
from devtools.dev_config import get_default_dev_experience_profile

def test_docs_audit_checks(tmp_path):
    profile = get_default_dev_experience_profile()
    c1, _ = check_required_docs(tmp_path, profile)
    assert len(c1) > 0

    p = tmp_path / "README.md"
    p.touch()
    c2, _ = check_docs_nonempty(tmp_path, ("README.md",))
    assert len(c2) > 0
