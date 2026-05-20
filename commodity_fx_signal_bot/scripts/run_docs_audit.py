import argparse
from pathlib import Path
from devtools.docs_audit import build_docs_audit_report
from devtools.dev_config import get_default_dev_experience_profile
from reports.report_builder import build_docs_audit_report as build_report

def main():
    parser = argparse.ArgumentParser(description="Run docs audit")
    parser.parse_args()

    project_root = Path(__file__).parent.parent
    output_dir = project_root / "reports" / "output" / "dev_reports"
    output_dir.mkdir(parents=True, exist_ok=True)

    profile = get_default_dev_experience_profile()
    df, summary = build_docs_audit_report(project_root, profile)

    df.to_csv(output_dir / "docs_audit.csv", index=False)

    report = build_report(df, summary)
    with open(output_dir / "docs_audit_report.txt", "w", encoding="utf-8") as f:
        f.write(report)

    print("Docs Audit report generated.")

if __name__ == "__main__":
    main()
