"""
Script to run analyst command query.
"""
import argparse
from pathlib import Path
from data.storage.data_lake import DataLake
from config.settings import settings
from config.paths import ProjectPaths
from command_center.command_config import get_command_center_profile
from command_center.command_pipeline import CommandCenterPipeline

def main():
    parser = argparse.ArgumentParser(description="Run analyst command query")
    parser.add_argument("--query", type=str, required=True, help="The query text.")
    parser.add_argument("--profile", type=str, default="balanced_offline_command_center")
    parser.add_argument("--no-save", action="store_true")
    args = parser.parse_args()

    paths = ProjectPaths()
    data_lake = DataLake(paths=paths)
    profile = get_command_center_profile(args.profile)

    print(f"Running query: '{args.query}' with profile {profile.name}...")

    pipeline = CommandCenterPipeline(
        data_lake=data_lake,
        settings=settings,
        project_root=Path(__file__).parent.parent,
        profile=profile
    )

    df, summary = pipeline.build_analyst_command_query(query_text=args.query, save=not args.no_save)

    print(f"Found {summary.get('suggested_commands', 0)} suggested commands.")

if __name__ == "__main__":
    main()
