import pandas as pd
from advanced_regime_featurestore_integration.regime_featurestore_query_contracts import (
    build_regime_featurestore_query_contract_registry,
    validate_regime_featurestore_query_request,
    summarize_regime_featurestore_query_contracts,
    CANONICAL_QUERY_FILTERS,
    FORBIDDEN_QUERY_TERMS,
)


def test_build_regime_featurestore_query_contract_registry():
    df, summary = build_regime_featurestore_query_contract_registry()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 8
    assert summary["forbidden_query_terms_count"] == len(FORBIDDEN_QUERY_TERMS)
    assert summary["non_signal"] is True
    assert summary["current_phase"] == 134


def test_validate_regime_featurestore_query_request():
    valid_query = {"store_entity_type": "regime_matrix", "source_phase": 127}
    res = validate_regime_featurestore_query_request(valid_query)
    assert res["is_valid"] is True
    assert res["non_signal"] is True

    bad_query_buy = {"store_entity_type": "regime_matrix", "action": "buy"}
    res_bad = validate_regime_featurestore_query_request(bad_query_buy)
    assert res_bad["is_valid"] is False
    assert any("buy" in err for err in res_bad["errors"])

    bad_query_pred = {"target_prediction": "bullish"}
    res_bad_pred = validate_regime_featurestore_query_request(bad_query_pred)
    assert res_bad_pred["is_valid"] is False


def test_summarize_regime_featurestore_query_contracts():
    df, _ = build_regime_featurestore_query_contract_registry()
    summary = summarize_regime_featurestore_query_contracts(df)
    assert summary["total_permitted_filters"] == 8
    assert summary["all_permitted"] is True
