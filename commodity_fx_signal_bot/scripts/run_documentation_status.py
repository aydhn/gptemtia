import argparse
import sys
import pandas as pd
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from config.settings import settings
from config.paths import ProjectPaths
paths = ProjectPaths()
from data.storage.data_lake import DataLake
from documentation.doc_pipeline import DocumentationPipeline
import reports.report_builder as rb

def main():
    parser = argparse.ArgumentParser(description="Run Documentation Status Report")
    parser.add_argument("--no-save", action="store_true", help="Do not save outputs")
    args = parser.parse_args()

    from config.paths import ensure_project_directories
    ensure_project_directories()

    data_lake = DataLake(root_dir=paths)
    pipeline = DocumentationPipeline(
        data_lake=data_lake,
        settings=settings,
        project_root=Path(__file__).resolve().parent.parent
    )

    print("Checking Documentation Status...")
    status_data = []

    target_files = [
        "docs/USER_GUIDE.md",
        "docs/OPERATOR_MANUAL.md",
        "docs/ANALYST_HANDBOOK.md",
        "docs/DEVELOPER_GUIDE.md",
        "docs/CODEX_AGENT_GUIDE.md",
        "docs/SAFE_USAGE_GUIDE.md",
        "docs/TROUBLESHOOTING_COOKBOOK.md",
        "docs/FAQ.md",
        "docs/GLOSSARY.md",
        "docs/DOCUMENTATION_INDEX.md",
        "docs/MODULE_MAP.md",
        "docs/SCRIPT_REFERENCE.md",
        "docs/OUTPUT_REFERENCE.md",
        "docs/SAFE_COMMAND_REFERENCE.md"
    ]

    base_dir = Path(__file__).resolve().parent.parent
    for tf in target_files:
        exists = (base_dir / tf).exists()
        status_data.append({
             "document": tf,
             "exists": exists,
             "status": "OK" if exists else "Missing"
        })

    status_df = pd.DataFrame(status_data)

    if args.no_save:
        print("Dry run completed. Checked status but did not save.")
    else:
        md_report = build_documentation_status_markdown_report_local({}, status_df)
        txt_report = rb.build_documentation_status_report(status_df, {})

        paths.REPORTS_DOCUMENTATION_MARKDOWN_DIR.mkdir(parents=True, exist_ok=True)
        paths.REPORTS_DOCUMENTATION_TXT_DIR.mkdir(parents=True, exist_ok=True)
        paths.REPORTS_DOCUMENTATION_CSV_DIR.mkdir(parents=True, exist_ok=True)

        with open(paths.REPORTS_DOCUMENTATION_MARKDOWN_DIR / "documentation_status_report.md", "w", encoding="utf-8") as f:
            f.write(md_report)

        with open(paths.REPORTS_DOCUMENTATION_TXT_DIR / "documentation_status_report.txt", "w", encoding="utf-8") as f:
            f.write(txt_report)

        if status_df is not None and not status_df.empty:
            status_df.to_csv(paths.REPORTS_DOCUMENTATION_CSV_DIR / "documentation_status.csv", index=False)

        print("Documentation Status Report generated successfully.")

def build_documentation_status_markdown_report_local(summary, df):
    from documentation.doc_report_builder import build_documentation_status_markdown_report
    return build_documentation_status_markdown_report(summary, df)

if __name__ == "__main__":
    main()
