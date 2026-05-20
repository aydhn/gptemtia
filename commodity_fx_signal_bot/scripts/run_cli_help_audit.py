import argparse
from pathlib import Path
from devtools.cli_help_audit import audit_cli_help
from reports.report_builder import build_cli_help_audit_report

def main():
    parser = argparse.ArgumentParser(description="Run CLI help audit")
    parser.parse_args()

    project_root = Path(__file__).parent.parent
    output_dir = project_root / "reports" / "output" / "dev_reports"
    output_dir.mkdir(parents=True, exist_ok=True)

    df, summary = audit_cli_help(project_root)

    df.to_csv(output_dir / "cli_help_audit.csv", index=False)

    report = build_cli_help_audit_report(df, summary)
    with open(output_dir / "cli_help_audit_report.txt", "w", encoding="utf-8") as f:
        f.write(report)

    print("CLI Help Audit report generated.")

if __name__ == "__main__":
    main()
