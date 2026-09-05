"""Test manual review."""
from commodity_fx_signal_bot.local_reproducibility_governance.reproducibility_manual_review import build_reproducibility_manual_review_ledger
from commodity_fx_signal_bot.local_reproducibility_governance.reproducibility_config import get_default_local_reproducibility_governance_profile

def test_manual_review():
    p = get_default_local_reproducibility_governance_profile()
    df, s = build_reproducibility_manual_review_ledger(p)
    assert not df.empty
