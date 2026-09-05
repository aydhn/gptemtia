import sys
from pathlib import Path

root = Path(__file__).resolve().parent.parent
if str(root) not in sys.path:
    sys.path.insert(0, str(root))

from config.settings import Settings
from config.paths import ensure_project_directories
from data.storage.data_lake import DataLake
from advanced_data_quality.data_quality_config import get_default_data_quality_profile
from advanced_data_quality.data_quality_pipeline import DataQualityPipeline
from advanced_data_quality.data_quality_report_builder import (
    build_quality_rule_registry_markdown_report,
)


def main():
    ensure_project_directories()
    settings = Settings()
    profile = get_default_data_quality_profile()
    lake = DataLake()
    pipeline = DataQualityPipeline(data_lake=lake, settings=settings, project_root=root, profile=profile)

    rules_tables, rules_sum = pipeline.build_quality_rules(save=True)
    domain_tables, domain_sum = pipeline.run_domain_quality_contracts(save=True)

    out_dir = root / "reports" / "output" / "advanced_data_quality"
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "csv").mkdir(exist_ok=True)
    (out_dir / "markdown").mkdir(exist_ok=True)
    (out_dir / "txt").mkdir(exist_ok=True)

    rules_df = rules_tables.get("rule_registry")
    if rules_df is not None:
        rules_df.to_csv(out_dir / "csv" / "quality_rule_registry.csv", index=False)

    md = build_quality_rule_registry_markdown_report(rules_sum.get("rule_summary", {}), rules_df)
    with open(out_dir / "markdown" / "quality_rule_registry_report.md", "w", encoding="utf-8") as f:
        f.write(md)

    with open(out_dir / "txt" / "quality_rule_registry_summary.txt", "w", encoding="utf-8") as f:
        f.write(f"Total Rules Registered: {len(rules_df) if rules_df is not None else 0}\n")

    print(f"Quality rule registry & domain contracts generated. Rules: {len(rules_df) if rules_df is not None else 0}")


if __name__ == "__main__":
    main()
