
import pytest
import pandas as pd
from commodity_fx_signal_bot.local_hardening.hardening_domain_registry import build_hardening_domain_registry, build_default_hardening_domains
from commodity_fx_signal_bot.local_hardening.hardening_config import get_default_local_hardening_profile

def test_domain_registry():
    prof = get_default_local_hardening_profile()
    assert len(build_default_hardening_domains(prof)) > 0
    df, summary = build_hardening_domain_registry(prof)
    assert isinstance(df, pd.DataFrame)
