
import pytest
import pandas as pd
from pathlib import Path
from commodity_fx_signal_bot.local_hardening.freeze_validation import build_final_freeze_validation_report, validate_no_release_or_destructive_claims
from commodity_fx_signal_bot.local_hardening.hardening_config import get_default_local_hardening_profile

def test_freeze_validation():
    prof = get_default_local_hardening_profile()
    df, s = build_final_freeze_validation_report({}, prof)
    assert isinstance(df, pd.DataFrame)
