import argparse
from pathlib import Path
from devtools.dx_pipeline import DeveloperExperiencePipeline
from reports.report_builder import build_local_dev_check_report
import pandas as pd

def main():
    parser = argparse.ArgumentParser(description="Run local dev check")
    parser.parse_args()

    project_root = Path(__file__).parent.parent
    output_dir = project_root / "reports" / "output" / "dev_reports"
    output_dir.mkdir(parents=True, exist_ok=True)

    pipeline = DeveloperExperiencePipeline(project_root)
    df, summary = pipeline.run_full_dx_check(save=False)

    summary_df = pd.DataFrame([summary])
    summary_df.to_csv(output_dir / "local_dev_check_summary.csv", index=False)

    report = build_local_dev_check_report(summary, df)
    with open(output_dir / "local_dev_check_report.txt", "w", encoding="utf-8") as f:
        f.write(report)

    print("Local Dev Check report generated.")

if __name__ == "__main__":
    main()
