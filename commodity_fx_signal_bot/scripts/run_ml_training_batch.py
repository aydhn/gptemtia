import argparse
import sys
import logging
import pandas as pd
from config.settings import settings
from config.paths import ProjectPaths
from config.symbols import get_enabled_symbols, get_symbol_spec
from data.storage.data_lake import DataLake
from ml.training_config import get_ml_training_profile
from ml.training_pipeline import MLTrainingPipeline
import reports.report_builder as report_builder

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def main():
    parser = argparse.ArgumentParser(description="ML Baseline Batch Training")
    parser.add_argument("--limit", type=int, default=None, help="Limit number of symbols to process")
    parser.add_argument("--asset-class", type=str, default=None, help="Filter by asset class")
    parser.add_argument("--symbol", type=str, default=None, help="Single symbol to process")
    parser.add_argument("--timeframe", type=str, default="1d", help="Timeframe (e.g. 1d)")
    parser.add_argument("--profile", type=str, default="balanced_baseline_training", help="Training profile name")
    parser.add_argument("--model-family", type=str, default=None, help="Model family to force")
    parser.add_argument("--save", action="store_true", default=True, help="Save artifacts and registry entry")
    parser.add_argument("--no-save", action="store_false", dest="save", help="Do not save artifacts")

    args = parser.parse_args()

    if args.symbol:
        spec = get_symbol_spec(args.symbol)
        if not spec:
            print(f"Symbol {args.symbol} not found")
            sys.exit(1)
        specs = [spec]
    else:
        specs = get_enabled_symbols()
        if args.asset_class:
            specs = [s for s in specs if s.asset_class == args.asset_class]

    try:
        profile = get_ml_training_profile(args.profile)
    except Exception as e:
        print(f"Error loading profile {args.profile}: {e}")
        sys.exit(1)

    paths = ProjectPaths()
    data_lake = DataLake(paths)

    pipeline = MLTrainingPipeline(data_lake, settings, profile)

    res = pipeline.train_for_universe(
        specs=specs,
        timeframe=args.timeframe,
        profile=profile,
        model_family=args.model_family,
        limit=args.limit,
        save=args.save
    )

    report = report_builder.build_ml_training_batch_report(res, res.get("ranking_df"))
    print(report)

    out_path_txt = paths.ml_training_reports / "ml_training_batch_summary.txt"
    with open(out_path_txt, "w") as f:
        f.write(report)

    df = res.get("ranking_df")
    if df is not None and not df.empty:
        out_path_csv = paths.ml_training_reports / "ml_training_batch_summary.csv"
        df.to_csv(out_path_csv, index=False)
        print(f"Saved CSV summary to {out_path_csv}")

if __name__ == "__main__":
    main()
