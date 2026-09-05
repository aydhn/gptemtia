from advanced_feature_store_integration.feature_store_read_contracts import (
    build_feature_store_read_contract_registry,
    validate_feature_store_read_request,
    summarize_feature_store_read_contracts,
)

def test_read_contracts():
    df, s = build_feature_store_read_contract_registry()
    assert not df.empty
    assert s["local_only_enforced"] is True
    assert s["non_signal_enforced"] is True

    valid_req = {"source": "local_disk", "query_text": "features for eurusd"}
    assert validate_feature_store_read_request(valid_req)["is_allowed"] is True

    invalid_req = {"source": "network_feed", "query_text": "signal for buy"}
    res = validate_feature_store_read_request(invalid_req)
    assert res["is_allowed"] is False
    assert res["non_signal"] is False
