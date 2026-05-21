import pandas as pd
from portfolio_regime.regime_quality import check_for_forbidden_trade_terms_in_regime_research

def test_forbidden_terms():
    text = "Burası AL sinyali üretiyor"
    res = check_for_forbidden_trade_terms_in_regime_research(text=text)
    assert res['forbidden_trade_terms_found']
    assert "AL" in res['terms']

    text = "This is a clean research report"
    res = check_for_forbidden_trade_terms_in_regime_research(text=text)
    assert not res['forbidden_trade_terms_found']
