import argparse
import pandas as pd
from data.storage.data_lake import DataLake
from config.settings import settings
from config.paths import ProjectPaths
from ml.dataset_pipeline import MLDatasetPipeline
from ml.dataset_config import get_ml_dataset_profile
from reports.report_builder import ReportBuilder
from core.universe_manager import UniverseManager

def main():
    parser = argparse.ArgumentParser(description="Batch build ML Datasets")
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--asset-class", type=str, default=None)
    parser.add_argument("--symbol", type=str, default=None)
    parser.add_argument("--timeframe", type=str, default=settings.default_ml_dataset_timeframe)
    parser.add_argument("--profile", type=str, default=settings.default_ml_dataset_profile)
    parser.add_argument("--save", action="store_true", default=True)
    args = parser.parse_args()

    paths = ProjectPaths()
    data_lake = DataLake(paths)
    report_builder = ReportBuilder()

    universe_manager = UniverseManager()

    try:
        profile = get_ml_dataset_profile(args.profile)
    except Exception as e:
        print(f"Error loading profile: {e}")
        return

    # Filter specs
    all_specs = universe_manager.get_enabled_symbols()
    specs_to_process = []

    for s in all_specs:
         if args.symbol and s.symbol != args.symbol:
              continue
         if getattr(args, 'asset_class', None) and s.asset_class != getattr(args, 'asset_class'):
              continue
         specs_to_process.append(s)

    pipeline = MLDatasetPipeline(data_lake, settings, profile)

    print(f"Starting batch build for {len(specs_to_process)} symbols...")

    summary = pipeline.build_for_universe(
         specs_to_process, args.timeframe, profile, args.limit, args.save
    )

    results = summary.get("results", [])
    ranking_df = pd.DataFrame(results) if results else pd.DataFrame()

    report = report_builder.build_ml_dataset_batch_report(summary, ranking_df)
    print(report)

    paths.ml_reports.mkdir(parents=True, exist_ok=True)

    report_path = paths.ml_reports / "ml_dataset_batch_summary.txt"
    with open(report_path, "w", encoding="utf-8") as f:
         f.write(report)

    if not ranking_df.empty:
         csv_path = paths.ml_reports / "ml_dataset_batch_summary.csv"
         ranking_df.to_csv(csv_path, index=False)
         print(f"\nSaved CSV to: {csv_path}")

if __name__ == "__main__":
    main()
