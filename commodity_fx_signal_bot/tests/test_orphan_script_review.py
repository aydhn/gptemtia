
import pytest
import pandas as pd
from pathlib import Path
from commodity_fx_signal_bot.local_hardening.orphan_script_review import build_orphan_script_candidate_report
from commodity_fx_signal_bot.local_hardening.hardening_config import get_default_local_hardening_profile

def test_orphan_script():
    prof = get_default_local_hardening_profile()
    df, summary = build_orphan_script_candidate_report(Path("."), prof)
    assert isinstance(df, pd.DataFrame)
