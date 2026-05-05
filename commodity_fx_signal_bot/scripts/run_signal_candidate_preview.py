import argparse
import logging
from config.settings import settings
from config.symbols import get_symbol_spec
from data.storage.data_lake import DataLake
from signals.signal_config import get_signal_scoring_profile
from signals.signal_pipeline import SignalPipeline
from reports.report_builder import build_signal_candidate_preview_report
from config.paths import SIGNAL_REPORTS_DIR

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--symbol", required=True, type=str)
    parser.add_argument("--timeframe", type=str, default="1d")
    parser.add_argument("--profile", type=str, default="balanced_candidate_scoring")
    parser.add_argument("--last", type=int, default=10)
    parser.add_argument("--save", action="store_true", default=False)
    return parser.parse_args()


def main():
    args = parse_args()
    spec = get_symbol_spec(args.symbol)
    if not spec:
        logger.error(f"Symbol not found: {args.symbol}")
        return

    from config.paths import DATA_DIR

    lake = DataLake(DATA_DIR)
    prof = get_signal_scoring_profile(args.profile)
    pipeline = SignalPipeline(lake, settings, prof)

    df, summary = pipeline.build_for_symbol_timeframe(
        spec, args.timeframe, prof, save=args.save
    )

    if df.empty:
        logger.info(f"No candidates generated for {args.symbol}")
        tail = df
    else:
        tail = df.tail(args.last)

    report = build_signal_candidate_preview_report(
        args.symbol, args.timeframe, args.profile, summary, tail
    )

    print(report)

    out_path = (
        SIGNAL_REPORTS_DIR
        / f"signal_candidate_preview_{args.symbol}_{args.timeframe}_{args.profile}.txt"
    )
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        f.write(report)
    logger.info(f"Report saved to {out_path}")


if __name__ == "__main__":
    main()
