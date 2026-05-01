import logging
from pathlib import Path

import pandas as pd

from config.paths import ensure_project_directories, DIVERGENCE_REPORTS_DIR
from config.settings import settings
from config.symbols import get_enabled_symbols
from config.symbols import get_allowed_timeframes_for_symbol
from data.storage.data_lake import DataLake
from ml.feature_store import FeatureStore
from reports.report_builder import build_divergence_status_report

logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(level=logging.INFO)
    ensure_project_directories()

    lake = DataLake()

    logger.info("Starting Divergence Status Check...")

    rows = []

    for spec in get_enabled_symbols():
        if spec.symbol_type in ["macro", "synthetic"]:
            continue

        timeframes = get_allowed_timeframes_for_symbol(spec)
        for tf in timeframes:
            has_raw = lake.has_ohlcv(spec, tf)
            has_processed = lake.has_processed_ohlcv(spec, tf)
            has_technical = lake.has_features(spec, tf, "technical")
            has_divergence = lake.has_features(spec, tf, "divergence")
            has_divergence_events = lake.has_features(spec, tf, "divergence_events")

            rows.append(
                {
                    "symbol": spec.name,
                    "timeframe": tf,
                    "has_raw": has_raw,
                    "has_processed": has_processed,
                    "has_technical": has_technical,
                    "has_divergence": has_divergence,
                    "has_divergence_events": has_divergence_events,
                }
            )

    status_df = pd.DataFrame(rows)

    summary = {
        "total_symbols": len(get_enabled_symbols()),
        "with_divergence": status_df["has_divergence"].sum(),
        "missing_but_has_technical": status_df[
            status_df["has_technical"] & ~status_df["has_divergence"]
        ].shape[0],
    }

    DIVERGENCE_REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    # Save CSV
    csv_path = DIVERGENCE_REPORTS_DIR / "divergence_status.csv"
    status_df.to_csv(csv_path, index=False)

    # Text Report
    report_text = build_divergence_status_report(status_df, summary)
    txt_path = DIVERGENCE_REPORTS_DIR / "divergence_status_report.txt"

    with open(txt_path, "w") as f:
        f.write(report_text)

    print(report_text)
    logger.info(f"Status check complete. Results saved to {DIVERGENCE_REPORTS_DIR}")


if __name__ == "__main__":
    main()
