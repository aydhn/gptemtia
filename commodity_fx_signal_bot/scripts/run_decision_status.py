import argparse
import logging
from config.symbols import get_enabled_symbols
from data.storage.data_lake import DataLake
from config.paths import DECISION_REPORTS_DIR
import pandas as pd
from reports.report_builder import build_decision_status_report

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(description="Check decision pipeline status")
    args = parser.parse_args()

    data_lake = DataLake()
    specs = get_enabled_symbols()

    status_records = []

    # Check candidates
    for spec in specs:
        if spec.sub_class in ["Synthetic", "Macro", "Benchmark", "Macro Indicators"]:
            continue

        timeframes = data_lake.list_feature_timeframes(spec, "decision_candidates")
        for tf in timeframes:
            try:
                df = data_lake.load_features(spec, tf, "decision_candidates")
                status_records.append(
                    {
                        "symbol": spec.symbol,
                        "type": "candidate",
                        "timeframe": tf,
                        "rows": len(df),
                        "latest_timestamp": (
                            str(df.index.max()) if not df.empty else None
                        ),
                    }
                )
            except Exception:
                report_builder = ReportBuilder()

    # Check pools
    # In a real implementation we would list all profiles and timeframes.
    # For now we'll check the default ones.
    for tf in ["1d", "1h", "4h"]:
        for prof in [
            "balanced_directional_decision",
            "conservative_directional_decision",
        ]:
            if data_lake.has_decision_pool(tf, prof):
                try:
                    df = data_lake.load_decision_pool(tf, prof)
                    status_records.append(
                        {
                            "symbol": f"UNIVERSE_{prof}",
                            "type": "pool",
                            "timeframe": tf,
                            "rows": len(df),
                            "latest_timestamp": (
                                str(df["timestamp"].max())
                                if not df.empty and "timestamp" in df.columns
                                else None
                            ),
                        }
                    )
                except Exception:
                    report_builder = ReportBuilder()

    status_df = pd.DataFrame(status_records)

    summary = {
        "total_candidate_files": (
            len(status_df[status_df["type"] == "candidate"])
            if not status_df.empty
            else 0
        ),
        "total_pool_files": (
            len(status_df[status_df["type"] == "pool"]) if not status_df.empty else 0
        ),
        "symbols_with_decisions": (
            status_df[status_df["type"] == "candidate"]["symbol"].nunique()
            if not status_df.empty
            else 0
        ),
    }

    report = build_decision_status_report(status_df, summary)
    print("\n" + report)

    DECISION_REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    report_path = DECISION_REPORTS_DIR / "decision_status_report.txt"
    report_path.write_text(report, encoding="utf-8")

    if not status_df.empty:
        csv_path = DECISION_REPORTS_DIR / "decision_status.csv"
        status_df.to_csv(csv_path, index=False)

    logger.info("Decision status report saved.")


if __name__ == "__main__":
    main()
