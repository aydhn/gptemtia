"""Test domain registry."""
from commodity_fx_signal_bot.local_documentation_export.export_domain_registry import build_documentation_export_domain_registry
from commodity_fx_signal_bot.local_documentation_export.export_config import get_default_local_documentation_export_profile

def test_domain_registry():
    p = get_default_local_documentation_export_profile()
    df, s = build_documentation_export_domain_registry(p)
    assert not df.empty
