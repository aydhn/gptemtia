import argparse
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from config.settings import settings
from data.storage.data_lake import DataLake
from portable_packaging.packaging_config import get_portable_packaging_profile
from portable_packaging.packaging_pipeline import PortablePackagingPipeline

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", type=str, default="balanced_local_packaging")
    parser.add_argument("--save", action="store_true", default=True)
    parser.add_argument("--no-save", dest="save", action="store_false")
    args = parser.parse_args()

    print(f"Running Portable Bundle Manifest with profile: {args.profile}")
    dl = DataLake(Path(__file__).resolve().parent.parent)
    profile = get_portable_packaging_profile(args.profile)
    pipeline = PortablePackagingPipeline(dl, settings, Path(__file__).resolve().parent.parent, profile)

    df_map, summary = pipeline.build_portable_bundle_manifest_report(save=args.save)
    print("Portable Bundle Manifest generated.")
    print(f"Artifacts Included: {summary.get('included_artifacts', 0)}")

if __name__ == "__main__":
    main()
