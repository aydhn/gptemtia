import argparse
import logging
from data.storage.data_lake import DataLake
from signals.signal_pool import SignalCandidatePool
from reports.report_builder import build_signal_pool_preview_report
from config.paths import SIGNAL_REPORTS_DIR

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--timeframe", type=str, default="1d")
    parser.add_argument("--profile", type=str, default="balanced_candidate_scoring")
    parser.add_argument("--top", type=int, default=20)
    parser.add_argument("--rebuild", action="store_true", default=False)
    return parser.parse_args()


def main():
    args = parse_args()
    from config.paths import DATA_DIR

    lake = DataLake(DATA_DIR)

    if args.rebuild or not lake.has_signal_pool(args.timeframe, args.profile):
        logger.info("Rebuilding or pool not found. Building for universe...")
        from config.symbols import get_enabled_symbols
        from signals.signal_pipeline import SignalPipeline
        from config.settings import settings
        from signals.signal_config import get_signal_scoring_profile

        prof = get_signal_scoring_profile(args.profile)
        pipeline = SignalPipeline(lake, settings, prof)
        pipeline.build_for_universe(get_enabled_symbols(), args.timeframe, prof)

    df = lake.load_signal_pool(args.timeframe, args.profile)
    pool = SignalCandidatePool.from_dataframe(df)

    summary = pool.summarize()
    top_candidates = pool.rank(args.top)
    top_df = SignalCandidatePool()
    top_df.extend(top_candidates)

    report = build_signal_pool_preview_report(
        args.timeframe, args.profile, summary, top_df.to_dataframe()
    )
    print(report)

    out_path = (
        SIGNAL_REPORTS_DIR / f"signal_pool_preview_{args.timeframe}_{args.profile}.txt"
    )
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        f.write(report)

    logger.info(f"Pool preview saved to {out_path}")


if __name__ == "__main__":
    main()
