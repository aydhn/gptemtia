import sys
from pathlib import Path

root = Path(__file__).resolve().parent.parent
if str(root) not in sys.path:
    sys.path.insert(0, str(root))

from config.settings import Settings
from config.paths import ensure_project_directories
from data.storage.data_lake import DataLake
from advanced_data_normalization.data_normalization_config import get_default_data_normalization_profile
from advanced_data_normalization.data_normalization_pipeline import DataNormalizationPipeline
from advanced_data_normalization.data_normalization_report_builder import (
    build_data_normalization_validation_markdown_report,
    build_data_normalization_safety_markdown_report,
)


def main():
    ensure_project_directories()
    settings = Settings()
    profile = get_default_data_normalization_profile()
    lake = DataLake()
    pipeline = DataNormalizationPipeline(data_lake=lake, settings=settings, project_root=root, profile=profile)

    # Collect core tables to validate
    p_tables, _ = pipeline.build_normalization_profiles_and_domains(save=False)
    r_tables, _ = pipeline.build_normalization_rules_and_canonical_schema(save=False)
    v_tables, _ = pipeline.build_normalized_views_and_findings(save=False)
    s_tables, _ = pipeline.build_normalization_scores_and_mapping(save=False)

    tables_to_validate = {
        "profile_registry": p_tables.get("profile_registry"),
        "domain_registry": p_tables.get("domain_registry"),
        "rule_registry": r_tables.get("rule_registry"),
        "canonical_schema_registry": r_tables.get("canonical_schema_registry"),
        "canonical_field_registry": r_tables.get("canonical_field_registry"),
        "decision_registry": v_tables.get("decision_registry"),
        "manual_review_queue": v_tables.get("manual_review_queue"),
        "output_manifest": v_tables.get("output_manifest"),
        "score_report": s_tables.get("score_report"),
    }

    tables, summary = pipeline.build_health_validation_safety_and_handoff(
        tables_to_validate=tables_to_validate,
        save=True,
    )
    val_df = tables.get("validation_report")
    safe_df = tables.get("safety_boundary")

    out_dir = root / "reports" / "output" / "advanced_data_normalization"
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "csv").mkdir(exist_ok=True)
    (out_dir / "markdown").mkdir(exist_ok=True)
    (out_dir / "txt").mkdir(exist_ok=True)

    if val_df is not None:
        val_df.to_csv(out_dir / "csv" / "data_normalization_validation_report.csv", index=False)
    if safe_df is not None:
        safe_df.to_csv(out_dir / "csv" / "data_normalization_safety_boundary.csv", index=False)

    md_val = build_data_normalization_validation_markdown_report(summary.get("validation_summary", {}), val_df)
    with open(out_dir / "markdown" / "data_normalization_validation_report.md", "w", encoding="utf-8") as f:
        f.write(md_val)

    md_safe = build_data_normalization_safety_markdown_report(summary.get("safety_summary", {}), safe_df)
    with open(out_dir / "markdown" / "data_normalization_safety_boundary_report.md", "w", encoding="utf-8") as f:
        f.write(md_safe)

    with open(out_dir / "txt" / "validation_summary.txt", "w", encoding="utf-8") as f:
        f.write(f"Total Validations: {summary.get('validation_summary', {}).get('total_validations', 0)}\n")
        f.write(f"All Passed: {summary.get('validation_summary', {}).get('all_passed', True)}\n")
        f.write(f"Forbidden Claims: {summary.get('validation_summary', {}).get('forbidden_claims_found', 0)}\n")

    print(f"Data normalization validation report generated: All Passed={summary.get('validation_summary', {}).get('all_passed', True)}")


if __name__ == "__main__":
    main()
