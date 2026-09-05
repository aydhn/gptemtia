"""Test environment replay manifest."""
from commodity_fx_signal_bot.local_reproducibility_governance.environment_replay_manifest import build_environment_replay_manifest
from commodity_fx_signal_bot.local_reproducibility_governance.reproducibility_config import get_default_local_reproducibility_governance_profile
from pathlib import Path

def test_manifest():
    p = get_default_local_reproducibility_governance_profile()
    text, s = build_environment_replay_manifest(Path("."), p)
    assert "Environment replay" in text
