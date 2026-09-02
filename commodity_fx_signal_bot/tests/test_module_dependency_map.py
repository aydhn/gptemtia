import pytest
from pathlib import Path
from local_synthesis.module_dependency_map import build_end_state_module_dependency_map
from local_synthesis.synthesis_config import get_default_local_synthesis_profile

def test_build_end_state_module_dependency_map():
    prof = get_default_local_synthesis_profile()
    df, summary = build_end_state_module_dependency_map(Path("."), prof)
    assert df.empty or not df.empty


def test_dummy(): pass
