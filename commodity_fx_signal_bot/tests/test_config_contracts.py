
import pytest
import pandas as pd
from pathlib import Path
from commodity_fx_signal_bot.local_hardening.config_contracts import build_config_settings_contract_catalog
from commodity_fx_signal_bot.local_hardening.hardening_config import get_default_local_hardening_profile

def test_config_contracts():
    prof = get_default_local_hardening_profile()
    df, summary = build_config_settings_contract_catalog(Path("."), prof)
    assert isinstance(df, pd.DataFrame)
