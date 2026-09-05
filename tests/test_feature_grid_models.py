from advanced_feature_grid.feature_grid_models import (
    FeatureGridProfileItem,
    FeatureGridDomain,
    WindowGridContract,
    IndicatorParameterGrid,
    FeatureGridOutputSchema,
    FeatureGridComputationResult,
    FeatureGridValidationFinding,
    build_feature_grid_profile_id,
    build_feature_grid_domain_id,
    build_window_grid_contract_id,
    build_indicator_parameter_grid_id,
    build_feature_grid_output_schema_id,
    build_feature_grid_computation_result_id,
    build_feature_grid_validation_finding_id,
    FORBIDDEN_OUTPUT_WORDS,
)


def test_feature_grid_models_and_ids():
    prof_id = build_feature_grid_profile_id("Balanced Profile")
    assert prof_id == "fg_prof_balanced_profile"

    dom_id = build_feature_grid_domain_id("Window Contract Domain")
    assert "wgc" not in dom_id
    assert "fg_dom" in dom_id

    wgc_id = build_window_grid_contract_id("sma_grid", "sma")
    assert wgc_id == "wgc_sma_grid_sma"

    ipg_id = build_indicator_parameter_grid_id("rsi", "momentum")
    assert ipg_id == "ipg_momentum_rsi"

    schema_id = build_feature_grid_output_schema_id("ma_grid", "sma_w20")
    assert "fgos_ma_grid" in schema_id

    res_id = build_feature_grid_computation_result_id("vol_grid", "synthetic")
    assert "fgcr_vol_grid" in res_id

    val_id = build_feature_grid_validation_finding_id("global", "rule_1")
    assert "fgvf_global" in val_id

    # Test dataclass to_dict
    contract = WindowGridContract(
        contract_id=wgc_id,
        grid_name="sma_grid",
        indicator_family="moving_average",
        indicator_name="sma",
        allowed_windows=[5, 10, 20],
        default_windows=[10, 20],
    )
    d = contract.to_dict()
    assert d["grid_name"] == "sma_grid"
    assert "signal" not in d["grid_name"]

    assert "signal" in FORBIDDEN_OUTPUT_WORDS
    assert "buy" in FORBIDDEN_OUTPUT_WORDS
    assert "target" in FORBIDDEN_OUTPUT_WORDS
