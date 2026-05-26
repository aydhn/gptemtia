import argparse
import sys
from pathlib import Path

# Add project root to path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from config.settings import settings
from config.paths import ProjectPaths
paths = ProjectPaths()
from data.storage.data_lake import DataLake
from documentation.doc_pipeline import DocumentationPipeline
import reports.report_builder as rb

def main():
    parser = argparse.ArgumentParser(description="Run Documentation Quality Report")
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

    print("Evaluating Documentation Quality...")
    quality, summary = pipeline.build_documentation_quality_report(save=not args.no_save)

    if args.no_save:
        print("Dry run completed. Evaluated quality but did not save.")
    else:
        md_report = build_documentation_quality_markdown_report_local(summary, quality)
        txt_report = rb.build_documentation_quality_text_report(summary, quality)

        paths.REPORTS_DOCUMENTATION_MARKDOWN_DIR.mkdir(parents=True, exist_ok=True)
        paths.REPORTS_DOCUMENTATION_TXT_DIR.mkdir(parents=True, exist_ok=True)
        paths.REPORTS_DOCUMENTATION_JSON_DIR.mkdir(parents=True, exist_ok=True)

        with open(paths.REPORTS_DOCUMENTATION_MARKDOWN_DIR / "documentation_quality_report.md", "w", encoding="utf-8") as f:
            f.write(md_report)

        with open(paths.REPORTS_DOCUMENTATION_TXT_DIR / "documentation_quality_report.txt", "w", encoding="utf-8") as f:
            f.write(txt_report)

        import json
        with open(paths.REPORTS_DOCUMENTATION_JSON_DIR / "documentation_quality_report.json", "w", encoding="utf-8") as f:
             json.dump(quality, f, indent=2)

        if not quality.get("passed"):
             print(f"WARNING: Documentation quality checks failed. Warnings: {quality.get('warnings')}")
        else:
             print("Documentation Quality Report generated successfully. All checks passed.")

def build_documentation_quality_markdown_report_local(summary, quality):
    from documentation.doc_report_builder import build_documentation_quality_markdown_report
    return build_documentation_quality_markdown_report(summary, quality)

if __name__ == "__main__":
    main()
