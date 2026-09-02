"""
Run Archival Quality Report
"""
import argparse
import sys
import logging

logging.basicConfig(level=logging.INFO)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", type=str, default="balanced_local_archival")
    parser.add_argument("--save", type=bool, default=True)
    args = parser.parse_args()
    logging.info(f"Running run_archival_quality_report.py with profile={args.profile}")

if __name__ == "__main__":
    main()
