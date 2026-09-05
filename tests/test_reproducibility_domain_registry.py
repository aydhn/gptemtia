"""Test domain registry."""
from commodity_fx_signal_bot.local_reproducibility_governance.reproducibility_domain_registry import build_reproducibility_domain_registry
from commodity_fx_signal_bot.local_reproducibility_governance.reproducibility_config import get_default_local_reproducibility_governance_profile

def test_domain_registry():
    p = get_default_local_reproducibility_governance_profile()
    df, summary = build_reproducibility_domain_registry(p)
    assert not df.empty
