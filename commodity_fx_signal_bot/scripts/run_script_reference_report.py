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
    parser = argparse.ArgumentParser(description="Run Script Reference Report")
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

    print("Generating Script Reference Report...")
    scripts_data = []
    scripts_dir = Path(__file__).resolve().parent
    for script in sorted(scripts_dir.glob("run_*.py")):
         scripts_data.append({
              "script": f"python -m scripts.{script.stem}",
              "type": "safe_command",
              "purpose": "Offline execution module"
         })

    scripts_df = pd.DataFrame(scripts_data)

    if args.no_save:
        print("Dry run completed. Built script reference but did not save.")
    else:
        md_report = build_script_reference_markdown_report_local({}, scripts_df)
        txt_report = rb.build_script_reference_text_report({}, scripts_df)

        paths.REPORTS_DOCUMENTATION_MARKDOWN_DIR.mkdir(parents=True, exist_ok=True)
        paths.REPORTS_DOCUMENTATION_TXT_DIR.mkdir(parents=True, exist_ok=True)
        paths.REPORTS_DOCUMENTATION_CSV_DIR.mkdir(parents=True, exist_ok=True)

        with open(paths.REPORTS_DOCUMENTATION_MARKDOWN_DIR / "script_reference_report.md", "w", encoding="utf-8") as f:
            f.write(md_report)

        with open(paths.REPORTS_DOCUMENTATION_TXT_DIR / "script_reference_report.txt", "w", encoding="utf-8") as f:
            f.write(txt_report)

        if scripts_df is not None and not scripts_df.empty:
            scripts_df.to_csv(paths.REPORTS_DOCUMENTATION_CSV_DIR / "script_reference.csv", index=False)

        print("Script Reference Report generated successfully.")

def build_script_reference_markdown_report_local(summary, df):
    from documentation.doc_report_builder import build_script_reference_markdown_report
    return build_script_reference_markdown_report(summary, df)

if __name__ == "__main__":
    main()
