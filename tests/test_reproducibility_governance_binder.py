"""Test binder."""
from commodity_fx_signal_bot.local_reproducibility_governance.reproducibility_governance_binder import build_terminal_reproducibility_governance_binder
from commodity_fx_signal_bot.local_reproducibility_governance.reproducibility_config import get_default_local_reproducibility_governance_profile
from pathlib import Path

def test_binder():
    p = get_default_local_reproducibility_governance_profile()
    text, s = build_terminal_reproducibility_governance_binder(Path("."), p)
    assert "Governance" in text
