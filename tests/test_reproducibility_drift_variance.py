"""Test drift variance."""
from commodity_fx_signal_bot.local_reproducibility_governance.reproducibility_drift_variance import (
    build_reproducibility_drift_register, build_reproducibility_variance_register
)
from commodity_fx_signal_bot.local_reproducibility_governance.reproducibility_config import get_default_local_reproducibility_governance_profile

def test_drift_variance():
    p = get_default_local_reproducibility_governance_profile()
    df1, s1 = build_reproducibility_drift_register(p)
    df2, s2 = build_reproducibility_variance_register(p)
    assert not df1.empty
    assert not df2.empty
