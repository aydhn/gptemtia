
import pytest
import pandas as pd
from pathlib import Path
from local_hardening.safety_hardening import build_final_safety_hardening_report
from local_hardening.hardening_config import get_default_local_hardening_profile

def test_safety_hardening():
    prof = get_default_local_hardening_profile()
    df, s = build_final_safety_hardening_report(Path("."), prof)
    assert isinstance(df, pd.DataFrame)


def test_dummy(): pass
