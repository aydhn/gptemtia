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
    build_cross_domain_mapping_markdown_report,
)


def main():
    ensure_project_directories()
    settings = Settings()
    profile = get_default_data_normalization_profile()
    lake = DataLake()
    pipeline = DataNormalizationPipeline(data_lake=lake, settings=settings, project_root=root, profile=profile)

    tables, summary = pipeline.run_symbol_indicator_event_tag_normalization(save=True)
    map_tables, map_sum = pipeline.build_normalization_scores_and_mapping(save=True)

    news_df = tables.get("news_topic_tag_report")
    cal_df = tables.get("calendar_event_report")
    map_df = map_tables.get("cross_domain_mapping")

    out_dir = root / "reports" / "output" / "advanced_data_normalization"
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "csv").mkdir(exist_ok=True)
    (out_dir / "markdown").mkdir(exist_ok=True)
    (out_dir / "txt").mkdir(exist_ok=True)

    if news_df is not None:
        news_df.to_csv(out_dir / "csv" / "news_topic_tag_normalization_enforcement_report.csv", index=False)
    if cal_df is not None:
        cal_df.to_csv(out_dir / "csv" / "calendar_event_normalization_enforcement_report.csv", index=False)
    if map_df is not None:
        map_df.to_csv(out_dir / "csv" / "cross_domain_normalized_mapping_report.csv", index=False)

    md = build_cross_domain_mapping_markdown_report(map_sum.get("cross_domain_summary", {}), map_df)
    with open(out_dir / "markdown" / "cross_domain_mapping_report.md", "w", encoding="utf-8") as f:
        f.write(md)

    with open(out_dir / "txt" / "news_calendar_normalization_summary.txt", "w", encoding="utf-8") as f:
        f.write(f"News Topics: {summary.get('news_topic_tag_summary', {}).get('total_mappings', 0)}\n")
        f.write(f"Calendar Events: {summary.get('calendar_event_summary', {}).get('total_mappings', 0)}\n")
        f.write(f"Cross-Domain Mappings: {map_sum.get('cross_domain_summary', {}).get('total_mappings', 0)}\n")

    print("News and calendar normalization reports generated successfully.")


if __name__ == "__main__":
    main()
