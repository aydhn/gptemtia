from advanced_feature_store_integration.feature_store_query_contracts import (
    build_feature_store_query_contract_registry,
    validate_feature_store_query_request,
    summarize_feature_store_query_contracts,
)

def test_query_contracts():
    df, s = build_feature_store_query_contract_registry()
    assert not df.empty
    assert s["non_signal_guaranteed"] is True
    assert s["target_prediction_query_forbidden"] is True

    valid_q = {"filters": {"entity_type": "entity_fx_pair", "feature_family": "technical"}}
    assert validate_feature_store_query_request(valid_q)["is_allowed"] is True

    bad_q = {"filters": {"signal": "buy", "target": "next_return"}}
    res = validate_feature_store_query_request(bad_q)
    assert res["is_allowed"] is False
    assert res["non_signal"] is False
