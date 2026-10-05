
import pytest
import pandas as pd
from pathlib import Path
from local_hardening.naming_convention import build_final_naming_convention_report
from local_hardening.hardening_config import get_default_local_hardening_profile

def test_naming_convention():
    prof = get_default_local_hardening_profile()
    df, s = build_final_naming_convention_report(Path("."), prof)
    assert isinstance(df, pd.DataFrame)
