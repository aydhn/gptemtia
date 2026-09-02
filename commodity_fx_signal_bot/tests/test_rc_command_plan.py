
import pytest
import pandas as pd
from pathlib import Path
from commodity_fx_signal_bot.local_hardening.rc_command_plan import build_rc_dry_run_command_plan, classify_rc_command_safety
from commodity_fx_signal_bot.local_hardening.hardening_config import get_default_local_hardening_profile

def test_rc_command_plan():
    prof = get_default_local_hardening_profile()
    df, s = build_rc_dry_run_command_plan(prof)
    assert isinstance(df, pd.DataFrame)
