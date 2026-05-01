"""
Script to check the status of regime features across the data lake.
"""

import argparse
import logging
import pandas as pd

from config.symbols import DEFAULT_SYMBOL_UNIVERSE
from config.paths import REGIME_REPORTS_DIR
from data.storage.data_lake import DataLake
from reports.report_builder import build_regime_status_report, save_text_report, save_dataframe_report

logger = logging.getLogger(__name__)

def parse_args():
    parser = argparse.ArgumentParser(description="Check status of regime features.")
    return parser.parse_args()

def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    args = parse_args()

    lake = DataLake()

    tradeable_specs = [s for s in DEFAULT_SYMBOL_UNIVERSE if not s.is_synthetic() and not s.is_macro()]

    rows = []

    logger.info("Scanning data lake for regime status...")

    for spec in tradeable_specs:
        tfs = lake.list_available_timeframes(spec)
        for tf in tfs:
            has_tech = lake.has_features(spec, tf, "technical")
            has_regime = lake.has_features(spec, tf, "regime")
            has_events = lake.has_features(spec, tf, "regime_events")

            latest_label = "unknown"
            latest_conf = 0.0
            row_count = 0

            if has_regime:
                try:
                    df = lake.load_features(spec, tf, "regime")
                    row_count = len(df)
                    if "regime_primary_label" in df.columns and not df.empty:
                        latest_label = df["regime_primary_label"].iloc[-1]
                    if "regime_confidence" in df.columns and not df.empty:
                        latest_conf = float(df["regime_confidence"].iloc[-1])
                except Exception:
                    pass

            rows.append({
                "symbol": spec.symbol,
                "asset_class": spec.asset_class,
                "timeframe": tf,
                "has_technical": has_tech,
                "has_regime": has_regime,
                "has_regime_events": has_events,
                "row_count": row_count,
                "latest_regime": latest_label,
                "latest_confidence": latest_conf
            })

    df = pd.DataFrame(rows)

    summary = {
        "total_symbols": len(tradeable_specs)
    }

    report = build_regime_status_report(df, summary)
    print(report)

    txt_path = REGIME_REPORTS_DIR / "regime_status_report.txt"
    csv_path = REGIME_REPORTS_DIR / "regime_status.csv"

    save_text_report(report, txt_path)
    save_dataframe_report(df, csv_path)

    logger.info(f"Reports saved to {txt_path} and {csv_path}")

if __name__ == "__main__":
    main()
