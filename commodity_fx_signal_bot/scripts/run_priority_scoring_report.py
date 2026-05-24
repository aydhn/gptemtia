import argparse
import sys
from pathlib import Path

from config.settings import settings
from config.paths import ProjectPaths
from data.storage.data_lake import DataLake
from research_planning.planning_config import get_research_planning_profile, ConfigError
from research_planning.planning_pipeline import ResearchPlanningPipeline

def main():
    parser = argparse.ArgumentParser(description="Generate Priority Scoring Report")
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

    print(f"Starting Priority Scoring Report for timeframe {args.timeframe} and profile {args.profile}...")
    pipeline = ResearchPlanningPipeline(data_lake, settings, project_root, profile)

    df, summary = pipeline.build_priority_scoring_report(args.timeframe, args.save)

    print(f"Average priority score: {summary.get('average_score', 0.0):.2f}")
    print("WARNING: Priority scores indicate offline research priority, NOT live trading priority.")

if __name__ == "__main__":
    main()
