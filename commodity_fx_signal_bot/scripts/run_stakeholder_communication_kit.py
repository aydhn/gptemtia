import argparse
from pathlib import Path
from data.storage.data_lake import DataLake
from config.settings import Settings
from local_briefing.briefing_config import get_local_briefing_profile
from local_briefing.briefing_pipeline import LocalBriefingPipeline

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", type=str, default="balanced_local_briefing")
    parser.add_argument("--save", type=bool, default=True)
    args, _ = parser.parse_known_args()
    
    settings = Settings()
    data_lake = DataLake("data/lake")
    profile = get_local_briefing_profile(args.profile)
    
    pipeline = LocalBriefingPipeline(data_lake, settings, Path("."), profile)
    res, sum = pipeline.build_stakeholder_communication_kit(save=args.save)
    print(f"run_stakeholder_communication_kit completed.")

if __name__ == "__main__":
    main()
