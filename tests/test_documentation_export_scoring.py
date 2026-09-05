"""Test scoring."""
import pandas as pd
from commodity_fx_signal_bot.local_documentation_export.documentation_export_scoring import build_documentation_export_readiness_score_report
from commodity_fx_signal_bot.local_documentation_export.export_config import get_default_local_documentation_export_profile

def test_scoring():
    p = get_default_local_documentation_export_profile()
    df, s = build_documentation_export_readiness_score_report(pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), p)
    assert not df.empty
