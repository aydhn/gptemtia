"""Test risks."""
import pandas as pd
from commodity_fx_signal_bot.local_reproducibility_governance.reproducibility_risks import build_reproducibility_risk_summary
from commodity_fx_signal_bot.local_reproducibility_governance.reproducibility_config import get_default_local_reproducibility_governance_profile

def test_risks():
    p = get_default_local_reproducibility_governance_profile()
    df, s = build_reproducibility_risk_summary(pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), p)
    assert not df.empty
