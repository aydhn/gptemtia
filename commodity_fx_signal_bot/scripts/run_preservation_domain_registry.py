import argparse
import sys
from pathlib import Path
import pandas as pd
from local_post_completion_preservation.preservation_config import get_local_post_completion_preservation_profile, get_default_local_post_completion_preservation_profile
from local_post_completion_preservation.preservation_pipeline import LocalPostCompletionPreservationPipeline

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", type=str, default="balanced_local_preservation")
    parser.add_argument("--save", action="store_true", default=True)
    args = parser.parse_args()

    try:
        profile = get_local_post_completion_preservation_profile(args.profile)
    except Exception:
        profile = get_default_local_post_completion_preservation_profile()
    
    pipeline = LocalPostCompletionPreservationPipeline(None, None, Path("."), profile)
    pipeline.build_preservation_domain_registry(save=args.save)
    
    print("Done")

if __name__ == "__main__":
    main()
