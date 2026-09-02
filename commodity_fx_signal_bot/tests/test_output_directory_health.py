
import pytest
import pandas as pd
from pathlib import Path
from commodity_fx_signal_bot.local_hardening.output_directory_health import build_final_output_directory_health_report
from commodity_fx_signal_bot.local_hardening.hardening_config import get_default_local_hardening_profile

def test_output_directory_health():
    prof = get_default_local_hardening_profile()
    df, s = build_final_output_directory_health_report(Path("."), prof)
    assert isinstance(df, pd.DataFrame)
