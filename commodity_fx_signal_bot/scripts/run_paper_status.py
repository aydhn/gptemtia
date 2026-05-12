import argparse
import sys
import pandas as pd
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from config.settings import settings
import reports.report_builder as report_builder
def main():



    parser = argparse.ArgumentParser(description="Check status of paper runs in data lake")
    args = parser.parse_args()

    lake = DataLake(settings)

    print("Checking paper trading runs in data lake...")
    runs_df = lake.list_paper_runs()

    if runs_df.empty:
        print("No paper trading runs found.")
        return

    out_dir = Path("reports/output/paper_reports")
    out_dir.mkdir(parents=True, exist_ok=True)

    runs_df.to_csv(out_dir / "paper_status.csv", index=False)

    summary = {
        "total_runs": len(runs_df),
        "profiles": runs_df['profile_name'].unique().tolist() if 'profile_name' in runs_df else [],
        "timeframes": runs_df['timeframe'].unique().tolist() if 'timeframe' in runs_df else [],
        "symbols": len(runs_df['symbol'].unique()) if 'symbol' in runs_df else 0
    }

    report_text = report_builder.build_paper_status_report(runs_df, summary)

    out_file = out_dir / "paper_status_report.txt"
    with open(out_file, "w") as f:
        f.write(report_text)

    print(f"Report saved to {out_file}")
    print("\n" + "="*40 + "\n")
    print(report_text)

if __name__ == "__main__":
    main()
