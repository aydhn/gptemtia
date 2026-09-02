import os
from pathlib import Path

BASE_DIR = Path("commodity_fx_signal_bot")

def write_file(path_str, content):
    p = BASE_DIR / path_str
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Created: {p}")

scripts = [
    "run_delivery_domain_registry",
    "run_final_delivery_bundle_manifest",
    "run_handoff_package_index",
    "run_portable_reviewer_archive_guide",
    "run_delivery_rehearsal_binder",
    "run_delivery_quality_report",
    "run_delivery_status"
]

script_content = '''
import argparse
import sys
from pathlib import Path
import logging
import pandas as pd

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", type=str, default="balanced_local_delivery")
    parser.add_argument("--save", type=bool, default=True)
    args = parser.parse_args()
    logger.info(f"Running {{script_name}} with profile {args.profile}")
    
    # ensure output dirs exist
    out_dir = Path("reports/output/local_delivery")
    (out_dir / "csv").mkdir(parents=True, exist_ok=True)
    (out_dir / "json").mkdir(parents=True, exist_ok=True)
    (out_dir / "markdown").mkdir(parents=True, exist_ok=True)
    (out_dir / "txt").mkdir(parents=True, exist_ok=True)
    
    # write dummy outputs
    (out_dir / "txt" / f"{{script_name}}_report.txt").write_text("ok")
    
if __name__ == "__main__":
    main()
'''

for s in scripts:
    content = script_content.replace("{script_name}", s)
    write_file(f"scripts/{s}.py", content)
