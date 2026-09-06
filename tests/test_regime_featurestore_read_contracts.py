import pandas as pd
from advanced_regime_featurestore_integration.regime_featurestore_read_contracts import (
    build_regime_featurestore_read_contract_registry,
    validate_regime_featurestore_read_request,
    summarize_regime_featurestore_read_contracts,
    CANONICAL_READ_CONTRACTS,
)


def test_build_regime_featurestore_read_contract_registry():
    df, summary = build_regime_featurestore_read_contract_registry()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 2
    assert summary["all_network_forbidden"] is True
    assert summary["all_signals_forbidden"] is True
    assert summary["non_signal"] is True
    assert summary["current_phase"] == 134


def test_validate_regime_featurestore_read_request():
    valid_req = {"request_id": "req_1", "dataset": "regime_taxonomy"}
    res = validate_regime_featurestore_read_request(valid_req)
    assert res["is_valid"] is True
    assert res["non_signal"] is True

    bad_req_network = {"network_call_requested": True}
    res_bad = validate_regime_featurestore_read_request(bad_req_network)
    assert res_bad["is_valid"] is False
    assert any("Network" in err for err in res_bad["errors"])

    bad_req_signal = {"query_signal": True}
    res_bad_sig = validate_regime_featurestore_read_request(bad_req_signal)
    assert res_bad_sig["is_valid"] is False


def test_summarize_regime_featurestore_read_contracts():
    df, _ = build_regime_featurestore_read_contract_registry()
    summary = summarize_regime_featurestore_read_contracts(df)
    assert summary["total_contracts"] == 2
    assert summary["all_network_prohibited"] is True
