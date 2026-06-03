import argparse
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from config.settings import settings
from data.storage.data_lake import DataLake
from portable_packaging.packaging_pipeline import PortablePackagingPipeline

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--save", action="store_true", default=True)
    parser.add_argument("--no-save", dest="save", action="store_false")
    args = parser.parse_args()

    print("Running Reproducible Setup Guide generation...")
    dl = DataLake(Path(__file__).resolve().parent.parent)
    pipeline = PortablePackagingPipeline(dl, settings, Path(__file__).resolve().parent.parent)

    md, summary = pipeline.build_reproducible_setup_guide(save=args.save)
    print("Reproducible Setup Guide generated.")

if __name__ == "__main__":
    main()
