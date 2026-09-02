import pytest
from pathlib import Path
from local_synthesis.project_closure_checklist import build_final_project_closure_checklist
from local_synthesis.synthesis_config import get_default_local_synthesis_profile

def test_build_final_project_closure_checklist():
    prof = get_default_local_synthesis_profile()
    df, summary = build_final_project_closure_checklist(Path("."), prof)
    assert not df.empty
