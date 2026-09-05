"""Test handoff."""
from commodity_fx_signal_bot.local_reproducibility_governance.reproducibility_governance_handoff import build_reproducibility_governance_handoff_checklist
from commodity_fx_signal_bot.local_reproducibility_governance.reproducibility_config import get_default_local_reproducibility_governance_profile

def test_handoff():
    p = get_default_local_reproducibility_governance_profile()
    df, s = build_reproducibility_governance_handoff_checklist(p)
    assert not df.empty
