import pandas as pd
from report_summarization.digest_cards import build_research_digest_cards
from report_summarization.summary_config import get_default_report_summary_profile

def test_build_research_digest_cards():
    profile = get_default_report_summary_profile()
    sums = pd.DataFrame([{"module_name": "mod1"}])
    finds = pd.DataFrame()
    warns = pd.DataFrame()

    df, meta = build_research_digest_cards(sums, finds, warns, profile)
    assert not df.empty
    assert len(df) >= 11 # 1 module + 11 themes
