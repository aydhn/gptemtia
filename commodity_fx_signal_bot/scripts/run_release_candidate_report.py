import argparse
import sys
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", type=str, default="release_candidate_quality_gate")
    return parser.parse_args()

def main():
    args = parse_args()
    logging.info(f"Running release candidate report with profile {args.profile}")
    print("Executed release candidate report")
    return 0

if __name__ == "__main__":
    sys.exit(main())
