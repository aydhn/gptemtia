import argparse
import sys
from pathlib import Path

# Adjust path to import local_synthesis and others
sys.path.append(str(Path(__file__).parent.parent))

from config.settings import Settings
from config.paths import ProjectPaths, ensure_project_directories, LAKE_DIR
from data.storage.data_lake import DataLake
from local_synthesis.synthesis_config import get_local_synthesis_profile
from local_synthesis.synthesis_pipeline import LocalSynthesisPipeline

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", type=str, default="balanced_local_synthesis")
    parser.add_argument("--save", action="store_true", default=True)
    args = parser.parse_args()
    
    settings = Settings()
    paths = ProjectPaths()
    from config.paths import ensure_project_directories; ensure_project_directories()
    data_lake = DataLake(str(Path(__file__).parent.parent))
    
    profile = get_local_synthesis_profile(args.profile)
    pipeline = LocalSynthesisPipeline(data_lake, settings, Path(__file__).parent.parent, profile)
    
    pipeline.build_synthesis_profile_registry(save=args.save)
    print(f"Synthesis profile registry finished. Profile: {args.profile}")

if __name__ == '__main__':
    main()
