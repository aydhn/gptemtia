import pytest
from pathlib import Path
from local_synthesis.no_go_safe_go_summary import build_final_no_go_safe_go_summary
from local_synthesis.synthesis_config import get_default_local_synthesis_profile

def test_build_final_no_go_safe_go_summary():
    prof = get_default_local_synthesis_profile()
    df, summary = build_final_no_go_safe_go_summary(Path("."), prof)
    assert not df.empty
