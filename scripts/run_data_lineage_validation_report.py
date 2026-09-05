import json
from pathlib import Path
from config.settings import Settings
from data.storage.data_lake import DataLake
from advanced_data_lineage.data_lineage_config import get_default_data_lineage_profile
from advanced_data_lineage.data_lineage_safety_boundary import build_data_lineage_safety_boundary
from advanced_data_lineage.data_lineage_validation import build_data_lineage_validation_report
from advanced_data_lineage.data_lineage_report_builder import (
    build_data_lineage_validation_markdown_report,
    build_data_lineage_safety_markdown_report,
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


def main():
    settings = Settings()
    project_root = Path(__file__).resolve().parent.parent
    data_lake = DataLake(base_dir=project_root)
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
    safe_df, safe_sum = build_data_lineage_safety_boundary(profile)

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

    data_lake.save_data_lineage_safety_boundary(safe_df, safe_sum)
    data_lake.save_data_lineage_validation_report(val_df, val_sum)

    out_dir = project_root / "reports" / "output" / "advanced_data_lineage"
    csv_dir = out_dir / "csv"
    md_dir = out_dir / "markdown"
    txt_dir = out_dir / "txt"
    json_dir = out_dir / "json"

    for d in [csv_dir, md_dir, txt_dir, json_dir]:
        d.mkdir(parents=True, exist_ok=True)

    val_df.to_csv(csv_dir / "data_lineage_validation_report.csv", index=False)
    safe_df.to_csv(csv_dir / "data_lineage_safety_boundary.csv", index=False)

    with open(json_dir / "data_lineage_validation_report.json", "w", encoding="utf-8") as f:
        json.dump(val_sum, f, ensure_ascii=False, indent=2)

    with open(json_dir / "data_lineage_safety_boundary.json", "w", encoding="utf-8") as f:
        json.dump(safe_sum, f, ensure_ascii=False, indent=2)

    md_val = build_data_lineage_validation_markdown_report(val_sum, val_df)
    (md_dir / "data_lineage_validation_report.md").write_text(md_val, encoding="utf-8")
    (txt_dir / "data_lineage_validation_report.txt").write_text(md_val, encoding="utf-8")

    md_safe = build_data_lineage_safety_markdown_report(safe_sum, safe_df)
    (md_dir / "data_lineage_safety_boundary.md").write_text(md_safe, encoding="utf-8")
    (txt_dir / "data_lineage_safety_boundary.txt").write_text(md_safe, encoding="utf-8")

    print(f"Data lineage validation and safety report completed: {val_sum['passed_rules']}/{val_sum['total_rules']} rules passed, {safe_sum['total_no_go']} No-Go rules active.")


if __name__ == "__main__":
    main()
