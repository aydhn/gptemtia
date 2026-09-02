import pytest
from pathlib import Path
from local_synthesis.end_state_capability_map import build_end_state_capability_map
from local_synthesis.synthesis_config import get_default_local_synthesis_profile

def test_build_end_state_capability_map():
    prof = get_default_local_synthesis_profile()
    df, summary = build_end_state_capability_map(Path("."), prof)
    assert not df.empty or summary["count"] == 0
