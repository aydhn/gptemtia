"""Test presentation freeze maps."""
from commodity_fx_signal_bot.local_documentation_export.presentation_freeze_maps import build_presentation_freeze_section_registry
from commodity_fx_signal_bot.local_documentation_export.export_config import get_default_local_documentation_export_profile

def test_presentation_freeze_maps():
    p = get_default_local_documentation_export_profile()
    df, s = build_presentation_freeze_section_registry(p)
    assert not df.empty
