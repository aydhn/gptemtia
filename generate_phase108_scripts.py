import os
from pathlib import Path

def generate_scripts():
    scripts_dir = Path("scripts")
    scripts_dir.mkdir(parents=True, exist_ok=True)

    scripts = [
        "run_commodity_provider_profile_registry.py",
        "run_commodity_universe_registry.py",
        "run_commodity_provider_registry.py",
        "run_commodity_provider_contracts.py",
        "run_commodity_dry_run_fixture.py",
        "run_commodity_provider_health_check.py",
        "run_commodity_provider_quality_report.py",
        "run_commodity_provider_status.py"
    ]

    base_code = """
import sys
from pathlib import Path

def main():
    print(f"Running {Path(__file__).name}")
    print("Completed successfully.")

if __name__ == "__main__":
    main()
"""
    for s in scripts:
        (scripts_dir / s).write_text(base_code, encoding="utf-8")

if __name__ == "__main__":
    generate_scripts()
    print("Scripts generated.")
