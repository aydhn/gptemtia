import argparse
import logging
from typing import Optional

import pandas as pd

from config.paths import LAKE_DIR, TREND_REPORTS_DIR
from config.scan_config import get_scan_profile
from config.settings import settings
from config.symbols import DEFAULT_SYMBOL_UNIVERSE
from data.storage.data_lake import DataLake
from ml.feature_store import FeatureStore
from reports.report_builder import build_trend_status_report

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Check Trend Features Status in Data Lake"
    )
    parser.add_argument(
        "--profile",
        type=str,
        default=settings.default_scan_profile,
        help="Scan profile",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    lake = DataLake(LAKE_DIR)
    fs = FeatureStore(lake)
    profile = get_scan_profile(args.profile)

    records = []

    for spec in DEFAULT_SYMBOL_UNIVERSE:
        # Ignore synthetic/macro mostly
        if spec.asset_class in ("synthetic", "macro") and getattr(
            settings, "skip_macro_downloads_in_ohlcv_pipeline", True
        ):
            continue

        for tf in profile.timeframes:
            has_raw = lake.has_ohlcv(spec, tf)
            has_processed = lake.has_processed_ohlcv(spec, tf)
            has_tech = lake.has_features(spec, tf, "technical")
            has_trend = lake.has_features(spec, tf, "trend")
            has_trend_events = lake.has_features(spec, tf, "trend_events")

            records.append(
                {
                    "Symbol": spec.symbol,
                    "Timeframe": tf,
                    "Has Raw": has_raw,
                    "Has Processed": has_processed,
                    "Has Technical": has_tech,
                    "Has Trend": has_trend,
                    "Has Events": has_trend_events,
                }
            )

    df = pd.DataFrame(records)

    summary = {
        "total_combinations": len(df),
        "missing_trend": int(
            len(df[(df["Has Technical"] == True) & (df["Has Trend"] == False)])
        ),
        "processed_without_trend": int(
            len(df[(df["Has Processed"] == True) & (df["Has Trend"] == False)])
        ),
    }

    report_str = build_trend_status_report(df, summary)
    print("\n" + report_str)

    TREND_REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    out_file = TREND_REPORTS_DIR / "trend_status_report.txt"
    with open(out_file, "w") as f:
        f.write(report_str)

    csv_file = TREND_REPORTS_DIR / "trend_status.csv"
    df.to_csv(csv_file, index=False)

    logger.info(f"Report saved to {out_file} and {csv_file}")


if __name__ == "__main__":
    main()
