"""Test dossier."""
from commodity_fx_signal_bot.local_reproducibility_governance.reproducibility_dossier import build_final_local_reproducibility_dossier, build_reproducibility_dossier_index
from commodity_fx_signal_bot.local_reproducibility_governance.reproducibility_config import get_default_local_reproducibility_governance_profile
from pathlib import Path

def test_dossier():
    p = get_default_local_reproducibility_governance_profile()
    text, summary = build_final_local_reproducibility_dossier(Path("."), p)
    assert "dossier" in text
    df, summary2 = build_reproducibility_dossier_index(p)
    assert not df.empty
