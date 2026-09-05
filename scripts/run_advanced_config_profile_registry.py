import os
import sys
import pandas as pd
from config import settings
from data.storage.data_lake import DataLake
from advanced_config_profiles.advanced_config_pipeline import AdvancedConfigProfilePipeline

def main():
    print("Running advanced config profile registry...")
    dl = DataLake()
    pipeline = AdvancedConfigProfilePipeline(dl, settings, ".")
    df, summaries = pipeline.build_profile_registries(save=True)
    print("Completed. Total default registries generated:", len(df))

if __name__ == "__main__":
    main()
