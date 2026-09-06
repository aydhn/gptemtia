import pandas as pd
from advanced_regime_featurestore_integration.regime_featurestore_report_builder import (
    build_regime_featurestore_disclaimer,
    build_regime_featurestore_profile_markdown_report,
    build_regime_featurestore_contract_markdown_report,
    build_regime_featurestore_schema_markdown_report,
    build_regime_component_store_catalog_markdown_report,
    build_regime_accepted_reference_markdown_report,
    build_regime_featurestore_manifest_markdown_report,
    build_regime_featurestore_validation_markdown_report,
    build_regime_featurestore_safety_markdown_report,
    build_phase_135_handoff_markdown_report,
)


def test_regime_featurestore_report_builder():
    disc = build_regime_featurestore_disclaimer()
    assert "Yasal ve Operasyonel Sınır" in disc
    assert "Phase 134" in disc

    prof_md = build_regime_featurestore_profile_markdown_report({"active_profile": "research"})
    assert "# Phase 134: Regime FeatureStore Profile Registry Report" in prof_md
    assert "Active Profile" in prof_md

    contract_md = build_regime_featurestore_contract_markdown_report({"total_contracts": 10})
    assert "# Phase 134: Regime FeatureStore Contract Registry Report" in contract_md

    schema_md = build_regime_featurestore_schema_markdown_report({"total_fields": 15})
    assert "# Phase 134: Regime FeatureStore Schema Registry Report" in schema_md

    cat_md = build_regime_component_store_catalog_markdown_report({"domain": "taxonomy", "total_items": 4})
    assert "# Phase 134: Component Store Catalog Report" in cat_md

    ref_md = build_regime_accepted_reference_markdown_report({"reference_type": "no_lookahead", "total_references": 5})
    assert "# Phase 134: Regime Accepted Reference Registry Report" in ref_md

    man_md = build_regime_featurestore_manifest_markdown_report({"manifest_name": "test_manifest", "readiness_score": 1.0})
    assert "# Phase 134: Regime FeatureStore Metadata Manifest Report" in man_md

    val_md = build_regime_featurestore_validation_markdown_report({"status": "VALIDATION_PASS", "total_checks": 5})
    assert "# Phase 134: Regime FeatureStore Validation Report" in val_md

    safe_md = build_regime_featurestore_safety_markdown_report({"safety_status": "SECURE", "no_go_count": 21})
    assert "# Phase 134: Regime FeatureStore Safety Boundary Report" in safe_md

    handoff_md = build_phase_135_handoff_markdown_report({"handoff_status": "READY", "total_prerequisites": 14})
    assert "# Phase 134 to Phase 135 Handoff Report" in handoff_md
