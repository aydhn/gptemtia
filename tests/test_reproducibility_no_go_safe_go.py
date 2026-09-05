"""Test no go."""
from commodity_fx_signal_bot.local_reproducibility_governance.reproducibility_no_go_safe_go import build_reproducibility_no_go_safe_go_summary
from commodity_fx_signal_bot.local_reproducibility_governance.reproducibility_config import get_default_local_reproducibility_governance_profile

def test_no_go():
    p = get_default_local_reproducibility_governance_profile()
    df, s = build_reproducibility_no_go_safe_go_summary(p)
    assert not df.empty
