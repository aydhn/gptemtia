import os
from config import settings
from data.storage.data_lake import DataLake
from advanced_config_profiles.advanced_config_pipeline import AdvancedConfigProfilePipeline

def main():
    print("Running advanced config quality report...")
    dl = DataLake()
    pipeline = AdvancedConfigProfilePipeline(dl, settings, ".")
    pipeline.build_profile_registries(save=False)
    pipeline.build_research_mode_presets(save=False)
    pipeline.build_composed_research_profiles(save=False)
    pipeline.build_profile_compatibility_matrix(save=False)
    quality, score = pipeline.build_profile_quality_report(save=True)
    print("Completed. Quality check:", quality)

if __name__ == "__main__":
    main()
