
import pytest
import pandas as pd
from pathlib import Path
from commodity_fx_signal_bot.local_hardening.duplicate_utility_review import build_duplicate_utility_candidate_report
from commodity_fx_signal_bot.local_hardening.hardening_config import get_default_local_hardening_profile

def test_duplicate_utility():
    prof = get_default_local_hardening_profile()
    df, summary = build_duplicate_utility_candidate_report(Path("."), prof)
    assert isinstance(df, pd.DataFrame)
