"""
Run ML Integration Batch

Runs the ML Context Integration pipeline across multiple symbols.
"""

import argparse
import logging
import pandas as pd
from config.settings import Settings
from config.symbols import get_symbol_spec, get_enabled_symbols
from config.paths import ensure_project_directories
from data.storage.data_lake import DataLake
from ml_integration.integration_pipeline import MLContextIntegrationPipeline
from ml_integration.integration_config import get_ml_integration_profile
from reports.report_builder import build_ml_integration_batch_report

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(description="ML Integration Batch Runner")
    parser.add_argument("--limit", type=int, default=None, help="Maximum number of symbols to process")
    parser.add_argument("--asset-class", type=str, default=None, help="Filter by asset class")
    parser.add_argument("--symbol", type=str, default=None, help="Run for specific symbol only")
    parser.add_argument("--timeframe", type=str, default="1d", help="Timeframe (e.g., 1d, 4h)")
    parser.add_argument("--profile", type=str, default="balanced_ml_context_integration", help="Integration profile name")
    parser.add_argument("--save", action="store_true", default=True, help="Save outputs to data lake")
    args = parser.parse_args()

    ensure_project_directories()
    settings = Settings()
    from config.paths import PROJECT_ROOT
    data_lake = DataLake(PROJECT_ROOT / 'data' / 'lake')

    try:
        profile = get_ml_integration_profile(args.profile)
    except Exception as e:
        logger.error(f"Error loading profile: {e}")
        return

    # Determine universe
    if args.symbol:
        spec = get_symbol_spec(args.symbol)
        if not spec:
            logger.error(f"Symbol {args.symbol} not found")
            return
        specs = [spec]
    else:
        specs = get_enabled_symbols()
        if args.asset_class:
            specs = [s for s in specs if s.asset_class == args.asset_class]

    if not specs:
        logger.warning("No symbols to process.")
        return

    logger.info(f"Running ML Integration Batch for {len(specs)} symbols (Profile: {args.profile})")

    pipeline = MLContextIntegrationPipeline(data_lake, settings, profile)
    batch_summary = pipeline.build_for_universe(specs, args.timeframe, profile, args.limit, args.save)

    ranking_df = pd.DataFrame(batch_summary.get("symbols", []))
    report_str = build_ml_integration_batch_report(batch_summary, ranking_df)
    print("\n" + report_str)

    if args.save and not ranking_df.empty:
        from config.paths import REPORTS_ML_INTEGRATION_REPORTS_DIR
        out_txt = REPORTS_ML_INTEGRATION_REPORTS_DIR / "ml_integration_batch_summary.txt"
        out_csv = REPORTS_ML_INTEGRATION_REPORTS_DIR / "ml_integration_batch_summary.csv"

        with open(out_txt, "w") as f:
            f.write(report_str)
        ranking_df.to_csv(out_csv, index=False)
        logger.info(f"Saved batch reports to {out_txt.parent}")


if __name__ == "__main__":
    main()
