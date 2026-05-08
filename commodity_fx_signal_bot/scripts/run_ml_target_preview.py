import argparse
from config.symbols import SymbolSpec
from data.storage.data_lake import DataLake
from config.settings import settings
from config.paths import ProjectPaths
from ml.dataset_config import get_ml_dataset_profile
from ml.target_engineering import build_target_frame
from reports.report_builder import ReportBuilder

def main():
    parser = argparse.ArgumentParser(description="Preview ML Targets for a symbol")
    parser.add_argument("--symbol", type=str, required=True)
    parser.add_argument("--timeframe", type=str, default="1d")
    parser.add_argument("--profile", type=str, default="balanced_supervised_dataset")
    parser.add_argument("--tail", type=int, default=20)
    args = parser.parse_args()

    paths = ProjectPaths()
    data_lake = DataLake(paths)
    report_builder = ReportBuilder()

    try:
        profile = get_ml_dataset_profile(args.profile)
    except Exception as e:
        print(f"Error loading profile: {e}")
        return

    df = data_lake.load_processed_ohlcv(args.symbol, args.timeframe)
    if df is None or df.empty:
         print(f"No OHLCV data for {args.symbol} {args.timeframe}")
         return

    candidate_df = None
    if "candidate_outcome" in profile.target_types:
         candidate_df = data_lake.load_signal_candidates(args.symbol, args.timeframe)

    targets, summary = build_target_frame(df, candidate_df, None, profile)

    tail_df = targets.tail(args.tail) if not targets.empty else None

    report = report_builder.build_ml_target_preview_report(
         args.symbol, args.timeframe, args.profile, summary, tail_df
    )

    print(report)

    report_path = paths.ml_reports / f"ml_target_preview_{args.symbol}_{args.timeframe}_{args.profile}.txt"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    with open(report_path, "w", encoding="utf-8") as f:
         f.write(report)
    print(f"\nReport saved to: {report_path}")

if __name__ == "__main__":
    main()
