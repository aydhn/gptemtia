import os
from config import settings
from data.storage.data_lake import DataLake
from advanced_config_profiles.advanced_config_pipeline import AdvancedConfigProfilePipeline

def main():
    print("Running advanced config status...")
    dl = DataLake()
    pipeline = AdvancedConfigProfilePipeline(dl, settings, ".")
    df, summary = pipeline.build_advanced_config_status(save=True)
    print("Completed.")

if __name__ == "__main__":
    main()
