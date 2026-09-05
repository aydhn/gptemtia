from advanced_feature_engine.feature_engine_models import (
    FeatureEngineProfileItem,
    FeatureEngineDomain,
    FeatureInputContract,
    FeatureSchema,
    FactorSchema,
    IndicatorCatalogItem,
    FeatureComputationResult,
    FeatureValidationFinding,
    build_feature_engine_profile_id,
    build_feature_engine_domain_id,
    build_feature_input_contract_id,
    build_feature_schema_id,
    build_factor_schema_id,
    build_indicator_catalog_id,
    build_feature_computation_result_id,
    build_feature_validation_finding_id,
)


def test_feature_engine_models():
    prof_item = FeatureEngineProfileItem(
        profile_id="p1",
        profile_name="balanced_local_feature_engine",
        current_phase=116,
        target_final_phase=160,
        next_phase=117,
        local_only=True,
        non_production=True,
        research_only=True,
        dry_run=True,
        non_signal=True,
        status_label="feature_ready",
    )
    d = prof_item.to_dict()
    assert d["non_signal"] is True
    assert d["current_phase"] == 116

    assert build_feature_engine_profile_id("test") == "fep_test"
    assert "price" in build_feature_engine_domain_id("price_indicator_domain")
    assert "fx_ohlcv" in build_feature_input_contract_id("dataset_fx_ohlcv")
    assert "close_ret" in build_feature_schema_id("close_ret", "dataset_fx_ohlcv")
    assert "trend" in build_factor_schema_id("trend_factor")
    assert "rsi" in build_indicator_catalog_id("rsi", "momentum")
    assert "ret" in build_feature_computation_result_id("ret", "fx_provider")
    assert "ret" in build_feature_validation_finding_id("ret", "dataset_fx_ohlcv")
