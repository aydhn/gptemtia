import argparse
import sys
from pathlib import Path
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from commodity_fx_signal_bot.config.settings import settings
from commodity_fx_signal_bot.config.paths import ProjectPaths
from commodity_fx_signal_bot.data.storage.data_lake import DataLake
from commodity_fx_signal_bot.symbols import get_symbol_spec
from commodity_fx_signal_bot.ml.prediction_pipeline import MLPredictionPipeline
from commodity_fx_signal_bot.ml.prediction_config import get_ml_prediction_profile
from commodity_fx_signal_bot.reports.report_builder import build_ml_prediction_preview_report

def main():
    parser = argparse.ArgumentParser(description="Run ML Prediction Preview")
    parser.add_argument("--symbol", type=str, required=True, help="Symbol to predict")
    parser.add_argument("--timeframe", type=str, default="1d", help="Timeframe (default: 1d)")
    parser.add_argument("--profile", type=str, default="balanced_offline_prediction", help="Prediction profile")
    parser.add_argument("--model-id", type=str, help="Optional specific model ID")
    parser.add_argument("--save", action="store_true", help="Save predictions")
    parser.add_argument("--tail", type=int, default=20, help="Number of rows to show")

    args = parser.parse_args()

    paths = ProjectPaths()
    lake = DataLake(paths)

    spec = get_symbol_spec(args.symbol)
    if not spec:
        print(f"Error: Symbol {args.symbol} not found.")
        sys.exit(1)

    try:
        profile = get_ml_prediction_profile(args.profile)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

    pipeline = MLPredictionPipeline(lake, settings, profile)

    print(f"Running ML Prediction Pipeline for {args.symbol} {args.timeframe} (Profile: {profile.name})...")

    if args.model_id:
        print(f"Warning: Individual model prediction not fully implemented in CLI yet. Running full pipeline.")

    pool_df, summary = pipeline.run_for_symbol_timeframe(spec, args.timeframe, profile, save=args.save)

    tail_df = pd.DataFrame()
    if not pool_df.empty:
        tail_df = pool_df.tail(args.tail)

    report_str = build_ml_prediction_preview_report(args.symbol, args.timeframe, profile.name, summary, tail_df)

    print("\n" + report_str)

    report_file = paths.reports_output / "ml_prediction_reports" / f"ml_prediction_preview_{args.symbol}_{args.timeframe}_{profile.name}.txt"
    report_file.parent.mkdir(parents=True, exist_ok=True)
    with open(report_file, "w", encoding="utf-8") as f:
        f.write(report_str)

    print(f"\nReport saved to {report_file}")

if __name__ == "__main__":
    main()
