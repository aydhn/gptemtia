
import pytest
import pandas as pd
from pathlib import Path
from commodity_fx_signal_bot.local_hardening.generated_docs_freeze import build_generated_docs_freeze_catalog
from commodity_fx_signal_bot.local_hardening.hardening_config import get_default_local_hardening_profile

def test_generated_docs_freeze():
    prof = get_default_local_hardening_profile()
    df, summary = build_generated_docs_freeze_catalog(Path("."), prof)
    assert isinstance(df, pd.DataFrame)
