import pandas as pd
from advanced_regime_featurestore_integration.regime_featurestore_write_contracts import (
    build_regime_featurestore_write_contract_registry,
    validate_regime_featurestore_write_request,
    summarize_regime_featurestore_write_contracts,
    CANONICAL_WRITE_CONTRACTS,
)


def test_build_regime_featurestore_write_contract_registry():
    df, summary = build_regime_featurestore_write_contract_registry()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 2
    assert summary["all_source_overwrites_forbidden"] is True
    assert summary["all_destructive_cleans_forbidden"] is True
    assert summary["all_non_signal_required"] is True
    assert summary["non_signal"] is True
    assert summary["current_phase"] == 134


def test_validate_regime_featurestore_write_request():
    valid_req = {
        "request_id": "write_1",
        "validation_acceptance_ref": "acc_001",
        "no_lookahead_acceptance_ref": "acc_002",
        "non_signal": True,
    }
    res = validate_regime_featurestore_write_request(valid_req)
    assert res["is_valid"] is True
    assert res["non_signal"] is True

    bad_req_overwrite = {
        "attempt_source_overwrite": True,
        "validation_acceptance_ref": "acc_001",
        "no_lookahead_acceptance_ref": "acc_002",
        "non_signal": True,
    }
    res_bad = validate_regime_featurestore_write_request(bad_req_overwrite)
    assert res_bad["is_valid"] is False
    assert any("Overwriting" in err for err in res_bad["errors"])

    bad_req_missing_acc = {
        "non_signal": True,
    }
    res_missing = validate_regime_featurestore_write_request(bad_req_missing_acc)
    assert res_missing["is_valid"] is False


def test_summarize_regime_featurestore_write_contracts():
    df, _ = build_regime_featurestore_write_contract_registry()
    summary = summarize_regime_featurestore_write_contracts(df)
    assert summary["total_contracts"] == 2
    assert summary["all_overwrites_forbidden"] is True
