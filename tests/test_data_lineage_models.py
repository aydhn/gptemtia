from advanced_data_lineage.data_lineage_models import (
    DataLineageProfileItem,
    DataLineageDomain,
    ProvenanceSource,
    SourceReference,
    ProviderProvenance,
    DatasetProvenance,
    SchemaProvenance,
    TransformationProvenance,
    AuditTrailEvent,
    LineageFinding,
    TraceabilityScore,
    build_data_lineage_profile_id,
    build_data_lineage_domain_id,
    build_provenance_source_id,
    build_source_reference_id,
    build_provider_provenance_id,
    build_dataset_provenance_id,
    build_schema_provenance_id,
    build_transformation_provenance_id,
    build_audit_trail_event_id,
    build_lineage_finding_id,
    build_traceability_score_id,
)


def test_model_id_builders():
    assert build_data_lineage_profile_id("test profile") == "lineage_profile_test_profile"
    assert build_data_lineage_domain_id("fx domain") == "lineage_domain_fx_domain"
    assert "prov_src" in build_provenance_source_id("src1", "prov1")
    assert "ref" in build_source_reference_id("src1", "uri")
    assert "prov_rec" in build_provider_provenance_id("prov1")
    assert "ds_prov" in build_dataset_provenance_id("ds1", "prov1")
    assert "schema_prov" in build_schema_provenance_id("fx_quote", "v1.0")
    assert "trans_prov" in build_transformation_provenance_id("fx", "pair", "normalized_pair")
    assert "audit" in build_audit_trail_event_id("registered", "rec1")
    assert "finding" in build_lineage_finding_id("type1", "fx", "prov1")
    assert "trace_score" in build_traceability_score_id("ent1", "provider")


def test_models_to_dict():
    p = DataLineageProfileItem("p1", "prof1", 114, 160, 115, True, True, True, True, True, "lineage_complete")
    assert p.to_dict()["profile_id"] == "p1"

    src = ProvenanceSource("s1", "src1", "type1", "prov1", "ds1", "lic1", "mode1", "Strict no-scraping", False)
    assert src.to_dict()["no_scraping_policy"] == "Strict no-scraping"

    ref = SourceReference("r1", "s1", "type1", "val1", "can1", True, False, False, False)
    assert ref.to_dict()["contains_credentials"] is False
    assert ref.to_dict()["contains_full_text"] is False
