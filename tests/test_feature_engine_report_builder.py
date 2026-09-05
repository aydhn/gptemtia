from advanced_feature_engine.feature_engine_report_builder import (
    build_feature_engine_disclaimer,
    build_feature_engine_profile_markdown_report,
    build_feature_input_contract_markdown_report,
    build_feature_schema_markdown_report,
    build_indicator_catalog_markdown_report,
    build_feature_metadata_markdown_report,
    build_feature_computation_markdown_report,
    build_feature_validation_markdown_report,
    build_feature_engine_health_markdown_report,
    build_feature_engine_safety_markdown_report,
    build_phase_117_handoff_markdown_report,
)


def test_feature_engine_report_builder():
    disclaimer = build_feature_engine_disclaimer()
    assert "Phase 116" in disclaimer
    assert "Canlı emir" in disclaimer

    rep1 = build_feature_engine_profile_markdown_report({"total_profiles": 3})
    assert "Profile Registry Report" in rep1

    rep2 = build_feature_input_contract_markdown_report({"total_contracts": 8})
    assert "Input Contracts Report" in rep2

    rep3 = build_feature_schema_markdown_report({"total_schemas": 17})
    assert "Feature Schema Registry Report" in rep3

    rep4 = build_indicator_catalog_markdown_report({"total_indicators": 30})
    assert "Indicator Catalog Registry Report" in rep4

    rep5 = build_feature_metadata_markdown_report({"total_features_registered": 17})
    assert "Feature Metadata Registry Report" in rep5

    rep6 = build_feature_computation_markdown_report({"features_computed_count": 12})
    assert "Basic Feature Computation Rehearsal Report" in rep6

    rep7 = build_feature_validation_markdown_report({"validation_status": "VALID"})
    assert "Feature Engine Validation Report" in rep7

    rep8 = build_feature_engine_health_markdown_report({"overall_status": "PASS"})
    assert "Feature Engine Health Check Report" in rep8

    rep9 = build_feature_engine_safety_markdown_report({"safety_status": "ACTIVE"})
    assert "Feature Engine Safety Boundary Report" in rep9

    rep10 = build_phase_117_handoff_markdown_report({"target_phase": 117})
    assert "Phase 117" in rep10
