"""
Run ML Context Integration Preview

Preview the ML Context Integration pipeline for a single symbol and timeframe.
"""

import argparse
import logging
from config.settings import Settings
from config.symbols import get_symbol_spec
from config.paths import ensure_project_directories
from data.storage.data_lake import DataLake
from ml_integration.integration_pipeline import MLContextIntegrationPipeline
from ml_integration.integration_config import get_ml_integration_profile
from reports.report_builder import build_ml_context_integration_preview_report

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(description="ML Context Integration Preview")
    parser.add_argument("--symbol", type=str, required=True, help="Target symbol")
    parser.add_argument("--timeframe", type=str, default="1d", help="Timeframe (e.g., 1d, 4h)")
    parser.add_argument("--profile", type=str, default="balanced_ml_context_integration", help="Integration profile name")
    parser.add_argument("--save", action="store_true", help="Save outputs to data lake")
    parser.add_argument("--tail", type=int, default=20, help="Number of rows to show in preview")
    args = parser.parse_args()

    ensure_project_directories()
    settings = Settings()
    from config.paths import PROJECT_ROOT
    data_lake = DataLake(PROJECT_ROOT / 'data' / 'lake')

    spec = get_symbol_spec(args.symbol)
    if not spec:
        logger.error(f"Symbol {args.symbol} not found in configuration.")
        return

    try:
        profile = get_ml_integration_profile(args.profile)
    except Exception as e:
        logger.error(f"Error loading profile: {e}")
        return

    logger.info(f"Running ML Context Integration preview for {args.symbol} ({args.timeframe}) using {args.profile}")

    pipeline = MLContextIntegrationPipeline(data_lake, settings, profile)
    summary, frames = pipeline.build_for_symbol_timeframe(spec, args.timeframe, profile, save=args.save)

    report_str = build_ml_context_integration_preview_report(args.symbol, args.timeframe, args.profile, summary)
    print("\n" + report_str)

    # Output to file
    if args.save:
        from config.paths import REPORTS_ML_INTEGRATION_REPORTS_DIR
        out_path = REPORTS_ML_INTEGRATION_REPORTS_DIR / f"ml_context_integration_preview_{args.symbol}_{args.timeframe}_{args.profile}.txt"
        with open(out_path, "w") as f:
            f.write(report_str)
        logger.info(f"Saved report to {out_path}")


if __name__ == "__main__":
    main()
