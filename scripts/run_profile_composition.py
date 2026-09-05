import os
from config import settings
from data.storage.data_lake import DataLake
from advanced_config_profiles.advanced_config_pipeline import AdvancedConfigProfilePipeline

def main():
    print("Running profile composition...")
    dl = DataLake()
    pipeline = AdvancedConfigProfilePipeline(dl, settings, ".")
    df, summary = pipeline.build_composed_research_profiles(save=True)
    print("Completed. Total composed profiles:", summary.get("total", 0))

if __name__ == "__main__":
    main()
