import argparse
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from config.settings import settings
from config.paths import ProjectPaths
paths = ProjectPaths()
from data.storage.data_lake import DataLake
from documentation.doc_pipeline import DocumentationPipeline
import reports.report_builder as rb

def main():
    parser = argparse.ArgumentParser(description="Run Safe Usage Docs Report")
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

    print("Generating Safe Usage Docs Report...")
    saf_df, saf_summary = pipeline.build_safe_usage_docs_report(save=not args.no_save)

    if args.no_save:
        print("Dry run completed. Evaluated safety but did not save.")
    else:
        md_report = build_safe_usage_docs_markdown_report_local(saf_summary, saf_df)
        txt_report = rb.build_safe_usage_docs_text_report(saf_summary, saf_df)

        paths.REPORTS_DOCUMENTATION_MARKDOWN_DIR.mkdir(parents=True, exist_ok=True)
        paths.REPORTS_DOCUMENTATION_TXT_DIR.mkdir(parents=True, exist_ok=True)
        paths.REPORTS_DOCUMENTATION_CSV_DIR.mkdir(parents=True, exist_ok=True)

        with open(paths.REPORTS_DOCUMENTATION_MARKDOWN_DIR / "safe_usage_docs_report.md", "w", encoding="utf-8") as f:
            f.write(md_report)

        with open(paths.REPORTS_DOCUMENTATION_TXT_DIR / "safe_usage_docs_report.txt", "w", encoding="utf-8") as f:
            f.write(txt_report)

        if saf_df is not None and not saf_df.empty:
            saf_df.to_csv(paths.REPORTS_DOCUMENTATION_CSV_DIR / "documentation_safety_scan.csv", index=False)

        print("Safe Usage Docs Report generated successfully.")

def build_safe_usage_docs_markdown_report_local(summary, df):
    from documentation.doc_report_builder import build_safe_usage_docs_markdown_report
    return build_safe_usage_docs_markdown_report(summary, df)

if __name__ == "__main__":
    main()
