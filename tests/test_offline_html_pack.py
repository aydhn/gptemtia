"""Test offline HTML pack."""
from pathlib import Path
from commodity_fx_signal_bot.local_documentation_export.offline_html_pack import build_offline_html_documentation_pack
from commodity_fx_signal_bot.local_documentation_export.export_config import get_default_local_documentation_export_profile

def test_html_pack():
    p = get_default_local_documentation_export_profile()
    txt, s = build_offline_html_documentation_pack(Path("."), p)
    assert len(txt) > 0
