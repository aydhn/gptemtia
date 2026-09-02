import pytest
from pathlib import Path
from local_synthesis.navigation_guides import build_final_operator_navigation_guide, build_navigation_index
from local_synthesis.synthesis_config import get_default_local_synthesis_profile

def test_navigation_guides():
    prof = get_default_local_synthesis_profile()
    text, summary = build_final_operator_navigation_guide(Path("."), prof)
    assert isinstance(text, str)
    df, summary = build_navigation_index(Path("."), prof)
    assert df.empty or not df.empty
