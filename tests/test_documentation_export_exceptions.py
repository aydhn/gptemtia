"""Test exceptions."""
import pandas as pd
from commodity_fx_signal_bot.local_documentation_export.documentation_export_exceptions import build_documentation_export_exception_register
from commodity_fx_signal_bot.local_documentation_export.export_config import get_default_local_documentation_export_profile

def test_exceptions():
    p = get_default_local_documentation_export_profile()
    df, s = build_documentation_export_exception_register(pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), p)
    assert df.empty  # Since inputs are empty, result might be empty
