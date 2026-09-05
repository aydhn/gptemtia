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
    build_symbol_normalization_markdown_report,
)


def main():
    ensure_project_directories()
    settings = Settings()
    profile = get_default_data_normalization_profile()
    lake = DataLake()
    pipeline = DataNormalizationPipeline(data_lake=lake, settings=settings, project_root=root, profile=profile)

    tables, summary = pipeline.run_symbol_indicator_event_tag_normalization(save=True)
    fx_df = tables.get("fx_symbol_report")
    comm_df = tables.get("commodity_symbol_report")
    macro_df = tables.get("macro_indicator_report")
    cal_df = tables.get("calendar_event_report")

    out_dir = root / "reports" / "output" / "advanced_data_normalization"
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "csv").mkdir(exist_ok=True)
    (out_dir / "markdown").mkdir(exist_ok=True)
    (out_dir / "txt").mkdir(exist_ok=True)

    if fx_df is not None:
        fx_df.to_csv(out_dir / "csv" / "fx_symbol_normalization_enforcement_report.csv", index=False)
    if comm_df is not None:
        comm_df.to_csv(out_dir / "csv" / "commodity_symbol_normalization_enforcement_report.csv", index=False)
    if macro_df is not None:
        macro_df.to_csv(out_dir / "csv" / "macro_indicator_normalization_enforcement_report.csv", index=False)
    if cal_df is not None:
        cal_df.to_csv(out_dir / "csv" / "calendar_event_normalization_enforcement_report.csv", index=False)

    md = build_symbol_normalization_markdown_report(summary.get("fx_symbol_summary", {}), fx_df)
    with open(out_dir / "markdown" / "symbol_normalization_report.md", "w", encoding="utf-8") as f:
        f.write(md)

    with open(out_dir / "txt" / "symbol_normalization_summary.txt", "w", encoding="utf-8") as f:
        f.write(f"FX Symbol Rules: {summary.get('fx_symbol_summary', {}).get('total_rules', 0)}\n")
        f.write(f"Commodity Symbol Rules: {summary.get('commodity_symbol_summary', {}).get('total_mappings', 0)}\n")
        f.write(f"Macro Indicators: {summary.get('macro_indicator_summary', {}).get('total_mappings', 0)}\n")
        f.write(f"Calendar Events: {summary.get('calendar_event_summary', {}).get('total_mappings', 0)}\n")

    print(f"Symbol normalization enforcement report generated successfully.")


if __name__ == "__main__":
    main()
