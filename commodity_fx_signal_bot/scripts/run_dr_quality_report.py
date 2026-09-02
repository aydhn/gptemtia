
import argparse
import sys
from config.settings import Settings\nfrom config.paths import PROJECT_ROOT, paths
from data.storage.data_lake import DataLake
from pathlib import Path
from local_dr.dr_config import get_local_dr_profile

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", default="strict_dr_boundary")
    parser.add_argument("--save", action="store_true", default=True)
    args = parser.parse_args()
    
    settings = Settings()
    dl = DataLake(settings)
    try:
        from local_dr.dr_pipeline import LocalDRPipeline
        pipeline = LocalDRPipeline(dl, settings, Path("."), profile=get_local_dr_profile(args.profile))
        qual, sum_dict = pipeline.build_dr_quality_report(save=args.save)
        print("DR Quality Report generated successfully.")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
