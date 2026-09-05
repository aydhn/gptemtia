"""Test gaps."""
import pandas as pd
from commodity_fx_signal_bot.local_reproducibility_governance.reproducibility_gaps import build_reproducibility_gap_register
from commodity_fx_signal_bot.local_reproducibility_governance.reproducibility_config import get_default_local_reproducibility_governance_profile

def test_gaps():
    p = get_default_local_reproducibility_governance_profile()
    df, s = build_reproducibility_gap_register(pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), p)
    assert not df.empty
