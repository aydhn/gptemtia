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
    build_normalization_rule_registry_markdown_report,
    build_canonical_schema_markdown_report,
)


def main():
    ensure_project_directories()
    settings = Settings()
    profile = get_default_data_normalization_profile()
    lake = DataLake()
    pipeline = DataNormalizationPipeline(data_lake=lake, settings=settings, project_root=root, profile=profile)

    tables, summary = pipeline.build_normalization_rules_and_canonical_schema(save=True)
    rule_df = tables.get("rule_registry")
    schema_df = tables.get("canonical_schema_registry")
    field_df = tables.get("canonical_field_registry")
    ver_df = tables.get("schema_version_registry")
    prov_df = tables.get("provider_name_registry")

    out_dir = root / "reports" / "output" / "advanced_data_normalization"
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "csv").mkdir(exist_ok=True)
    (out_dir / "markdown").mkdir(exist_ok=True)
    (out_dir / "txt").mkdir(exist_ok=True)

    if rule_df is not None:
        rule_df.to_csv(out_dir / "csv" / "normalization_rule_registry.csv", index=False)
    if schema_df is not None:
        schema_df.to_csv(out_dir / "csv" / "canonical_schema_registry.csv", index=False)
    if field_df is not None:
        field_df.to_csv(out_dir / "csv" / "canonical_field_registry.csv", index=False)
    if ver_df is not None:
        ver_df.to_csv(out_dir / "csv" / "schema_version_registry.csv", index=False)
    if prov_df is not None:
        prov_df.to_csv(out_dir / "csv" / "provider_name_registry.csv", index=False)

    md_rule = build_normalization_rule_registry_markdown_report(summary.get("rule_summary", {}), rule_df)
    with open(out_dir / "markdown" / "normalization_rule_registry_report.md", "w", encoding="utf-8") as f:
        f.write(md_rule)

    md_schema = build_canonical_schema_markdown_report(summary.get("schema_summary", {}), schema_df)
    with open(out_dir / "markdown" / "canonical_schema_registry_report.md", "w", encoding="utf-8") as f:
        f.write(md_schema)

    with open(out_dir / "txt" / "rule_registry_summary.txt", "w", encoding="utf-8") as f:
        f.write(f"Normalization Rules: {summary.get('rule_summary', {}).get('total_rules', 0)}\n")
        f.write(f"Canonical Schemas: {summary.get('schema_summary', {}).get('total_schemas', 0)}\n")
        f.write(f"Canonical Fields: {summary.get('field_summary', {}).get('total_canonical_fields', 0)}\n")

    print(f"Normalization rule & schema registry generated successfully. Rules: {len(rule_df) if rule_df is not None else 0}")


if __name__ == "__main__":
    main()
