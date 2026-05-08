import argparse
import sys
from pathlib import Path
from config.symbols import SymbolSpec
from data.storage.data_lake import DataLake
from config.settings import settings
from config.paths import ProjectPaths
from ml.dataset_pipeline import MLDatasetPipeline
from ml.dataset_config import get_ml_dataset_profile
from reports.report_builder import ReportBuilder

def main():
    parser = argparse.ArgumentParser(description="Preview ML Dataset for a symbol")
    parser.add_argument("--symbol", type=str, required=True, help="Symbol to build dataset for (e.g. GC=F)")
    parser.add_argument("--timeframe", type=str, default=settings.default_ml_dataset_timeframe, help="Timeframe")
    parser.add_argument("--profile", type=str, default=settings.default_ml_dataset_profile, help="Dataset profile name")
    parser.add_argument("--save", action="store_true", help="Save outputs to data lake")
    parser.add_argument("--tail", type=int, default=10, help="Number of rows to preview")
    args = parser.parse_args()

    paths = ProjectPaths()
    data_lake = DataLake(paths)
    report_builder = ReportBuilder()

    spec = SymbolSpec(symbol=args.symbol, asset_class="unknown")
    try:
        profile = get_ml_dataset_profile(args.profile)
    except Exception as e:
        print(f"Error loading profile: {e}")
        return

    pipeline = MLDatasetPipeline(data_lake, settings, profile)
    dataset, summary = pipeline.build_for_symbol_timeframe(spec, args.timeframe, save=args.save)

    tail_df = dataset.tail(args.tail) if not dataset.empty else None

    report = report_builder.build_ml_dataset_preview_report(
        args.symbol, args.timeframe, args.profile, summary, tail_df
    )

    print(report)

    report_path = paths.ml_reports / f"ml_dataset_preview_{args.symbol}_{args.timeframe}_{args.profile}.txt"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    with open(report_path, "w", encoding="utf-8") as f:
         f.write(report)
    print(f"\nReport saved to: {report_path}")

if __name__ == "__main__":
    main()
