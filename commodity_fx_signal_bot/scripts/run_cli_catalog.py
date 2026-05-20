import argparse
from pathlib import Path
from devtools.cli_catalog import build_cli_command_catalog, export_cli_catalog_markdown
from reports.report_builder import build_cli_catalog_report

def main():
    parser = argparse.ArgumentParser(description="Run CLI catalog generation")
    parser.parse_args()

    project_root = Path(__file__).parent.parent
    output_dir = project_root / "reports" / "output" / "dev_reports"
    output_dir.mkdir(parents=True, exist_ok=True)

    df, summary = build_cli_command_catalog(project_root)

    df.to_csv(output_dir / "cli_catalog.csv", index=False)

    md_content = export_cli_catalog_markdown(df)
    with open(output_dir / "cli_catalog.md", "w", encoding="utf-8") as f:
        f.write(md_content)

    report = build_cli_catalog_report(df, summary)
    with open(output_dir / "cli_catalog_report.txt", "w", encoding="utf-8") as f:
        f.write(report)

    print("CLI Catalog report generated.")

if __name__ == "__main__":
    main()
