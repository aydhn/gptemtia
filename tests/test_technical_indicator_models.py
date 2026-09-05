from advanced_technical_indicators.technical_indicator_models import (
    TechnicalIndicatorProfileItem,
    TechnicalIndicatorDomain,
    TechnicalIndicatorCatalogItem,
    IndicatorParameterContract,
    IndicatorOutputSchema,
    IndicatorComputationResult,
    IndicatorValidationFinding,
    build_technical_indicator_profile_id,
    build_technical_indicator_domain_id,
    build_technical_indicator_id,
    build_indicator_parameter_id,
    build_indicator_output_schema_id,
    build_indicator_computation_result_id,
    build_indicator_validation_finding_id,
)


def test_technical_indicator_models():
    prof_id = build_technical_indicator_profile_id("test_prof")
    assert prof_id == "tiprof_test_prof"

    p_item = TechnicalIndicatorProfileItem(
        profile_id=prof_id,
        profile_name="test_prof",
        current_phase=117,
        target_final_phase=160,
        next_phase=118,
        local_only=True,
        non_production=True,
        research_only=True,
        dry_run=True,
        non_signal=True,
        status_label="indicator_ready",
    )
    d = p_item.to_dict()
    assert d["current_phase"] == 117
    assert d["non_signal"] is True

    cat_id = build_technical_indicator_id("rsi", "family_momentum")
    assert "rsi" in cat_id
