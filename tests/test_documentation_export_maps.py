"""Test documentation export maps."""
from pathlib import Path
from commodity_fx_signal_bot.local_documentation_export.documentation_export_maps import build_documentation_export_source_map
from commodity_fx_signal_bot.local_documentation_export.export_config import get_default_local_documentation_export_profile

def test_export_maps():
    p = get_default_local_documentation_export_profile()
    df, s = build_documentation_export_source_map(Path("."), p)
    assert not df.empty
