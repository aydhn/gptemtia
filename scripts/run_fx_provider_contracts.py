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
    pipeline.build_fx_request_response_schemas()
    pipeline.build_fx_contracts()
    print("Success: run_fx_provider_contracts")

if __name__ == "__main__":
    main()
