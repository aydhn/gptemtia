
import pytest
import pandas as pd
from pathlib import Path
from commodity_fx_signal_bot.local_hardening.rc_boundary_checklist import build_rc_non_use_boundary_checklist
from commodity_fx_signal_bot.local_hardening.hardening_config import get_default_local_hardening_profile

def test_rc_boundary_checklist():
    prof = get_default_local_hardening_profile()
    df, s = build_rc_non_use_boundary_checklist(prof)
    assert isinstance(df, pd.DataFrame)
