"""Test risks."""
import pandas as pd
from commodity_fx_signal_bot.local_documentation_export.documentation_export_risks import build_documentation_export_risk_summary
from commodity_fx_signal_bot.local_documentation_export.export_config import get_default_local_documentation_export_profile

def test_risks():
    p = get_default_local_documentation_export_profile()
    df, s = build_documentation_export_risk_summary(pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), p)
    assert not df.empty
