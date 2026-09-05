"""Test validation."""
from commodity_fx_signal_bot.local_documentation_export.documentation_export_validation import build_documentation_export_validation_report
from commodity_fx_signal_bot.local_documentation_export.export_config import get_default_local_documentation_export_profile

def test_validation():
    p = get_default_local_documentation_export_profile()
    df, s = build_documentation_export_validation_report({}, p)
    assert s["passed"]
