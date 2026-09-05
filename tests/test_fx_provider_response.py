from advanced_fx_providers.fx_provider_response import create_fx_provider_response
def test_resp():
    r = create_fx_provider_response("req", "dummy", "fx_data_ohlcv", "status")
    assert r.manual_review_required is True
