
import pytest
import pandas as pd
from pathlib import Path
from local_hardening.path_health import build_final_path_health_report
from local_hardening.hardening_config import get_default_local_hardening_profile

def test_path_health():
    prof = get_default_local_hardening_profile()
    df, s = build_final_path_health_report(Path("."), prof)
    assert isinstance(df, pd.DataFrame)
