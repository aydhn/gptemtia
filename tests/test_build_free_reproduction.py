"""Test build free."""
from commodity_fx_signal_bot.local_reproducibility_governance.build_free_reproduction import build_build_free_reproduction_manifest
from commodity_fx_signal_bot.local_reproducibility_governance.reproducibility_config import get_default_local_reproducibility_governance_profile
from pathlib import Path

def test_build_free():
    p = get_default_local_reproducibility_governance_profile()
    text, s = build_build_free_reproduction_manifest(Path("."), p)
    assert "Build-free" in text
