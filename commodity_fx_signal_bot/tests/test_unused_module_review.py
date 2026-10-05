
import pytest
import pandas as pd
from pathlib import Path
from local_hardening.unused_module_review import build_unused_module_candidate_report
from local_hardening.hardening_config import get_default_local_hardening_profile

def test_unused_module():
    prof = get_default_local_hardening_profile()
    df, summary = build_unused_module_candidate_report(Path("."), prof)
    assert isinstance(df, pd.DataFrame)
