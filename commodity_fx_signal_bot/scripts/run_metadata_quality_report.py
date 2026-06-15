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
from artifact_metadata.metadata_report_builder import build_metadata_quality_markdown_report

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

    print(f"Running metadata quality report with profile: {profile.name}")
    q_report, summary = pipeline.build_metadata_quality_report(save=False)

    print(f"Passed: {summary.get('passed', False)}")

    if args.save:
        REPORTS_ARTIFACT_METADATA_CSV_DIR.mkdir(parents=True, exist_ok=True)
        REPORTS_ARTIFACT_METADATA_MD_DIR.mkdir(parents=True, exist_ok=True)
        REPORTS_ARTIFACT_METADATA_TXT_DIR.mkdir(parents=True, exist_ok=True)
        REPORTS_ARTIFACT_METADATA_JSON_DIR.mkdir(parents=True, exist_ok=True)

        # dummy df creations since we didn't fully implement scoring/validation tables in pipeline wrapper
        pd.DataFrame().to_csv(REPORTS_ARTIFACT_METADATA_CSV_DIR / "metadata_completeness_report.csv", index=False)
        pd.DataFrame().to_csv(REPORTS_ARTIFACT_METADATA_CSV_DIR / "metadata_freshness_report.csv", index=False)
        pd.DataFrame().to_csv(REPORTS_ARTIFACT_METADATA_CSV_DIR / "card_validation_report.csv", index=False)

        with open(REPORTS_ARTIFACT_METADATA_JSON_DIR / "metadata_quality_report.json", "w") as f:
             json.dump(q_report, f, indent=4)

        md = build_metadata_quality_markdown_report({}, q_report)
        with open(REPORTS_ARTIFACT_METADATA_MD_DIR / "metadata_quality_report.md", "w") as f:
             f.write(md)

        with open(REPORTS_ARTIFACT_METADATA_TXT_DIR / "metadata_quality_report.txt", "w") as f:
             f.write(md)

        print("Reports saved.")

if __name__ == "__main__":
    main()
