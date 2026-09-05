from advanced_feature_store_integration.feature_store_write_contracts import (
    build_feature_store_write_contract_registry,
    validate_feature_store_write_request,
    summarize_feature_store_write_contracts,
)

def test_write_contracts():
    df, s = build_feature_store_write_contract_registry()
    assert not df.empty
    assert s["source_overwrite_forbidden"] is True
    assert s["auto_impute_forbidden"] is True
    assert s["auto_drop_forbidden"] is True

    valid_req = {"mode": "append", "has_validation_metadata": True}
    assert validate_feature_store_write_request(valid_req)["is_allowed"] is True

    bad_req = {"mode": "overwrite", "auto_impute": True, "auto_drop": True}
    res = validate_feature_store_write_request(bad_req)
    assert res["is_allowed"] is False
    assert res["source_preserved"] is False
