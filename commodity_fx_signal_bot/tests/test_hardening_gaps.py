
import pytest
import pandas as pd
from pathlib import Path
from commodity_fx_signal_bot.local_hardening.hardening_gaps import build_final_hardening_gap_register
from commodity_fx_signal_bot.local_hardening.hardening_config import get_default_local_hardening_profile

def test_hardening_gaps():
    prof = get_default_local_hardening_profile()
    df, s = build_final_hardening_gap_register(pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), prof)
    assert isinstance(df, pd.DataFrame)
