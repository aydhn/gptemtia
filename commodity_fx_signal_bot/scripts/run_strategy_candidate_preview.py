import argparse
import logging

from config.paths import LAKE_DIR, REPORTS_DIR
from config.settings import settings
from config.symbols import get_symbol_spec
from data.storage.data_lake import DataLake
from reports.report_builder import build_strategy_candidate_preview_report
from strategies.strategy_config import get_strategy_selection_profile
from strategies.strategy_pipeline import StrategyPipeline

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(
        description="Preview strategy candidates for a symbol"
    )
    parser.add_argument("--symbol", type=str, required=True, help="Symbol to analyze")
    parser.add_argument(
        "--timeframe", type=str, default="1d", help="Timeframe (default: 1d)"
    )
    parser.add_argument(
        "--profile",
        type=str,
        default="balanced_strategy_selection",
        help="Strategy profile",
    )
    parser.add_argument(
        "--last", type=int, default=10, help="Number of recent candidates to show"
    )
    parser.add_argument(
        "--save", action="store_true", help="Save features to data lake"
    )
    args = parser.parse_args()

    spec = get_symbol_spec(args.symbol)
    if not spec:
        logger.error(f"Symbol {args.symbol} not found")
        return

    data_lake = DataLake(LAKE_DIR)

    try:
        profile = get_strategy_selection_profile(args.profile)
    except Exception as e:
        logger.error(f"Error loading profile: {e}")
        return

    pipeline = StrategyPipeline(data_lake, settings, profile)

    df, summary = pipeline.build_for_symbol_timeframe(
        spec, args.timeframe, profile, save=args.save
    )

    if df.empty:
        logger.warning(f"No strategy candidates generated for {args.symbol}")
        if summary.get("missing_context_frames"):
            logger.warning(f"Missing context: {summary['missing_context_frames']}")
        return

    tail_df = df.tail(args.last)
    report = build_strategy_candidate_preview_report(
        args.symbol, args.timeframe, args.profile, summary, tail_df
    )

    print("\n" + report + "\n")

    out_dir = REPORTS_DIR / "strategy_reports"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = (
        out_dir
        / f"strategy_candidate_preview_{args.symbol}_{args.timeframe}_{args.profile}.txt"
    )
    out_file.write_text(report, encoding="utf-8")
    logger.info(f"Report saved to {out_file}")


if __name__ == "__main__":
    main()
