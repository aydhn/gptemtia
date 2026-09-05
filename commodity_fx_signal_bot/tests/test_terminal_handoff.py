from local_project_completion.terminal_handoff import *
from local_project_completion.completion_config import get_default_local_project_completion_profile

def test_terminal_handoff():
    prof = get_default_local_project_completion_profile()
    text, summary = build_terminal_handoff_pack(prof)
    assert "not official acceptance" in summary["note"]
