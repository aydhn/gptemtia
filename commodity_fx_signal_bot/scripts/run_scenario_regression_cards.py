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
from artifact_metadata.metadata_report_builder import build_scenario_regression_cards_markdown_report

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

    print(f"Running scenario/regression cards with profile: {profile.name}")
    tables, summary = pipeline.build_scenario_regression_cards(save=False)

    print(f"Total scenario cards: {summary.get('total_scenario_cards', 0)}")

    if args.save:
        REPORTS_ARTIFACT_METADATA_CSV_DIR.mkdir(parents=True, exist_ok=True)
        REPORTS_ARTIFACT_METADATA_MD_DIR.mkdir(parents=True, exist_ok=True)
        REPORTS_ARTIFACT_METADATA_TXT_DIR.mkdir(parents=True, exist_ok=True)

        for name, df in tables.items():
            if not df.empty:
                df.to_csv(REPORTS_ARTIFACT_METADATA_CSV_DIR / f"{name}_registry.csv", index=False)

        md = build_scenario_regression_cards_markdown_report(summary)
        with open(REPORTS_ARTIFACT_METADATA_MD_DIR / "scenario_regression_cards_report.md", "w") as f:
             f.write(md)

        with open(REPORTS_ARTIFACT_METADATA_TXT_DIR / "scenario_regression_cards_report.txt", "w") as f:
             f.write(md)

        print("Reports saved.")

if __name__ == "__main__":
    main()
