import pytest
from advanced_factor_metadata.factor_contract_registry import (
    build_factor_contract_registry,
    validate_factor_contract,
)
from advanced_factor_metadata.factor_metadata_models import FactorContract


def test_build_factor_contract_registry():
    df, summary = build_factor_contract_registry()
    assert not df.empty
    assert summary["total_contracts"] == 12
    assert summary["all_contracts_valid"] is True
    assert summary["non_signal"] is True

    contract_names = list(df["factor_name"])
    assert "factor_trend_multi_window_context" in contract_names
    assert "factor_momentum_rsi_roc_context" in contract_names
    assert "factor_volatility_atr_realized_context" in contract_names
    assert "factor_mean_reversion_zscore_context" in contract_names
    assert "factor_macro_inflation_rate_context" in contract_names
    assert "factor_event_release_context" in contract_names
    assert "factor_news_attention_context" in contract_names
    assert "factor_cross_asset_context" in contract_names


def test_validate_factor_contract_forbidden_word():
    invalid_contract = FactorContract(
        contract_id="test",
        factor_name="factor_trend_buy_signal",
        factor_family="trend",
        required_feature_sets=["fset_sma"],
    )
    res = validate_factor_contract(invalid_contract)
    assert res["is_valid"] is False
    assert any("forbidden token" in err for err in res["errors"])
