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
    build_time_frequency_unit_markdown_report,
)


def main():
    ensure_project_directories()
    settings = Settings()
    profile = get_default_data_normalization_profile()
    lake = DataLake()
    pipeline = DataNormalizationPipeline(data_lake=lake, settings=settings, project_root=root, profile=profile)

    tables, summary = pipeline.run_region_time_frequency_unit_normalization(save=True)
    num_tables, num_sum = pipeline.run_numeric_string_duplicate_normalization(save=True)

    reg_df = tables.get("region_currency_registry")
    ts_df = tables.get("timestamp_timezone_registry")
    sess_df = tables.get("session_alignment_registry")
    freq_df = tables.get("frequency_registry")
    unit_df = tables.get("unit_registry")

    num_df = num_tables.get("numeric_type_registry")
    str_df = num_tables.get("string_slug_registry")
    dup_df = num_tables.get("duplicate_key_registry")

    out_dir = root / "reports" / "output" / "advanced_data_normalization"
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "csv").mkdir(exist_ok=True)
    (out_dir / "markdown").mkdir(exist_ok=True)
    (out_dir / "txt").mkdir(exist_ok=True)

    if reg_df is not None:
        reg_df.to_csv(out_dir / "csv" / "region_country_currency_normalization_registry.csv", index=False)
    if ts_df is not None:
        ts_df.to_csv(out_dir / "csv" / "timestamp_timezone_normalization_registry.csv", index=False)
    if sess_df is not None:
        sess_df.to_csv(out_dir / "csv" / "session_alignment_requirement_registry.csv", index=False)
    if freq_df is not None:
        freq_df.to_csv(out_dir / "csv" / "frequency_normalization_registry.csv", index=False)
    if unit_df is not None:
        unit_df.to_csv(out_dir / "csv" / "unit_normalization_registry.csv", index=False)
    if num_df is not None:
        num_df.to_csv(out_dir / "csv" / "numeric_type_normalization_registry.csv", index=False)
    if str_df is not None:
        str_df.to_csv(out_dir / "csv" / "string_case_slug_normalization_registry.csv", index=False)
    if dup_df is not None:
        dup_df.to_csv(out_dir / "csv" / "duplicate_key_normalization_registry.csv", index=False)

    md = build_time_frequency_unit_markdown_report(summary.get("timestamp_timezone_summary", {}), ts_df)
    with open(out_dir / "markdown" / "time_frequency_unit_report.md", "w", encoding="utf-8") as f:
        f.write(md)

    with open(out_dir / "txt" / "time_frequency_unit_summary.txt", "w", encoding="utf-8") as f:
        f.write(f"Region/Currency Mappings: {summary.get('region_currency_summary', {}).get('total_mappings', 0)}\n")
        f.write(f"Frequencies: {summary.get('frequency_summary', {}).get('total_mappings', 0)}\n")
        f.write(f"Units: {summary.get('unit_summary', {}).get('total_mappings', 0)}\n")

    print("Time, frequency and unit normalization registry generated successfully.")


if __name__ == "__main__":
    main()
