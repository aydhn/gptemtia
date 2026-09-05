"""Test criteria."""
from commodity_fx_signal_bot.local_reproducibility_governance.reproducibility_governance_criteria import build_reproducibility_governance_criteria_matrix
from commodity_fx_signal_bot.local_reproducibility_governance.reproducibility_config import get_default_local_reproducibility_governance_profile

def test_criteria():
    p = get_default_local_reproducibility_governance_profile()
    df, s = build_reproducibility_governance_criteria_matrix(p)
    assert not df.empty
