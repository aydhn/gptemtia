"""Test integrity."""
from commodity_fx_signal_bot.local_reproducibility_governance.reproducibility_integrity import build_reproducibility_integrity_rehearsal
from commodity_fx_signal_bot.local_reproducibility_governance.reproducibility_config import get_default_local_reproducibility_governance_profile
from pathlib import Path

def test_integrity():
    p = get_default_local_reproducibility_governance_profile()
    df, s = build_reproducibility_integrity_rehearsal(Path("."), p)
    assert not df.empty
