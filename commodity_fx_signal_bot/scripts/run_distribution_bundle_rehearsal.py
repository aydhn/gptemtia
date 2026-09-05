import argparse
import sys
from pathlib import Path
from config.settings import Settings
from data.storage.data_lake import DataLake
from local_distribution_packaging.packaging_pipeline import LocalDistributionPackagingPipeline
import config.paths as paths

def main():
    parser = argparse.ArgumentParser(description="Run run_distribution_bundle_rehearsal.py")
    parser.add_argument("--profile", type=str, default="balanced_local_distribution_packaging", help="Profile name")
    parser.add_argument("--save", action="store_true", default=True, help="Save outputs")
    parser.add_argument("--no-save", dest="save", action="store_false", help="Do not save outputs")
    args = parser.parse_args()

    print(f"Running run_distribution_bundle_rehearsal.py with profile: {args.profile}")
    settings = Settings()
    
    # Initialize DataLake safely by providing paths if possible, or string path
    try:
        data_lake = DataLake(paths)
    except:
        data_lake = DataLake("data/lake")
        
    pipeline = LocalDistributionPackagingPipeline(data_lake, settings, Path("."))
    
    # Mocking execution for run_distribution_bundle_rehearsal.py
    if "run_distribution_bundle_rehearsal.py" == "run_packaging_domain_registry.py":
        pipeline.build_packaging_domain_registry(save=args.save)
    elif "run_distribution_bundle_rehearsal.py" == "run_distribution_bundle_rehearsal.py":
        pipeline.build_distribution_bundle_rehearsal(save=args.save)
    elif "run_distribution_bundle_rehearsal.py" == "run_portable_docs_bundle.py":
        pipeline.build_portable_docs_bundle(save=args.save)
    elif "run_distribution_bundle_rehearsal.py" == "run_offline_release_folder_manifest.py":
        pipeline.build_offline_release_folder_manifest(save=args.save)
    elif "run_distribution_bundle_rehearsal.py" == "run_terminal_handover_zip_map.py":
        pipeline.build_terminal_handover_zip_map(save=args.save)
    elif "run_distribution_bundle_rehearsal.py" == "run_final_packaging_governance.py":
        pipeline.build_final_packaging_governance(save=args.save)
    elif "run_distribution_bundle_rehearsal.py" == "run_packaging_quality_report.py":
        pipeline.build_packaging_quality_report(save=args.save)
    elif "run_distribution_bundle_rehearsal.py" == "run_packaging_status.py":
        pipeline.build_packaging_status(save=args.save)
        
    print(f"Completed run_distribution_bundle_rehearsal.py")

if __name__ == "__main__":
    main()
