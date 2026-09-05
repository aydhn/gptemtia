"""Test maps."""
from commodity_fx_signal_bot.local_documentation_export.static_site_maps import build_static_site_page_registry
from commodity_fx_signal_bot.local_documentation_export.export_config import get_default_local_documentation_export_profile

def test_maps():
    p = get_default_local_documentation_export_profile()
    df, s = build_static_site_page_registry(p)
    assert not df.empty
