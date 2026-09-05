"""Test evidence."""
from commodity_fx_signal_bot.local_reproducibility_governance.reproducibility_evidence import build_reproducibility_evidence_index
from commodity_fx_signal_bot.local_reproducibility_governance.reproducibility_config import get_default_local_reproducibility_governance_profile
from pathlib import Path

def test_evidence():
    p = get_default_local_reproducibility_governance_profile()
    df, s = build_reproducibility_evidence_index(Path("."), p)
    assert not df.empty
