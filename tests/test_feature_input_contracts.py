import pandas as pd
from advanced_feature_engine.feature_engine_config import get_default_feature_engine_profile
from advanced_feature_engine.feature_input_contracts import (
    build_feature_input_contract_registry,
    validate_feature_input_contract,
    summarize_feature_input_contracts,
)


def test_feature_input_contracts():
    profile = get_default_feature_engine_profile()
    df, summary = build_feature_input_contract_registry(profile)

    assert not df.empty
    assert len(df) >= 8
    assert "dataset_type" in df.columns
    assert "quality_dependency" in df.columns
    assert "normalization_dependency" in df.columns
    assert "lineage_dependency" in df.columns
    assert summary["all_contracts_registered"] is True
    assert summary["non_signal"] is True

    # Test validation with a valid FX OHLCV dataframe
    valid_fx = pd.DataFrame({
        "timestamp": ["2026-01-01"],
        "symbol": ["EURUSD"],
        "open": [1.08],
        "high": [1.09],
        "low": [1.07],
        "close": [1.085],
    })
    res = validate_feature_input_contract(valid_fx, "dataset_fx_ohlcv")
    assert res["valid"] is True
    assert len(res["missing_fields"]) == 0

    # Test validation with missing fields
    invalid_fx = pd.DataFrame({"timestamp": ["2026-01-01"], "close": [1.085]})
    res2 = validate_feature_input_contract(invalid_fx, "dataset_fx_ohlcv")
    assert res2["valid"] is False
    assert "open" in res2["missing_fields"]
