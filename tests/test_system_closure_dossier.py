from pathlib import Path
from local_project_completion.system_closure_dossier import *
from local_project_completion.completion_config import get_default_local_project_completion_profile

def test_system_closure_dossier():
    prof = get_default_local_project_completion_profile()
    text, summary = build_final_local_system_closure_dossier(Path("."), prof)
    assert "Not a real project closure" in summary["note"]
    assert "Gerçek project closure" in text or "gerçek project closure" in text.lower()
