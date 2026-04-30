import argparse
import logging
import sys
import pandas as pd

from config.paths import ensure_project_directories
from config.symbols import DEFAULT_SYMBOL_UNIVERSE
from data.storage.data_lake import DataLake
from reports.report_builder import build_mean_reversion_status_report, save_text_report

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def parse_args():
    parser = argparse.ArgumentParser(description="Mean Reversion Data Lake Status")
    parser.add_argument("--profile", type=str, default="balanced_swing")
    return parser.parse_args()


def main():
    ensure_project_directories()
    args = parse_args()

    lake = DataLake()

    from config.symbols import get_profile_timeframes

    try:
        tfs = get_profile_timeframes(args.profile)
    except:
        tfs = ["1d"]

    specs = [
        s
        for s in DEFAULT_SYMBOL_UNIVERSE
        if s.asset_class not in ("macro", "synthetic")
    ]

    rows = []

    for spec in specs:
        for tf in tfs:
            has_proc = lake.has_processed_ohlcv(spec, tf)
            has_raw = lake.has_ohlcv(spec, tf)
            has_tech = lake.has_features(spec, tf, "technical")
            has_mr = lake.has_features(spec, tf, "mean_reversion")
            has_mrev = lake.has_features(spec, tf, "mean_reversion_events")

            rows.append(
                {
                    "symbol": spec.symbol,
                    "timeframe": tf,
                    "has_processed": has_proc,
                    "has_raw": has_raw,
                    "has_technical": has_tech,
                    "has_mean_reversion_features": has_mr,
                    "has_mean_reversion_events": has_mrev,
                }
            )

    df = pd.DataFrame(rows)

    summary = {
        "total_symbols": len(df),
        "with_mean_reversion_features": df["has_mean_reversion_features"].sum(),
        "with_mean_reversion_events": df["has_mean_reversion_events"].sum(),
        "missing_but_have_processed": df[
            (~df["has_mean_reversion_features"]) & df["has_processed"]
        ].shape[0],
        "missing_but_have_technical": df[
            (~df["has_mean_reversion_features"]) & df["has_technical"]
        ].shape[0],
    }

    report_text = build_mean_reversion_status_report(df, summary)
    print("\n" + report_text)

    from config.paths import MEAN_REVERSION_REPORTS_DIR

    MEAN_REVERSION_REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    report_path = MEAN_REVERSION_REPORTS_DIR / "mean_reversion_status_report.txt"
    save_text_report(report_text, report_path)

    csv_path = MEAN_REVERSION_REPORTS_DIR / "mean_reversion_status.csv"
    df.to_csv(csv_path, index=False)

    logger.info(f"Saved status reports to {MEAN_REVERSION_REPORTS_DIR}")


if __name__ == "__main__":
    main()
