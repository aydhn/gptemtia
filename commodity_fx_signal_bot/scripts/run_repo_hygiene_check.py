import argparse
from pathlib import Path
from devtools.repo_hygiene import build_repo_hygiene_report
from devtools.dev_config import get_default_dev_experience_profile
from reports.report_builder import build_repo_hygiene_report as build_report

def main():
    parser = argparse.ArgumentParser(description="Run repo hygiene check")
    parser.parse_args()

    project_root = Path(__file__).parent.parent
    output_dir = project_root / "reports" / "output" / "dev_reports"
    output_dir.mkdir(parents=True, exist_ok=True)

    profile = get_default_dev_experience_profile()
    df, summary = build_repo_hygiene_report(project_root, profile)

    df.to_csv(output_dir / "repo_hygiene.csv", index=False)

    report = build_report(df, summary)
    with open(output_dir / "repo_hygiene_report.txt", "w", encoding="utf-8") as f:
        f.write(report)

    print("Repo Hygiene report generated.")

if __name__ == "__main__":
    main()
