import argparse
import sys
from pathlib import Path

# Add project root to path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from config.settings import settings
from config.paths import ProjectPaths
paths = ProjectPaths()
from data.storage.data_lake import DataLake
from documentation.documentation_config import get_documentation_profile
from documentation.doc_pipeline import DocumentationPipeline
import reports.report_builder as rb

def main():
    parser = argparse.ArgumentParser(description="Run Documentation Pack Report")
    parser.add_argument("--profile", type=str, default="balanced_documentation_pack", help="Documentation profile to use")
    parser.add_argument("--no-save", action="store_true", help="Do not save outputs")
    args = parser.parse_args()

    from config.paths import ensure_project_directories
    ensure_project_directories()

    try:
        profile = get_documentation_profile(args.profile)
    except Exception as e:
        print(f"Hata: {e}")
        return

    data_lake = DataLake(root_dir=paths)
    pipeline = DocumentationPipeline(
        data_lake=data_lake,
        settings=settings,
        project_root=Path(__file__).resolve().parent.parent,
        profile=profile
    )

    print(f"Starting Documentation Pack generation with profile: {profile.name}...")
    dfs, summary = pipeline.build_documentation_pack_report(save=not args.no_save)

    if args.no_save:
        print("Dry run completed. Generated content but did not save to DataLake/Reports.")
    else:
        # Generate Text / Markdown / CSV outputs
        docs_df = dfs.get("inventory")
        cov_df = dfs.get("coverage")

        md_report = build_documentation_pack_markdown_report_local(summary, docs_df)
        txt_report = rb.build_documentation_pack_text_report(summary, docs_df)

        paths.REPORTS_DOCUMENTATION_MARKDOWN_DIR.mkdir(parents=True, exist_ok=True)
        paths.REPORTS_DOCUMENTATION_TXT_DIR.mkdir(parents=True, exist_ok=True)
        paths.REPORTS_DOCUMENTATION_CSV_DIR.mkdir(parents=True, exist_ok=True)
        paths.REPORTS_DOCUMENTATION_JSON_DIR.mkdir(parents=True, exist_ok=True)

        with open(paths.REPORTS_DOCUMENTATION_MARKDOWN_DIR / "documentation_pack_report.md", "w", encoding="utf-8") as f:
            f.write(md_report)

        with open(paths.REPORTS_DOCUMENTATION_TXT_DIR / "documentation_pack_report.txt", "w", encoding="utf-8") as f:
            f.write(txt_report)

        if docs_df is not None and not docs_df.empty:
             docs_df.to_csv(paths.REPORTS_DOCUMENTATION_CSV_DIR / "documentation_inventory.csv", index=False)

        if cov_df is not None and not cov_df.empty:
             cov_df.to_csv(paths.REPORTS_DOCUMENTATION_CSV_DIR / "documentation_coverage.csv", index=False)

        import json
        with open(paths.REPORTS_DOCUMENTATION_JSON_DIR / "documentation_pack_manifest.json", "w", encoding="utf-8") as f:
             json.dump(summary, f, indent=2)

        print("Documentation Pack generated successfully.")

def build_documentation_pack_markdown_report_local(summary, docs_df):
    from documentation.doc_report_builder import build_documentation_pack_markdown_report
    return build_documentation_pack_markdown_report(summary, docs_df)

if __name__ == "__main__":
    main()
