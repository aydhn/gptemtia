import argparse
import sys
from pathlib import Path
import pandas as pd

# Add project root to sys.path
project_root = Path(__file__).parent.parent.resolve()
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from config.symbols import get_symbol_map
from data.storage.data_lake import DataLake
from config.paths import LAKE_DIR, REPORTS_LEVEL_REPORTS_DIR
import reports.report_builder as report_builder


def main():
    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    data_lake = DataLake(LAKE_DIR)

    status_rows = []

    for symbol, spec in get_symbol_map().items():
        if symbol != spec.symbol:
            continue  # skip aliases
        timeframes = ["1d"]
        for tf in timeframes:
            if data_lake.has_features(spec, tf, "level_candidates"):
                df = data_lake.load_features(spec, tf, "level_candidates")
                if not df.empty:
                    passed = len(df[df.get("passed_level_filters", False) == True])
                    avg_rr = (
                        df["reward_risk"].mean() if "reward_risk" in df.columns else 0.0
                    )
                    status_rows.append(
                        {
                            "symbol": symbol,
                            "timeframe": tf,
                            "total_candidates": len(df),
                            "passed": passed,
                            "average_reward_risk": avg_rr,
                        }
                    )

    status_df = pd.DataFrame(status_rows)

    report = report_builder.build_level_status_report(status_df, {})

    print(report)

    REPORTS_LEVEL_REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    out_txt = REPORTS_LEVEL_REPORTS_DIR / "level_status_report.txt"
    with open(out_txt, "w") as f:
        f.write(report)

    out_csv = REPORTS_LEVEL_REPORTS_DIR / "level_status.csv"
    if not status_df.empty:
        status_df.to_csv(out_csv, index=False)


if __name__ == "__main__":
    main()
