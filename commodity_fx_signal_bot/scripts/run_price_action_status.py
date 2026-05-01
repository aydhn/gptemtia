import logging

import pandas as pd

from config.paths import PRICE_ACTION_REPORTS_DIR
from config.symbols import get_enabled_symbols
from data.storage.data_lake import DataLake
from reports.report_builder import build_price_action_status_report

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


def main():
    lake = DataLake()
    specs = get_enabled_symbols()

    rows = []

    for spec in specs:
        if spec.symbol_type in ["macro", "synthetic"]:
            continue

        tech_tfs = lake.list_feature_timeframes(spec, "technical")
        proc_tfs = (
            lake.list_processed_timeframes(spec)
            if hasattr(lake, "list_processed_timeframes")
            else []
        )
        pa_tfs = lake.list_feature_timeframes(spec, "price_action")
        ev_tfs = lake.list_feature_timeframes(spec, "price_action_events")

        # We'll just check common timeframes
        for tf in ["1d", "4h", "1h"]:
            has_tech = tf in tech_tfs
            has_proc = tf in proc_tfs
            has_pa = tf in pa_tfs
            has_ev = tf in ev_tfs

            row = {
                "symbol": spec.name,
                "asset_class": spec.asset_class,
                "timeframe": tf,
                "has_processed": has_proc,
                "has_technical": has_tech,
                "has_price_action": has_pa,
                "has_events": has_ev,
                "rows": 0,
                "pa_columns": 0,
                "event_columns": 0,
                "nan_ratio": 0.0,
            }

            if has_pa:
                pa_df = lake.load_features(spec, tf, "price_action")
                row["rows"] = len(pa_df)
                row["pa_columns"] = len(pa_df.columns)
                if len(pa_df) > 0:
                    row["nan_ratio"] = pa_df.isna().sum().sum() / (
                        pa_df.shape[0] * pa_df.shape[1]
                    )

            if has_ev:
                ev_df = lake.load_features(spec, tf, "price_action_events")
                row["event_columns"] = len(ev_df.columns)

            rows.append(row)

    df = pd.DataFrame(rows)

    # Generate report text
    summary = {
        "total_symbols": len(
            [s for s in specs if s.symbol_type not in ["macro", "synthetic"]]
        ),
        "with_price_action": len(df[df["has_price_action"]]["symbol"].unique()),
        "missing_but_has_technical": len(
            df[df["has_technical"] & ~df["has_price_action"]]
        ),
        "total_timeframes": len(df),
        "timeframes_with_features": len(df[df["has_price_action"]]),
    }

    report_text = build_price_action_status_report(df, summary)

    PRICE_ACTION_REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    txt_path = PRICE_ACTION_REPORTS_DIR / "price_action_status_report.txt"
    csv_path = PRICE_ACTION_REPORTS_DIR / "price_action_status.csv"

    with open(txt_path, "w") as f:
        f.write(report_text)

    df.to_csv(csv_path, index=False)

    logger.info(f"Status report saved to {txt_path}")
    logger.info(f"Status CSV saved to {csv_path}")


if __name__ == "__main__":
    main()
