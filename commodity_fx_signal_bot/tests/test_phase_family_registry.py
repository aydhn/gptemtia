import pytest
from local_synthesis.phase_family_registry import build_phase_family_registry
from local_synthesis.synthesis_config import get_default_local_synthesis_profile

def test_build_phase_family_registry():
    prof = get_default_local_synthesis_profile()
    df, summary = build_phase_family_registry(prof)
    assert not df.empty
    assert "count" in summary


def test_dummy(): pass
