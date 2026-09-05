"""Run script."""
import argparse
from pathlib import Path
from commodity_fx_signal_bot.config.settings import settings
from commodity_fx_signal_bot.config.paths import paths
from commodity_fx_signal_bot.data.storage.data_lake import DataLake
from commodity_fx_signal_bot.local_documentation_export.documentation_export_pipeline import LocalDocumentationExportPipeline
from commodity_fx_signal_bot.local_documentation_export.export_config import get_local_documentation_export_profile

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", type=str, default="balanced_local_documentation_export")
    parser.add_argument("--save", type=bool, default=True)
    args = parser.parse_args()
    print(f"Running {__file__} with profile {args.profile}")
    
    # Simple mocked call to pipeline
    dl = DataLake(paths, settings)
    profile = get_local_documentation_export_profile(args.profile)
    pipeline = LocalDocumentationExportPipeline(dl, settings, paths.project_root, profile)
    
    # Just to show it's hooked up
    pass

if __name__ == "__main__":
    main()
