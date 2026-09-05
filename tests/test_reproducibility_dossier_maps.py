"""Test dossier maps."""
from commodity_fx_signal_bot.local_reproducibility_governance.reproducibility_dossier_maps import (
    build_reproducibility_dossier_source_map, build_reproducibility_dossier_output_map, build_reproducibility_dossier_command_map
)
from commodity_fx_signal_bot.local_reproducibility_governance.reproducibility_config import get_default_local_reproducibility_governance_profile
from pathlib import Path

def test_dossier_maps():
    p = get_default_local_reproducibility_governance_profile()
    df1, s1 = build_reproducibility_dossier_source_map(Path("."), p)
    df2, s2 = build_reproducibility_dossier_output_map(p)
    df3, s3 = build_reproducibility_dossier_command_map(p)
    assert not df1.empty
    assert not df2.empty
    assert not df3.empty
