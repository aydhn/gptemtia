
import pytest
import pandas as pd
from pathlib import Path
from commodity_fx_signal_bot.local_hardening.dead_code_review import build_dead_code_candidate_report
from commodity_fx_signal_bot.local_hardening.hardening_config import get_default_local_hardening_profile

def test_dead_code():
    prof = get_default_local_hardening_profile()
    df, summary = build_dead_code_candidate_report(Path("."), prof)
    assert isinstance(df, pd.DataFrame)
