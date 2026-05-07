import argparse
import logging
import pandas as pd
from pathlib import Path

from config.settings import settings
from config.paths import REPORTS_SIZING_REPORTS_DIR
from config.symbols import get_enabled_symbols
from data.storage.data_lake import DataLake
from sizing.sizing_pool import SizingCandidatePool
from reports.report_builder import build_sizing_status_report

logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(description="Check Sizing Status")
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO)

    data_lake = DataLake()
    specs = get_enabled_symbols()

    status_records = []
    total_pools = 0
    total_candidates = 0

    # Check individual sizing candidates
    for spec in specs:
        if spec.is_synthetic or spec.is_macro or spec.is_benchmark:
            continue

        timeframes = ["1d"]  # Simplify for status checking
        for tf in timeframes:
            try:
                if data_lake.has_features(spec, tf, "sizing_candidates"):
                    df = data_lake.load_features(spec, tf, "sizing_candidates")
                    if not df.empty:
                        total_candidates += len(df)
                        passed = (
                            len(df[df["sizing_label"] == "sizing_approved_candidate"])
                            if "sizing_label" in df.columns
                            else 0
                        )
                        status_records.append(
                            {
                                "symbol": spec.symbol,
                                "timeframe": tf,
                                "candidates": len(df),
                                "passed": passed,
                            }
                        )
            except Exception as e:
                logger.debug(f"Error checking status for {spec.symbol}: {e}")

    # Check pools
    profile_names = [
        "balanced_theoretical_sizing",
        "volatility_scaled_sizing",
        "conservative_theoretical_sizing",
        "forex_try_sizing",
        "metals_sizing",
    ]
    for p in profile_names:
        for tf in ["1d"]:
            try:
                if hasattr(data_lake, "has_sizing_pool") and data_lake.has_sizing_pool(
                    tf, p
                ):
                    total_pools += 1
            except Exception:
                pass

    summary = {"total_pools": total_pools, "total_candidates": total_candidates}

    status_df = pd.DataFrame(status_records)

    report_text = build_sizing_status_report(status_df, summary)
    print(report_text)

    REPORTS_SIZING_REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    report_path = REPORTS_SIZING_REPORTS_DIR / "sizing_status_report.txt"
    with open(report_path, "w") as f:
        f.write(report_text)

    csv_path = REPORTS_SIZING_REPORTS_DIR / "sizing_status.csv"
    if not status_df.empty:
        status_df.to_csv(csv_path, index=False)

    logger.info(f"Saved status report to {report_path} and {csv_path}")


if __name__ == "__main__":
    main()
