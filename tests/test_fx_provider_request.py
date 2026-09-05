from advanced_fx_providers.fx_provider_request import create_fx_provider_request
def test_req():
    r = create_fx_provider_request("dummy", "fx_data_ohlcv")
    assert r.dry_run is True
    assert r.local_only is True
