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
    parser = argparse.ArgumentParser(description="Run Output Reference Report")
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

    print("Generating Output Reference Report...")
    output_data = []

    base_dir = Path(__file__).resolve().parent.parent
    for d in [paths.lake_dir, paths.reports_dir]:
         if hasattr(d, "exists") and d.exists():
             for subdir in d.glob("*"):
                  if subdir.is_dir():
                       output_data.append({
                            "directory": str(subdir.relative_to(base_dir)),
                            "type": "data_lake" if "lake" in str(subdir) else "report",
                            "status": "active"
                       })

    outputs_df = pd.DataFrame(output_data)

    if args.no_save:
        print("Dry run completed. Built output reference but did not save.")
    else:
        md_report = build_output_reference_markdown_report_local({}, outputs_df)
        txt_report = rb.build_output_reference_text_report({}, outputs_df)

        paths.REPORTS_DOCUMENTATION_MARKDOWN_DIR.mkdir(parents=True, exist_ok=True)
        paths.REPORTS_DOCUMENTATION_TXT_DIR.mkdir(parents=True, exist_ok=True)
        paths.REPORTS_DOCUMENTATION_CSV_DIR.mkdir(parents=True, exist_ok=True)

        with open(paths.REPORTS_DOCUMENTATION_MARKDOWN_DIR / "output_reference_report.md", "w", encoding="utf-8") as f:
            f.write(md_report)

        with open(paths.REPORTS_DOCUMENTATION_TXT_DIR / "output_reference_report.txt", "w", encoding="utf-8") as f:
            f.write(txt_report)

        if outputs_df is not None and not outputs_df.empty:
            outputs_df.to_csv(paths.REPORTS_DOCUMENTATION_CSV_DIR / "output_reference.csv", index=False)

        print("Output Reference Report generated successfully.")

def build_output_reference_markdown_report_local(summary, df):
    from documentation.doc_report_builder import build_output_reference_markdown_report
    return build_output_reference_markdown_report(summary, df)

if __name__ == "__main__":
    main()
