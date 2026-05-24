import argparse
import sys
from pathlib import Path

from config.settings import settings
from config.paths import ProjectPaths
from data.storage.data_lake import DataLake
from research_planning.planning_config import get_research_planning_profile, ConfigError
from research_planning.planning_pipeline import ResearchPlanningPipeline

def main():
    parser = argparse.ArgumentParser(description="Generate Roadmap Health Report")
    parser.add_argument("--timeframe", type=str, default="1d", help="Timeframe (e.g. 1d)")
    parser.add_argument("--profile", type=str, default="balanced_research_planning", help="Planning profile")
    parser.add_argument("--save", type=bool, default=True, help="Save to Data Lake and Reports")

    args = parser.parse_args()

    try:
        profile = get_research_planning_profile(args.profile)
    except ConfigError as e:
        print(f"Error: {e}")
        sys.exit(1)

    project_root = Path(__file__).parent.parent
    paths = ProjectPaths(project_root)
    data_lake = DataLake(paths)

    print(f"Starting Roadmap Health Report for timeframe {args.timeframe} and profile {args.profile}...")
    pipeline = ResearchPlanningPipeline(data_lake, settings, project_root, profile)

    summary, _ = pipeline.build_roadmap_health_report(args.timeframe, args.save)

    print(f"Roadmap Status: {summary.get('roadmap_status', 'Unknown')}")
    print("WARNING: Roadmap Health indicates offline research capacity, NOT production readiness.")

if __name__ == "__main__":
    main()
