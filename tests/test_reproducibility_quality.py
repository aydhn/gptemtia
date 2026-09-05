"""Test quality."""
from commodity_fx_signal_bot.local_reproducibility_governance.reproducibility_quality import build_reproducibility_quality_report
from commodity_fx_signal_bot.local_reproducibility_governance.reproducibility_config import get_default_local_reproducibility_governance_profile

def test_quality():
    p = get_default_local_reproducibility_governance_profile()
    q = build_reproducibility_quality_report({})
    assert q["passed"]
