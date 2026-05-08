import argparse
import logging
import sys

import pandas as pd

from config.paths import VOLATILITY_REPORTS_DIR
from config.symbols import get_enabled_symbols, get_symbol_spec
from data.storage.data_lake import DataLake
from ml.feature_store import FeatureStore
from reports.report_builder import build_volatility_status_report

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Check status of volatility features in Data Lake."
    )
    return parser.parse_args()


def main():
    args = parse_args()

    specs = get_enabled_symbols()

    from config.paths import DATA_DIR

    lake = DataLake(DATA_DIR)
    feature_store = FeatureStore(lake)

    status_data = []

    logger.info("Scanning volatility features status...")

    summary = {
        "total_symbols": len(specs),
        "with_volatility_features": 0,
        "with_volatility_events": 0,
        "missing_but_have_processed": 0,
        "missing_but_have_technical": 0,
    }

    for spec in specs:
        # Check available timeframes for processed data
        processed_tfs = lake.list_available_timeframes(spec)
        tech_tfs = lake.list_feature_timeframes(spec, "technical")

        # We'll check the default timeframes or the ones that exist
        tfs_to_check = set(processed_tfs + tech_tfs)
        if not tfs_to_check:
            tfs_to_check = {"1d"}  # Default fallback

        for tf in tfs_to_check:
            has_volatility = lake.has_features(spec, tf, "volatility")
            has_events = lake.has_features(spec, tf, "volatility_events")
            has_processed = lake.has_processed_ohlcv(spec, tf)
            has_tech = lake.has_features(spec, tf, "technical")

            row = {
                "symbol": spec.symbol,
                "asset_class": spec.asset_class,
                "timeframe": tf,
                "has_volatility_features": has_volatility,
                "has_volatility_events": has_events,
                "has_processed": has_processed,
                "has_technical": has_tech,
                "rows": 0,
                "cols": 0,
                "event_cols": 0,
                "nan_ratio": 0.0,
            }

            if has_volatility:
                summary["with_volatility_features"] += 1
                try:
                    df = feature_store.load_volatility_features(spec, tf)
                    row["rows"] = len(df)
                    row["cols"] = len(df.columns)
                    row["nan_ratio"] = df.isna().mean().mean() if not df.empty else 0.0
                except Exception as e:
                    logger.error(
                        f"Error loading {spec.symbol} volatility features: {e}"
                    )

            if has_events:
                summary["with_volatility_events"] += 1
                try:
                    event_df = feature_store.load_volatility_events(spec, tf)
                    row["event_cols"] = len(event_df.columns)
                except Exception:
                    report_builder = ReportBuilder()

            if not has_volatility and has_processed:
                summary["missing_but_have_processed"] += 1

            if not has_volatility and has_tech:
                summary["missing_but_have_technical"] += 1

            status_data.append(row)

    df_status = pd.DataFrame(status_data)

    report = build_volatility_status_report(df_status, summary)

    VOLATILITY_REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    report_file = VOLATILITY_REPORTS_DIR / "volatility_status_report.txt"
    csv_file = VOLATILITY_REPORTS_DIR / "volatility_status.csv"

    with open(report_file, "w", encoding="utf-8") as f:
        f.write(report)

    df_status.to_csv(csv_file, index=False)

    print(report)
    print(f"\nReports saved to {VOLATILITY_REPORTS_DIR}")


if __name__ == "__main__":
    main()
