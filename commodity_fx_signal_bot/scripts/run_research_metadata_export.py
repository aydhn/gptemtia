import argparse
import sys
from pathlib import Path
import pandas as pd
import json

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import Settings
from config.paths import PROJECT_ROOT
REPORTS_ARTIFACT_METADATA_CSV_DIR = PROJECT_ROOT / "reports/output/artifact_metadata/csv"
REPORTS_ARTIFACT_METADATA_MD_DIR = PROJECT_ROOT / "reports/output/artifact_metadata/markdown"
REPORTS_ARTIFACT_METADATA_TXT_DIR = PROJECT_ROOT / "reports/output/artifact_metadata/txt"
REPORTS_ARTIFACT_METADATA_JSON_DIR = PROJECT_ROOT / "reports/output/artifact_metadata/json"
# from config.paths import REPORTS_ARTIFACT_METADATA_CSV_DIR, REPORTS_ARTIFACT_METADATA_MD_DIR, REPORTS_ARTIFACT_METADATA_TXT_DIR, REPORTS_ARTIFACT_METADATA_JSON_DIR
from artifact_metadata.metadata_config import get_artifact_metadata_profile
from artifact_metadata.metadata_pipeline import ArtifactMetadataPipeline
from artifact_metadata.metadata_report_builder import build_metadata_export_markdown_report

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", type=str, default="balanced_local_metadata")
    parser.add_argument("--save", action="store_true", default=True)
    args = parser.parse_args()

    settings = Settings()
    profile = get_artifact_metadata_profile(args.profile)

    class MockDataLake:
         pass

    pipeline = ArtifactMetadataPipeline(MockDataLake(), settings, PROJECT_ROOT, profile)

    print(f"Running research metadata export with profile: {profile.name}")
    tables, summary = pipeline.build_research_metadata_export(save=False)

    print(f"Total exports: {summary.get('total_exports', 0)}")

    if args.save:
        REPORTS_ARTIFACT_METADATA_CSV_DIR.mkdir(parents=True, exist_ok=True)
        REPORTS_ARTIFACT_METADATA_MD_DIR.mkdir(parents=True, exist_ok=True)
        REPORTS_ARTIFACT_METADATA_TXT_DIR.mkdir(parents=True, exist_ok=True)
        REPORTS_ARTIFACT_METADATA_JSON_DIR.mkdir(parents=True, exist_ok=True)

        for name, df in tables.items():
            if name != "export_index" and not df.empty:
                # Some are registry, some are cards. Just use .csv
                df.to_csv(REPORTS_ARTIFACT_METADATA_CSV_DIR / f"{name}{'_registry' if name == 'research_report_cards' else ''}.csv", index=False)

        with open(REPORTS_ARTIFACT_METADATA_JSON_DIR / "research_artifact_metadata_export.json", "w") as f:
             json.dump({"local_only": True}, f)

        md = build_metadata_export_markdown_report(summary)
        with open(REPORTS_ARTIFACT_METADATA_MD_DIR / "research_metadata_export_report.md", "w") as f:
             f.write(md)

        with open(REPORTS_ARTIFACT_METADATA_TXT_DIR / "research_metadata_export_report.txt", "w") as f:
             f.write(md)

        print("Reports saved.")

if __name__ == "__main__":
    main()
