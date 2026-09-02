import os
from pathlib import Path

base_dir = Path("c:/Users/immor/OneDrive/Belgeler/Projelerim/gptemtia/commodity_fx_signal_bot")
scripts_dir = base_dir / "scripts"

def gen_script(name):
    return f"""\
import argparse
import sys
from pathlib import Path

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", type=str, default="balanced_local_synthesis")
    parser.add_argument("--save", action="store_true", default=True)
    args = parser.parse_args()
    print("Running {name} with profile:", args.profile)

if __name__ == "__main__":
    main()
"""

scripts = [
    "run_synthesis_profile_registry.py",
    "run_master_index_unification.py",
    "run_cross_phase_final_map.py",
    "run_project_completion_dossier.py",
    "run_end_state_documentation.py",
    "run_synthesis_quality_report.py",
    "run_synthesis_status.py"
]

for s in scripts:
    with open(scripts_dir / s, "w", encoding="utf-8") as f:
        f.write(gen_script(s))
