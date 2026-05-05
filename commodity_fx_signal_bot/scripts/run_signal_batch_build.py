import argparse
import logging
import pandas as pd
from config.settings import settings
from config.symbols import get_enabled_symbols
from data.storage.data_lake import DataLake
from signals.signal_config import get_signal_scoring_profile
from signals.signal_pipeline import SignalPipeline
from reports.report_builder import build_signal_batch_report
from config.paths import SIGNAL_REPORTS_DIR

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--asset-class", type=str, default=None)
    parser.add_argument("--symbol", type=str, default=None)
    parser.add_argument("--timeframe", type=str, default="1d")
    parser.add_argument("--profile", type=str, default="balanced_candidate_scoring")
    parser.add_argument("--no-save", action="store_true", default=False)
    return parser.parse_args()


def main():
    args = parse_args()
    from config.paths import DATA_DIR

    lake = DataLake(DATA_DIR)
    prof = get_signal_scoring_profile(args.profile)
    pipeline = SignalPipeline(lake, settings, prof)

    specs = get_enabled_symbols()
    if args.symbol:
        specs = [s for s in specs if s.symbol == args.symbol]
    elif args.asset_class:
        specs = [s for s in specs if s.asset_class == args.asset_class]

    summary = pipeline.build_for_universe(
        specs, args.timeframe, prof, limit=args.limit, save=not args.no_save
    )

    report = build_signal_batch_report(summary)
    print(report)

    out_path = SIGNAL_REPORTS_DIR / "signal_batch_summary.txt"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        f.write(report)

    df_sum = pd.DataFrame([summary])
    df_sum.to_csv(SIGNAL_REPORTS_DIR / "signal_batch_summary.csv", index=False)

    logger.info(f"Batch completed. Saved to {out_path}")


if __name__ == "__main__":
    main()
