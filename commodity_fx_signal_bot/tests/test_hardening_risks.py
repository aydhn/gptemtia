
import pytest
import pandas as pd
from pathlib import Path
from commodity_fx_signal_bot.local_hardening.hardening_risks import build_final_hardening_risk_summary
from commodity_fx_signal_bot.local_hardening.hardening_config import get_default_local_hardening_profile

def test_hardening_risks():
    prof = get_default_local_hardening_profile()
    df, s = build_final_hardening_risk_summary(pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), prof)
    assert isinstance(df, pd.DataFrame)
