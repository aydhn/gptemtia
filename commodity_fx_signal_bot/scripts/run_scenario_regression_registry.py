import argparse
import sys
from pathlib import Path
from config.settings import settings
from data.storage.data_lake import DataLake
from scenario_regression.regression_config import get_scenario_regression_profile
from scenario_regression.regression_pipeline import ScenarioRegressionPipeline

def main():
    parser = argparse.ArgumentParser(description="Run Scenario Regression Registry")
    parser.add_argument("--profile", type=str, default=settings.default_scenario_regression_profile)
    parser.add_argument("--save", type=str, default="true")
    args = parser.parse_args()

    profile = get_scenario_regression_profile(args.profile)
    save = args.save.lower() == "true"
    project_root = Path(__file__).parent.parent

    from config.paths import LAKE_DIR
    dl = DataLake(LAKE_DIR)
    pipeline = ScenarioRegressionPipeline(dl, settings, project_root, profile)

    df, summary = pipeline.build_scenario_regression_registry(save=save)
    print("Scenario Regression Registry generated.")
    print(summary)

if __name__ == "__main__":
    main()
