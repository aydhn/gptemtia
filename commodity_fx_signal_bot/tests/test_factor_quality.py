from factor_research.factor_quality import check_for_forbidden_trade_terms_in_factor_research

def test_factor_quality():
    res = check_for_forbidden_trade_terms_in_factor_research(text="This is a BUY signal")
    assert not res["is_clean"]
    assert "BUY" in res["forbidden_terms_found"]
