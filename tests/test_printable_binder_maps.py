"""Test binder maps."""
from commodity_fx_signal_bot.local_documentation_export.printable_binder_maps import build_printable_binder_section_registry
from commodity_fx_signal_bot.local_documentation_export.export_config import get_default_local_documentation_export_profile

def test_binder_maps():
    p = get_default_local_documentation_export_profile()
    df, s = build_printable_binder_section_registry(p)
    assert not df.empty
