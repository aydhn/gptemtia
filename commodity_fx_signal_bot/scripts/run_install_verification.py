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

    print("Running Install Verification...")
    dl = DataLake(Path(__file__).resolve().parent.parent)
    pipeline = PortablePackagingPipeline(dl, settings, Path(__file__).resolve().parent.parent)

    df, summary = pipeline.build_install_verification_report(save=args.save)
    print("Install Verification generated.")
    print(f"Checks passed: {summary.get('passed_checks', 0)} / {summary.get('total_checks', 0)}")

if __name__ == "__main__":
    main()
