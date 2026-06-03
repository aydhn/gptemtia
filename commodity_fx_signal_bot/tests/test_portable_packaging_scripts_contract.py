import subprocess
from pathlib import Path

def test_portable_packaging_scripts_importable():
    scripts_dir = Path("scripts")
    scripts = [
        "run_environment_snapshot.py",
        "run_dependency_inventory.py",
        "run_requirements_export.py",
        "run_install_verification.py",
        "run_portable_bundle_manifest.py",
        "run_reproducible_setup_guide.py",
        "run_packaging_status.py"
    ]
    for script in scripts:
        if (scripts_dir / script).exists():
            res = subprocess.run(["python", "-c", f"import scripts.{script.replace('.py', '')}"])
            assert res.returncode == 0
