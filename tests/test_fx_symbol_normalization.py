from advanced_fx_providers.fx_symbol_normalization import normalize_fx_pair_symbol
def test_normalization():
    assert normalize_fx_pair_symbol("EURUSD") == "EUR/USD"
    assert normalize_fx_pair_symbol("USDTRY") == "USD/TRY"
