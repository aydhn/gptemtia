import pytest
from pathlib import Path
from local_consistency.consistency_config import get_default_local_consistency_profile
from local_consistency.safety_boundary_consistency import build_safety_boundary_consistency_report

def test_build_safety_boundary_consistency_report():
    profile = get_default_local_consistency_profile()
    df, summary = build_safety_boundary_consistency_report(Path("."), profile)
    assert df is not None
