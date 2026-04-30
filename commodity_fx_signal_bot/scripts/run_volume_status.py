import logging
import pandas as pd

from config.symbols import get_enabled_symbols
from config.symbols import get_allowed_timeframes_for_symbol
from data.storage.data_lake import DataLake
from config.paths import PROJECT_ROOT

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    lake = DataLake(PROJECT_ROOT / "data" / "lake")
    specs = get_enabled_symbols()

    records = []

    for spec in specs:
        tfs = get_allowed_timeframes_for_symbol(spec)
        for tf in tfs:
            has_raw = lake.has_ohlcv(spec, tf)
            has_proc = (
                lake.has_processed_ohlcv(spec, tf)
                if hasattr(lake, "has_processed_ohlcv")
                else lake.has_ohlcv(spec, tf)
            )
            has_tech = lake.has_features(spec, tf, "technical")
            has_vol = lake.has_features(spec, tf, "volume")
            has_vol_ev = lake.has_features(spec, tf, "volume_events")

            records.append(
                {
                    "symbol": spec.symbol,
                    "timeframe": tf,
                    "has_raw": has_raw,
                    "has_processed": has_proc,
                    "has_technical": has_tech,
                    "has_volume": has_vol,
                    "has_volume_events": has_vol_ev,
                }
            )

    df = pd.DataFrame(records)

    summary = {
        "total_symbols": len(specs),
        "total_combinations": len(df),
        "with_volume": df["has_volume"].sum(),
        "with_volume_events": df["has_volume_events"].sum(),
        "missing_but_have_processed": df[
            (~df["has_volume"]) & df["has_processed"]
        ].shape[0],
        "missing_but_have_technical": df[
            (~df["has_volume"]) & df["has_technical"]
        ].shape[0],
    }

    from config.paths import REPORTS_DIR
    from reports.report_builder import build_volume_status_report

    VOL_REPORTS_DIR = REPORTS_DIR / "volume_reports"
    VOL_REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    report = build_volume_status_report(df, summary)

    df.to_csv(VOL_REPORTS_DIR / "volume_status.csv", index=False)
    with open(VOL_REPORTS_DIR / "volume_status_report.txt", "w") as f:
        f.write(report)

    print(report)


if __name__ == "__main__":
    main()
