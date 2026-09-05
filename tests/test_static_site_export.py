"""Test static site."""
from pathlib import Path
from commodity_fx_signal_bot.local_documentation_export.static_site_export import build_final_local_static_site_export_rehearsal
from commodity_fx_signal_bot.local_documentation_export.export_config import get_default_local_documentation_export_profile

def test_static_site():
    p = get_default_local_documentation_export_profile()
    txt, s = build_final_local_static_site_export_rehearsal(Path("."), p)
    assert len(txt) > 0
