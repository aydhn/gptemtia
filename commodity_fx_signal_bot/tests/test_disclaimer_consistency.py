import pytest
from pathlib import Path
from local_consistency.consistency_config import get_default_local_consistency_profile
from local_consistency.disclaimer_consistency import build_disclaimer_consistency_report

def test_build_disclaimer_consistency_report():
    profile = get_default_local_consistency_profile()
    df, summary = build_disclaimer_consistency_report(Path("."), profile)
    assert df is not None
