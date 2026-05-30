import pandas as pd
from report_summarization.symbol_briefs import extract_symbols_from_reports, build_symbol_brief_cards
from report_summarization.summary_config import get_default_report_summary_profile

def test_build_symbol_brief_cards():
    profile = get_default_report_summary_profile()
    inv = pd.DataFrame()
    sums = pd.DataFrame()
    finds = pd.DataFrame([{"related_symbols": ["GC=F", "SI=F"]}])
    warns = pd.DataFrame()

    df, meta = build_symbol_brief_cards(inv, finds, warns, sums, profile)
    assert not df.empty
    assert len(df) == 2
    assert "GC=F" in df["symbol"].tolist()
