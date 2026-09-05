from advanced_data_lineage.data_lineage_config import get_default_data_lineage_profile
from advanced_data_lineage.data_lineage_validation import (
    validate_no_forbidden_lineage_claims,
    build_data_lineage_validation_report,
)
from advanced_data_lineage.data_lineage_profile_registry import build_data_lineage_profile_registry
from advanced_data_lineage.data_lineage_domain_registry import build_data_lineage_domain_registry
from advanced_data_lineage.provenance_source_registry import build_provenance_source_registry
from advanced_data_lineage.source_reference_registry import build_source_reference_registry
from advanced_data_lineage.provider_provenance_registry import build_provider_provenance_registry
from advanced_data_lineage.dataset_provenance_registry import build_dataset_provenance_registry
from advanced_data_lineage.schema_provenance_registry import build_schema_provenance_registry
from advanced_data_lineage.transformation_provenance_registry import build_transformation_provenance_registry
from advanced_data_lineage.license_provenance_registry import build_license_provenance_registry
from advanced_data_lineage.copyright_boundary_provenance import build_copyright_boundary_provenance_registry
from advanced_data_lineage.metadata_only_provenance import build_metadata_only_provenance_registry
from advanced_data_lineage.audit_trail_event_registry import build_audit_trail_event_registry
from advanced_data_lineage.traceability_scoring import build_dataset_traceability_score_report
from advanced_data_lineage.data_lineage_safety_boundary import build_data_lineage_safety_boundary


def test_validation_forbidden_claims():
    clean_text = "Data lineage and provenance diagnostic report for offline research."
    res = validate_no_forbidden_lineage_claims(text=clean_text)
    assert res["passed"] is True

    dirty_text = "This model provides official approval and live trading buy signal."
    res_bad = validate_no_forbidden_lineage_claims(text=dirty_text)
    assert res_bad["passed"] is False
    assert len(res_bad["violations"]) > 0


def test_full_validation_report():
    profile = get_default_data_lineage_profile()
    prof_df, _ = build_data_lineage_profile_registry(profile)
    dom_df, _ = build_data_lineage_domain_registry(profile)
    src_df, _ = build_provenance_source_registry(profile)
    ref_df, _ = build_source_reference_registry(profile)
    prov_df, _ = build_provider_provenance_registry(profile)
    ds_df, _ = build_dataset_provenance_registry(profile)
    sch_df, _ = build_schema_provenance_registry(profile)
    trans_df, _ = build_transformation_provenance_registry(profile)
    lic_df, _ = build_license_provenance_registry(profile)
    cop_df, _ = build_copyright_boundary_provenance_registry(profile)
    meta_df, _ = build_metadata_only_provenance_registry(profile)
    aud_df, _ = build_audit_trail_event_registry(profile)
    trace_df, _ = build_dataset_traceability_score_report(profile)
    safe_df, _ = build_data_lineage_safety_boundary(profile)

    tables = {
        "profiles": prof_df,
        "domains": dom_df,
        "sources": src_df,
        "source_references": ref_df,
        "providers": prov_df,
        "datasets": ds_df,
        "schemas": sch_df,
        "transformations": trans_df,
        "licenses": lic_df,
        "copyright": cop_df,
        "metadata_only": meta_df,
        "audit_trail": aud_df,
        "traceability_scores": trace_df,
        "safety": safe_df,
    }

    val_df, val_sum = build_data_lineage_validation_report(tables, profile)
    assert len(val_df) >= 12
    assert val_sum["validation_status"] == "PASS"
