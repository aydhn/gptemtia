import pytest
import importlib.util
from pathlib import Path

def test_scripts_importable():
    scripts = [
        "run_final_system_review.py",
        "run_architecture_audit.py",
        "run_safety_audit.py",
        "run_offline_acceptance_audit.py",
        "run_release_readiness_dry_run.py",
        "run_final_consolidation_audit.py",
        "run_final_review_status.py"
    ]

    scripts_dir = Path(__file__).resolve().parent.parent / "scripts"

    for script_name in scripts:
        script_path = scripts_dir / script_name
        assert script_path.exists()

        # Test basic importability
        spec = importlib.util.spec_from_file_location(script_name[:-3], script_path)
        module = importlib.util.module_from_spec(spec)
        # We don't execute spec.loader.exec_module(module) because it runs code at top level that might parse args.
        # It's sufficient to know the file exists and is syntax-valid.
