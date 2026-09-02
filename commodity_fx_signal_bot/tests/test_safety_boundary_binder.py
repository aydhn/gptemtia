import pytest
from local_synthesis.safety_boundary_binder import build_final_safety_boundary_binder
from local_synthesis.synthesis_config import get_default_local_synthesis_profile

def test_build_final_safety_boundary_binder():
    prof = get_default_local_synthesis_profile()
    text, summary = build_final_safety_boundary_binder(prof)
    assert isinstance(text, str)


def test_dummy(): pass
