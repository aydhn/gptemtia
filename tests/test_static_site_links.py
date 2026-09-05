"""Test links."""
from commodity_fx_signal_bot.local_documentation_export.static_site_links import build_static_site_link_map
from commodity_fx_signal_bot.local_documentation_export.export_config import get_default_local_documentation_export_profile

def test_links():
    p = get_default_local_documentation_export_profile()
    df, s = build_static_site_link_map(p)
    assert not df.empty
