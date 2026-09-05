import subprocess
import sys
from pathlib import Path


def run_script(script_name: str) -> subprocess.CompletedProcess:
    root = Path(__file__).resolve().parent.parent
    cmd = [sys.executable, "-m", f"scripts.{script_name}"]
    return subprocess.run(cmd, cwd=str(root), capture_output=True, text=True)


def test_data_lineage_script_contracts():
    scripts = [
        "run_data_lineage_profile_registry",
        "run_provenance_source_registry",
        "run_provider_dataset_provenance",
        "run_transformation_lineage",
        "run_domain_lineage_registries",
        "run_news_provenance_boundary",
        "run_lineage_scoring",
        "run_data_lineage_health_check",
        "run_data_lineage_validation_report",
        "run_data_lineage_status",
    ]
    for sc in scripts:
        res = run_script(sc)
        assert res.returncode == 0, f"Script {sc} failed:\nSTDOUT: {res.stdout}\nSTDERR: {res.stderr}"
