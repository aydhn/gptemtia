from advanced_fx_providers.fx_symbol_normalization import normalize_fx_pair_symbol


def test_normalization():
    # 6-char basic
    assert normalize_fx_pair_symbol("EURUSD") == "EUR/USD"
    assert normalize_fx_pair_symbol("USDTRY") == "USD/TRY"

    # Separators
    assert normalize_fx_pair_symbol("EUR-USD") == "EUR/USD"
    assert normalize_fx_pair_symbol("EUR_USD") == "EUR/USD"
    assert normalize_fx_pair_symbol("EUR.USD") == "EUR/USD"
    assert normalize_fx_pair_symbol("EUR/USD") == "EUR/USD"
    assert normalize_fx_pair_symbol("BTC-USDT") == "BTC/USDT"

    # Non-standard lengths with known quotes
    assert normalize_fx_pair_symbol("DOGEUSD") == "DOGE/USD"
    assert normalize_fx_pair_symbol("BTCUSDT") == "BTC/USDT"
    assert (
        normalize_fx_pair_symbol("XAUUSD") == "XAU/USD"
    )  # Though 6 chars, works with either

    # Known mappings
    # assert normalize_fx_pair_symbol("EUROUSD") == "EUR/USD"
