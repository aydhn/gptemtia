from advanced_data_lineage.data_lineage_report_builder import (
    build_data_lineage_disclaimer,
    build_data_lineage_profile_markdown_report,
    build_provenance_source_markdown_report,
    build_provider_provenance_markdown_report,
    build_dataset_provenance_markdown_report,
    build_transformation_provenance_markdown_report,
    build_domain_lineage_markdown_report,
    build_license_copyright_markdown_report,
    build_audit_trail_markdown_report,
    build_lineage_finding_markdown_report,
    build_traceability_score_markdown_report,
    build_cross_domain_provenance_markdown_report,
    build_data_lineage_health_markdown_report,
    build_data_lineage_validation_markdown_report,
    build_data_lineage_safety_markdown_report,
    build_phase_115_handoff_markdown_report,
)


def test_report_builder_outputs():
    disc = build_data_lineage_disclaimer()
    assert "Phase 114 Data Lineage and Provenance" in disc
    assert "Canlı emir" in disc

    dummy_summary = {"current_phase": 114, "target_final_phase": 160}
    assert "Profile Registry" in build_data_lineage_profile_markdown_report(dummy_summary)
    assert "Provenance Source" in build_provenance_source_markdown_report(dummy_summary)
    assert "Provider Provenance" in build_provider_provenance_markdown_report(dummy_summary)
    assert "Dataset Provenance" in build_dataset_provenance_markdown_report(dummy_summary)
    assert "Transformation Provenance" in build_transformation_provenance_markdown_report(dummy_summary)
    assert "Domain Lineage" in build_domain_lineage_markdown_report(dummy_summary)
    assert "License & Copyright" in build_license_copyright_markdown_report(dummy_summary)
    assert "Audit Trail" in build_audit_trail_markdown_report(dummy_summary)
    assert "Lineage Finding" in build_lineage_finding_markdown_report(dummy_summary)
    assert "Traceability Score" in build_traceability_score_markdown_report(dummy_summary)
    assert "Cross-Domain Provenance" in build_cross_domain_provenance_markdown_report(dummy_summary)
    assert "Health Check" in build_data_lineage_health_markdown_report(dummy_summary)
    assert "Validation Report" in build_data_lineage_validation_markdown_report(dummy_summary)
    assert "Safety Boundary" in build_data_lineage_safety_markdown_report(dummy_summary)
    assert "Phase 115" in build_phase_115_handoff_markdown_report(dummy_summary)
