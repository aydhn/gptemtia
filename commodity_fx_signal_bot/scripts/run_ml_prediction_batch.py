import argparse
import sys
from pathlib import Path
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from commodity_fx_signal_bot.config.settings import settings
from commodity_fx_signal_bot.config.paths import ProjectPaths
from commodity_fx_signal_bot.data.storage.data_lake import DataLake
from commodity_fx_signal_bot.symbols import get_symbol_spec, list_all_symbols
from commodity_fx_signal_bot.ml.prediction_pipeline import MLPredictionPipeline
from commodity_fx_signal_bot.ml.prediction_config import get_ml_prediction_profile
from commodity_fx_signal_bot.reports.report_builder import build_ml_prediction_batch_report

def main():
    parser = argparse.ArgumentParser(description="Run ML Prediction Batch")
    parser.add_argument("--symbol", type=str, help="Specific symbol to process")
    parser.add_argument("--asset-class", type=str, help="Filter by asset class")
    parser.add_argument("--limit", type=int, help="Limit number of symbols")
    parser.add_argument("--timeframe", type=str, default="1d", help="Timeframe (default: 1d)")
    parser.add_argument("--profile", type=str, default="balanced_offline_prediction", help="Prediction profile")
    parser.add_argument("--save", action="store_true", default=True, help="Save predictions")

    args = parser.parse_args()

    paths = ProjectPaths()
    lake = DataLake(paths)

    try:
        profile = get_ml_prediction_profile(args.profile)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

    specs = []
    if args.symbol:
        spec = get_symbol_spec(args.symbol)
        if spec:
            specs = [spec]
    else:
        all_specs = list_all_symbols()
        if args.asset_class:
            specs = [s for s in all_specs if s.asset_class.lower() == args.asset_class.lower()]
        else:
            specs = all_specs

    if not specs:
        print("No valid symbols found.")
        sys.exit(1)

    print(f"Running ML Prediction Batch for {len(specs)} symbols (Timeframe: {args.timeframe}, Profile: {profile.name})...")

    pipeline = MLPredictionPipeline(lake, settings, profile)

    result = pipeline.run_for_universe(specs, args.timeframe, profile, limit=args.limit, save=args.save)

    batch_results = result.get("batch_results", [])

    ranking_data = []
    for res in batch_results:
        q = res.get("quality_report", {})
        ranking_data.append({
            "symbol": res.get("symbol", "unknown"),
            "asset_class": res.get("asset_class", "unknown"),
            "selected_model_count": res.get("selected_model_count", 0),
            "successful_model_count": res.get("successful_model_count", 0),
            "prediction_candidate_count": res.get("prediction_candidate_count", 0),
            "ensemble_available": res.get("ensemble_available", False),
            "quality_passed": q.get("passed", False),
            "warnings": len(res.get("warnings", []))
        })

    ranking_df = pd.DataFrame(ranking_data)

    report_str = build_ml_prediction_batch_report(result, ranking_df)
    print("\n" + report_str)

    out_dir = paths.reports_output / "ml_prediction_reports"
    out_dir.mkdir(parents=True, exist_ok=True)

    report_file = out_dir / "ml_prediction_batch_summary.txt"
    with open(report_file, "w", encoding="utf-8") as f:
        f.write(report_str)

    csv_file = out_dir / "ml_prediction_batch_summary.csv"
    if not ranking_df.empty:
        ranking_df.to_csv(csv_file, index=False)

    print(f"\nBatch report saved to {report_file} and {csv_file}")

if __name__ == "__main__":
    main()
