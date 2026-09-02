
import pytest
import pandas as pd
from pathlib import Path
from commodity_fx_signal_bot.local_hardening.contract_surface_registry import build_contract_surface_registry
from commodity_fx_signal_bot.local_hardening.hardening_config import get_default_local_hardening_profile

def test_contract_surface():
    prof = get_default_local_hardening_profile()
    df, summary = build_contract_surface_registry(Path("."), prof)
    assert isinstance(df, pd.DataFrame)
