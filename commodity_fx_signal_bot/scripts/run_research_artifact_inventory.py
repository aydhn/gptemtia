import argparse
import sys
from pathlib import Path
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import Settings
from config.paths import PROJECT_ROOT
REPORTS_ARTIFACT_METADATA_CSV_DIR = PROJECT_ROOT / "reports/output/artifact_metadata/csv"
REPORTS_ARTIFACT_METADATA_MD_DIR = PROJECT_ROOT / "reports/output/artifact_metadata/markdown"
REPORTS_ARTIFACT_METADATA_TXT_DIR = PROJECT_ROOT / "reports/output/artifact_metadata/txt"
REPORTS_ARTIFACT_METADATA_JSON_DIR = PROJECT_ROOT / "reports/output/artifact_metadata/json"
# from config.paths import REPORTS_ARTIFACT_METADATA_CSV_DIR, REPORTS_ARTIFACT_METADATA_MD_DIR, REPORTS_ARTIFACT_METADATA_TXT_DIR
from artifact_metadata.metadata_config import get_artifact_metadata_profile
from artifact_metadata.metadata_pipeline import ArtifactMetadataPipeline
from artifact_metadata.metadata_report_builder import build_research_artifact_inventory_markdown_report

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", type=str, default="balanced_local_metadata")
    parser.add_argument("--save", action="store_true", default=True)
    args = parser.parse_args()

    settings = Settings()
    profile = get_artifact_metadata_profile(args.profile)

    # Simple Mock DataLake
    class MockDataLake:
         pass

    pipeline = ArtifactMetadataPipeline(MockDataLake(PROJECT_ROOT / "data"), settings, PROJECT_ROOT, profile)

    print(f"Running research artifact inventory with profile: {profile.name}")
    df, summary = pipeline.build_research_artifact_inventory(save=False)

    print(f"Discovered artifacts: {summary.get('total_artifacts', 0)}")

    if args.save:
        # Mock save
        REPORTS_ARTIFACT_METADATA_CSV_DIR.mkdir(parents=True, exist_ok=True)
        REPORTS_ARTIFACT_METADATA_MD_DIR.mkdir(parents=True, exist_ok=True)
        REPORTS_ARTIFACT_METADATA_TXT_DIR.mkdir(parents=True, exist_ok=True)

        if not df.empty:
             df.to_csv(REPORTS_ARTIFACT_METADATA_CSV_DIR / "research_artifact_inventory.csv", index=False)
             df.to_csv(REPORTS_ARTIFACT_METADATA_CSV_DIR / "research_artifact_metadata_registry.csv", index=False)

        md = build_research_artifact_inventory_markdown_report(summary, df)
        with open(REPORTS_ARTIFACT_METADATA_MD_DIR / "research_artifact_inventory_report.md", "w") as f:
             f.write(md)

        with open(REPORTS_ARTIFACT_METADATA_TXT_DIR / "research_artifact_inventory_report.txt", "w") as f:
             f.write(md)

        print("Reports saved.")

if __name__ == "__main__":
    main()
