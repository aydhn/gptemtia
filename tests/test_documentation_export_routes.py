"""Test export routes."""
from commodity_fx_signal_bot.local_documentation_export.documentation_export_routes import build_documentation_export_route_map
from commodity_fx_signal_bot.local_documentation_export.export_config import get_default_local_documentation_export_profile

def test_export_routes():
    p = get_default_local_documentation_export_profile()
    df, s = build_documentation_export_route_map(p)
    assert not df.empty
