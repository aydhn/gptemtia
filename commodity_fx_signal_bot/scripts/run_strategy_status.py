import logging

import pandas as pd

from config.paths import LAKE_DIR, REPORTS_DIR
from config.symbols import get_enabled_symbols
from data.storage.data_lake import DataLake
from reports.report_builder import build_strategy_status_report

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def main():
    data_lake = DataLake(LAKE_DIR)
    specs = get_enabled_symbols()

    status_list = []

    for spec in specs:
        if spec.asset_class in ("synthetic", "macro", "benchmark"):
            continue

        timeframes = data_lake.list_feature_timeframes(spec, "strategy_candidates")
        for tf in timeframes:
            try:
                df = data_lake.load_features(spec, tf, "strategy_candidates")
                if not df.empty:
                    report_builder = ReportBuilder()ed = (
                        df[df["report_builder = ReportBuilder()ed_strategy_filters"] == True]
                        if "report_builder = ReportBuilder()ed_strategy_filters" in df.columns
                        else pd.DataFrame()
                    )
                    status_list.append(
                        {
                            "symbol": spec.symbol,
                            "timeframe": tf,
                            "candidate_count": len(df),
                            "report_builder = ReportBuilder()ed_count": len(report_builder = ReportBuilder()ed),
                            "latest_timestamp": (
                                str(df.index.max()) if not df.index.empty else "N/A"
                            ),
                        }
                    )
            except Exception as e:
                logger.debug(f"Error loading {spec.symbol} {tf}: {e}")

    status_df = pd.DataFrame(status_list)
    summary = {}

    report = build_strategy_status_report(status_df, summary)
    print("\n" + report + "\n")

    out_dir = REPORTS_DIR / "strategy_reports"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / "strategy_status_report.txt"
    out_file.write_text(report, encoding="utf-8")

    if not status_df.empty:
        csv_file = out_dir / "strategy_status.csv"
        status_df.to_csv(csv_file, index=False)

    logger.info("Status report saved")


if __name__ == "__main__":
    main()
