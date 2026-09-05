"""Test runbook."""
from commodity_fx_signal_bot.local_reproducibility_governance.deterministic_runbook import build_deterministic_runbook
from commodity_fx_signal_bot.local_reproducibility_governance.reproducibility_config import get_default_local_reproducibility_governance_profile
from pathlib import Path

def test_runbook():
    p = get_default_local_reproducibility_governance_profile()
    text, s = build_deterministic_runbook(Path("."), p)
    assert "Deterministic runbook" in text
