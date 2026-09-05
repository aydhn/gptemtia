"""Test scoring."""
import pandas as pd
from commodity_fx_signal_bot.local_reproducibility_governance.reproducibility_scoring import build_reproducibility_readiness_score_report
from commodity_fx_signal_bot.local_reproducibility_governance.reproducibility_config import get_default_local_reproducibility_governance_profile

def test_scoring():
    p = get_default_local_reproducibility_governance_profile()
    df, s = build_reproducibility_readiness_score_report(pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), p)
    assert not df.empty
    assert 0 <= s["score"] <= 1
