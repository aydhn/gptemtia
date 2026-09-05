import sys
from pathlib import Path
project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

from config.settings import Settings
from data.storage.data_lake import DataLake
from advanced_fx_providers.fx_pipeline import FXProviderPipeline

def main():
    settings = Settings()
    data_lake = DataLake()
    pipeline = FXProviderPipeline(data_lake, settings, project_root)
    pipeline.build_fx_metadata_and_capabilities()
    pipeline.build_fx_registry_and_resolver()
    print("Success: run_fx_provider_registry")

if __name__ == "__main__":
    main()
