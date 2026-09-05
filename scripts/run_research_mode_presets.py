import os
from config import settings
from data.storage.data_lake import DataLake
from advanced_config_profiles.advanced_config_pipeline import AdvancedConfigProfilePipeline

def main():
    print("Running research mode presets...")
    dl = DataLake()
    pipeline = AdvancedConfigProfilePipeline(dl, settings, ".")
    df, summary = pipeline.build_research_mode_presets(save=True)
    print("Completed. Total presets:", summary.get("total_presets", 0))

if __name__ == "__main__":
    main()
