"""
Script to generate the scenario registry report.
"""

import argparse
import sys
from pathlib import Path
import logging

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from config.settings import Settings
from config.paths import ensure_project_directories
from data.storage.data_lake import DataLake
from scenarios.scenario_config import get_scenario_profile
from scenarios.scenario_pipeline import ScenarioPipeline

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(description="Generate scenario registry report")
    parser.add_argument("--profile", type=str, default="balanced_offline_scenarios", help="Scenario profile name")
    parser.add_argument("--save", type=str, default="true", help="Save outputs (true/false)")

    args = parser.parse_args()
    save = args.save.lower() == "true"

    logger.info("Starting scenario registry generation...")

    settings = Settings()
    ensure_project_directories()

    if not settings.scenarios_enabled:
        logger.warning("Scenarios are disabled in settings.")
        return

    try:
        profile = get_scenario_profile(args.profile)
    except Exception as e:
        logger.error(f"Error loading profile: {e}")
        return

    from config.paths import PROJECT_ROOT
    data_lake = DataLake(PROJECT_ROOT)
    project_root = Path(__file__).parent.parent

    pipeline = ScenarioPipeline(data_lake, settings, project_root, profile)

    df, summary = pipeline.build_scenario_registry_report(save=save)

    if save:
        # Generate and save txt report
        from reports.report_builder import build_scenario_registry_text_report
        from config.paths import REPORTS_SCENARIOS_TXT_DIR
        txt_report = build_scenario_registry_text_report(summary, df)
        REPORTS_SCENARIOS_TXT_DIR.mkdir(parents=True, exist_ok=True)
        with open(REPORTS_SCENARIOS_TXT_DIR / "scenario_registry_report.txt", "w") as f:
            f.write(txt_report)

    logger.info(f"Done. Registry contains {summary.get('total_scenarios')} scenarios.")

if __name__ == "__main__":
    main()
