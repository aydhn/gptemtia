from advanced_regime_matrix.regime_matrix_config import get_default_regime_matrix_profile
from advanced_regime_matrix.regime_feature_matrix_contracts import (
    build_regime_feature_matrix_contract_registry,
    build_regime_feature_matrix_contracts,
    validate_regime_feature_matrix_contract,
    CORE_FEATURE_MATRIX_CONTRACTS,
)


def test_build_regime_feature_matrix_contracts():
    prof = get_default_regime_matrix_profile()
    df, s = build_regime_feature_matrix_contracts(prof)
    assert len(df) == 7
    assert s["total_contracts"] == 7
    assert s["all_non_signal"] is True
    assert s["all_source_preserved"] is True
    assert s["model_training_executed"] is False

    names = set(df["contract_name"].values)
    assert "regime_technical_feature_matrix_contract" in names
    assert "regime_factor_feature_matrix_contract" in names
    assert "regime_macro_event_context_matrix_contract" in names
    assert "regime_news_metadata_context_matrix_contract" in names
    assert "regime_cross_asset_context_matrix_contract" in names
    assert "regime_quality_drift_context_matrix_contract" in names
    assert "regime_combined_research_matrix_contract" in names


def test_validate_regime_feature_matrix_contract():
    c = CORE_FEATURE_MATRIX_CONTRACTS[0]
    res = validate_regime_feature_matrix_contract(c)
    assert res["is_valid"] is True
    assert res["non_signal"] is True
