"""Test no go safe go."""
from commodity_fx_signal_bot.local_documentation_export.documentation_export_no_go_safe_go import build_documentation_export_no_go_safe_go_summary
from commodity_fx_signal_bot.local_documentation_export.export_config import get_default_local_documentation_export_profile

def test_no_go_safe_go():
    p = get_default_local_documentation_export_profile()
    df, s = build_documentation_export_no_go_safe_go_summary(p)
    assert not df.empty
