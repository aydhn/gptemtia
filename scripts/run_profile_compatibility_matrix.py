import os
from config import settings
from data.storage.data_lake import DataLake
from advanced_config_profiles.advanced_config_pipeline import AdvancedConfigProfilePipeline

def main():
    print("Running profile compatibility matrix...")
    dl = DataLake()
    pipeline = AdvancedConfigProfilePipeline(dl, settings, ".")
    df, summary = pipeline.build_profile_compatibility_matrix(save=True)
    print("Completed. Total compatibility items:", summary.get("total", 0))

if __name__ == "__main__":
    main()
