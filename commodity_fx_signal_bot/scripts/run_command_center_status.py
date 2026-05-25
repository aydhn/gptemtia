"""
Script to generate the command center status report.
"""
import argparse
from pathlib import Path
from data.storage.data_lake import DataLake
from config.settings import settings
from config.paths import ProjectPaths
from command_center.command_config import get_command_center_profile
from command_center.command_pipeline import CommandCenterPipeline

def main():
    parser = argparse.ArgumentParser(description="Run command center status")
    parser.add_argument("--profile", type=str, default="balanced_offline_command_center")
    parser.add_argument("--no-save", action="store_true")
    args = parser.parse_args()

    paths = ProjectPaths()
    data_lake = DataLake(paths=paths)
    profile = get_command_center_profile(args.profile)

    print(f"Generating command center status report with profile {profile.name}...")

    pipeline = CommandCenterPipeline(
        data_lake=data_lake,
        settings=settings,
        project_root=Path(__file__).parent.parent,
        profile=profile
    )

    df, summary = pipeline.build_command_center_status(save=not args.no_save)

    print(f"Status generated for {summary['components_checked']} components.")

if __name__ == "__main__":
    main()
