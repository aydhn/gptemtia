import logging

import pandas as pd

from config.symbols import get_allowed_timeframes_for_symbol, get_enabled_symbols
from data.storage.data_lake import DataLake
from reports.report_builder import build_momentum_status_report

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    lake = DataLake()
    specs = get_enabled_symbols()
    rows = []
    for spec in specs:
        timeframes = get_allowed_timeframes_for_symbol(spec)
        for tf in timeframes:
            has_raw = lake.has_ohlcv(spec, tf)
            has_processed = lake.has_processed_ohlcv(spec, tf)
            has_tech = lake.has_features(spec, tf, "technical")
            has_mom = lake.has_features(spec, tf, "momentum")
            rows.append(
                {
                    "Symbol": spec.symbol,
                    "Timeframe": tf,
                    "Has Raw": has_raw,
                    "Has Processed": has_processed,
                    "Has Technical": has_tech,
                    "Has Momentum": has_mom,
                }
            )
    df = pd.DataFrame(rows)
    summary = {
        "total_combinations": len(df),
        "missing_momentum": len(
            df[(df["Has Technical"] is True) & (df["Has Momentum"] is False)]
        ),
        "processed_without_momentum": len(
            df[(df["Has Processed"] is True) & (df["Has Momentum"] is False)]
        ),
    }
    report_str = build_momentum_status_report(df, summary)

    from config.paths import MOMENTUM_REPORTS_DIR

    MOMENTUM_REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    txt_path = MOMENTUM_REPORTS_DIR / "momentum_status_report.txt"
    with open(txt_path, "w") as f:
        f.write(report_str)
    csv_path = MOMENTUM_REPORTS_DIR / "momentum_status.csv"
    df.to_csv(csv_path, index=False)
    print(report_str)
    logger.info(f"Saved text report to {txt_path} and CSV to {csv_path}")


if __name__ == "__main__":
    main()
